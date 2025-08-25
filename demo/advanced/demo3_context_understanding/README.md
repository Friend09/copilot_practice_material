# Demo 3: Context Understanding & Workspace Awareness

## What This Demo Shows

- **Multi-file project comprehension**: Copilot understands entire codebase
- **Architectural pattern recognition**: Maintains consistency across services
- **Cross-file dependency management**: Intelligent imports and references
- **Service boundary understanding**: Respects microservice separation

**Duration**: 15-18 minutes
**Complexity**: Advanced
**Best For**: Technical architects, senior developers

---

## Quick Setup (2 minutes)

### 1. Navigate to Demo Folder

```bash
cd demo/advanced/demo3_context_understanding
```

### 2. Review Foundation Files

- Open `setup/base_models.py` - Base classes and domain models
- Open `setup/service_interfaces.py` - Service contracts and patterns

### 3. Open Copilot Chat

Press `Ctrl/Cmd + Shift + I` to open Copilot Chat

---

## Demo Steps

### Step 1: Show the Foundation (3 minutes)

1. Open both setup files side by side
2. Explain the architectural patterns established
3. Point out the interfaces that Copilot will implement

### Step 2: Context-Aware Service Creation (10 minutes)

Use prompts from `prompts.md` in sequence:

1. **UserService Implementation**:

   ```text
   Create a UserService class that implements UserServiceInterface
   following the BaseService pattern defined in this file
   ```

2. **ProductService with Patterns**:

   ```text
   Create ProductService with inventory management, following
   the same patterns as UserService
   ```

3. **OrderService Coordination**:
   ```text
   Create OrderService that coordinates UserService and ProductService
   for order processing
   ```

### Step 3: Show Cross-File Understanding (5 minutes)

- Demonstrate that Copilot maintains consistent patterns
- Show how it references base classes correctly
- Point out intelligent import suggestions

---

## Expected Results

Copilot should generate services that:

- ✅ Inherit from BaseService correctly
- ✅ Implement all interface methods
- ✅ Use domain models appropriately
- ✅ Maintain consistent patterns across services
- ✅ Handle cross-service dependencies intelligently

---

## Key Demo Messages

1. **"Copilot thinks beyond single files"** - Understands entire project context
2. **"Architectural consistency is automatic"** - Patterns maintained across codebase
3. **"Complex workflows work seamlessly"** - Multi-service operations understood
4. **"Enterprise-ready suggestions"** - Proper error handling and best practices

---

## Success Metrics

After this demo, your audience should understand:

- ✅ Context understanding goes beyond autocomplete
- ✅ Architectural patterns are preserved automatically
- ✅ Cross-service logic is handled intelligently
- ✅ Enterprise development scales with AI assistance
