# Week 1 Project: Command-Line Todo Application

## Project Overview
Build a command-line todo application using Python and GitHub Copilot. This project will help you practice using Copilot for a complete, real-world application.

## Features to Implement

### Core Features
1. **Add Tasks**: Add new todo items with descriptions
2. **List Tasks**: Display all tasks with their status
3. **Mark Complete**: Mark tasks as completed
4. **Delete Tasks**: Remove tasks from the list
5. **Save/Load**: Persist tasks to a file

### Advanced Features (Optional)
1. **Due Dates**: Add due dates to tasks
2. **Priorities**: Set task priorities (high, medium, low)
3. **Categories**: Organize tasks by category
4. **Search**: Find tasks by keyword
5. **Statistics**: Show completion statistics

## Project Structure
```
todo-app/
├── main.py          # Main application entry point
├── todo.py          # Todo class and core logic
├── storage.py       # File I/O operations
├── cli.py           # Command-line interface
└── tasks.json       # Data storage file
```

## Implementation Guidelines

### Using Copilot Effectively
1. **Start with Comments**: Write detailed comments describing each function
2. **Use Examples**: Provide examples of expected input/output
3. **Iterate**: Refine your prompts based on Copilot's suggestions
4. **Review Code**: Always review and test generated code

### Suggested Prompts
- "Create a Todo class that stores task description, completion status, and creation date"
- "Implement a function to save todo list to JSON file"
- "Create a command-line interface that accepts commands like 'add', 'list', 'complete'"

## Getting Started

1. Create the project directory and files
2. Start with the Todo class in `todo.py`
3. Implement file storage in `storage.py`
4. Build the CLI in `cli.py`
5. Create the main application loop in `main.py`

## Testing Your Application

Test these scenarios:
- Add multiple tasks
- Mark some as complete
- Save and reload the application
- Handle invalid input gracefully

## Success Criteria

Your application should:
- ✅ Allow adding, listing, and completing tasks
- ✅ Persist data between sessions
- ✅ Handle user input validation
- ✅ Provide clear user feedback
- ✅ Be built primarily using Copilot suggestions

## Next Steps

After completing this project, you'll be ready for more complex applications in Week 2!

