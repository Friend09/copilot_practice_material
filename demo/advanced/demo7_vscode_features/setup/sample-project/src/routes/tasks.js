const express = require('express');
const Joi = require('joi');

const router = express.Router();

// Task validation schema
const taskSchema = Joi.object({
  title: Joi.string().min(3).max(100).required(),
  description: Joi.string().max(500),
  priority: Joi.string().valid('low', 'medium', 'high').default('medium'),
  dueDate: Joi.date().iso(),
  tags: Joi.array().items(Joi.string())
});

// Mock tasks data
let tasks = [
  {
    id: 1,
    title: 'Complete project documentation',
    description: 'Write comprehensive documentation for the API',
    priority: 'high',
    status: 'in-progress',
    createdAt: new Date('2024-01-15'),
    updatedAt: new Date('2024-01-15')
  },
  {
    id: 2,
    title: 'Review security configurations',
    description: 'Audit all security settings and configurations',
    priority: 'medium',
    status: 'pending',
    createdAt: new Date('2024-01-16'),
    updatedAt: new Date('2024-01-16')
  }
];

/**
 * GET /api/v1/tasks
 * Get all tasks with optional filtering
 */
router.get('/', (req, res) => {
  try {
    const { status, priority, page = 1, limit = 10 } = req.query;

    let filteredTasks = [...tasks];

    // Apply filters
    if (status) {
      filteredTasks = filteredTasks.filter(task => task.status === status);
    }

    if (priority) {
      filteredTasks = filteredTasks.filter(task => task.priority === priority);
    }

    // Pagination
    const startIndex = (page - 1) * limit;
    const endIndex = startIndex + parseInt(limit);
    const paginatedTasks = filteredTasks.slice(startIndex, endIndex);

    res.json({
      status: 'success',
      data: {
        tasks: paginatedTasks,
        pagination: {
          currentPage: parseInt(page),
          totalPages: Math.ceil(filteredTasks.length / limit),
          totalItems: filteredTasks.length,
          itemsPerPage: parseInt(limit)
        }
      }
    });
  } catch (error) {
    res.status(500).json({
      status: 'error',
      message: 'Failed to fetch tasks',
      error: error.message
    });
  }
});

/**
 * POST /api/v1/tasks
 * Create a new task
 */
router.post('/', (req, res) => {
  try {
    // Validate request body
    const { error, value } = taskSchema.validate(req.body);
    if (error) {
      return res.status(400).json({
        status: 'error',
        message: 'Validation failed',
        details: error.details
      });
    }

    const newTask = {
      id: Date.now(), // Simple ID generation
      ...value,
      status: 'pending',
      createdAt: new Date(),
      updatedAt: new Date()
    };

    tasks.push(newTask);

    res.status(201).json({
      status: 'success',
      message: 'Task created successfully',
      data: { task: newTask }
    });
  } catch (error) {
    res.status(500).json({
      status: 'error',
      message: 'Failed to create task',
      error: error.message
    });
  }
});

/**
 * GET /api/v1/tasks/:id
 * Get a specific task by ID
 */
router.get('/:id', (req, res) => {
  try {
    const taskId = parseInt(req.params.id);
    const task = tasks.find(t => t.id === taskId);

    if (!task) {
      return res.status(404).json({
        status: 'error',
        message: 'Task not found'
      });
    }

    res.json({
      status: 'success',
      data: { task }
    });
  } catch (error) {
    res.status(500).json({
      status: 'error',
      message: 'Failed to fetch task',
      error: error.message
    });
  }
});

module.exports = router;
