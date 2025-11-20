# 08 - Copilot Extensions Ecosystem

## Introduction

GitHub Copilot Extensions, introduced in 2024, transform Copilot into an extensible platform. You can now integrate external services, custom APIs, and specialized tools directly into your Copilot Chat experience, creating a truly personalized AI development environment.

## The Copilot Extensibility Platform

### Architecture Overview

```
GitHub Copilot Chat (VS Code)
          ↓
GitHub Copilot Platform (routing, orchestration)
          ↓
Your Extension (Skillset or Agent)
          ↓
External Services (APIs, databases, tools)
```

### Two Extension Types

#### 1. Skillsets: Task-Specific Functions
- **Best for**: Focused, single-purpose operations
- **Complexity**: Low to medium
- **Control**: GitHub handles most of the heavy lifting
- **Examples**: Data retrieval, simple calculations, lookups

#### 2. Agents: Full-Control Extensions
- **Best for**: Complex, multi-step workflows
- **Complexity**: Medium to high
- **Control**: You manage everything
- **Examples**: Custom reasoning, stateful conversations, complex integrations

## Building Skillsets

### Anatomy of a Skillset

A skillset consists of up to 5 "skills"—individual functions that Copilot can invoke.

### Skillset Manifest

```json
{
  "schema_version": "1.0",
  "name": "my-skillset",
  "description": "Brief description of what this skillset does",
  "skills": [
    {
      "name": "skill_name",
      "description": "What this skill does",
      "function": {
        "name": "function_name",
        "description": "Detailed description for the AI model",
        "parameters": {
          "type": "object",
          "properties": {
            "param1": {
              "type": "string",
              "description": "Parameter description"
            }
          },
          "required": ["param1"]
        }
      },
      "endpoint": "https://your-api.com/skill"
    }
  ]
}
```

### Example: Weather Skillset

**Manifest:**
```json
{
  "schema_version": "1.0",
  "name": "weather-lookup",
  "description": "Get current weather information",
  "skills": [
    {
      "name": "get_current_weather",
      "description": "Retrieves current weather for a city",
      "function": {
        "name": "getCurrentWeather",
        "parameters": {
          "type": "object",
          "properties": {
            "city": {
              "type": "string",
              "description": "City name"
            },
            "units": {
              "type": "string",
              "enum": ["metric", "imperial"],
              "description": "Temperature units"
            }
          },
          "required": ["city"]
        }
      },
      "endpoint": "https://api.example.com/weather"
    }
  ]
}
```

**Implementation:**
```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/weather', methods=['POST'])
def get_current_weather():
    data = request.json
    city = data.get('city')
    units = data.get('units', 'metric')

    # Call actual weather API
    weather_data = fetch_weather(city, units)

    return jsonify({
        'city': city,
        'temperature': weather_data['temp'],
        'conditions': weather_data['conditions'],
        'humidity': weather_data['humidity']
    })
```

**Usage in Copilot:**
```
@weather-lookup What's the weather in Tokyo?
```

### Platform Benefits for Skillsets

GitHub's platform automatically handles:
- **Routing**: Directing user queries to the right skill
- **Parameter extraction**: Parsing user input for function parameters
- **Response formatting**: Presenting results in Copilot Chat
- **Error handling**: Basic error management
- **Rate limiting**: Preventing abuse

## Building Agents

### When to Use Agents

Choose agents when you need:
- **Custom conversation flow**
- **State management** across interactions
- **Integration with multiple services**
- **Custom LLM or reasoning logic**
- **Complex data processing**
- **Fine-grained control** over responses

### Agent Structure

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Store conversation state
conversation_state = {}

@app.route('/agent', methods=['POST'])
def agent_endpoint():
    """
    Main agent endpoint
    Receives messages from Copilot and returns responses
    """
    data = request.json

    # Extract conversation details
    session_id = data.get('session_id', 'default')
    messages = data.get('messages', [])
    user_message = messages[-1]['content'] if messages else ''

    # Initialize or retrieve state
    if session_id not in conversation_state:
        conversation_state[session_id] = {
            'history': [],
            'context': {}
        }

    state = conversation_state[session_id]

    # Process request
    response_content = process_message(user_message, state)

    # Update state
    state['history'].append({
        'user': user_message,
        'assistant': response_content
    })

    # Return response in expected format
    return jsonify({
        'choices': [{
            'message': {
                'role': 'assistant',
                'content': response_content
            }
        }]
    })

def process_message(message, state):
    """Custom logic to process user messages"""
    # Implement your custom logic here
    # Access external APIs, databases, etc.
    # Use state for context-aware responses
    return "Your response"
```

### Agent Capabilities

#### 1. Multi-Step Workflows
```python
def process_message(message, state):
    if 'step' not in state['context']:
        state['context']['step'] = 1

    step = state['context']['step']

    if step == 1:
        # First step logic
        state['context']['step'] = 2
        return "Step 1 complete. Proceeding to step 2..."
    elif step == 2:
        # Second step logic
        state['context']['step'] = 3
        return "Step 2 complete. Final step..."
    else:
        # Final step
        state['context']['step'] = 1  # Reset
        return "Task complete!"
```

#### 2. External API Integration
```python
import requests

def process_message(message, state):
    # Call external API
    response = requests.get('https://api.example.com/data')
    data = response.json()

    # Process and return
    return f"Retrieved data: {data['result']}"
```

#### 3. Database Queries
```python
import sqlite3

def process_message(message, state):
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE status='active'")
    results = cursor.fetchall()
    conn.close()

    return f"Found {len(results)} active users"
```

#### 4. Custom LLM Integration
```python
from openai import OpenAI

client = OpenAI(api_key='your-key')

def process_message(message, state):
    # Use your own LLM for processing
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Custom system prompt"},
            {"role": "user", "content": message}
        ]
    )

    return response.choices[0].message.content
```

## Real-World Extension Examples

### 1. Jira Integration Skillset

**Skills:**
- `search_issues` - Search Jira issues
- `create_issue` - Create new issue
- `update_issue` - Update existing issue
- `get_issue_details` - Get full issue information
- `list_my_issues` - Get issues assigned to user

**Usage:**
```
@jira Show me my open bugs
@jira Create a bug for login error
@jira Update PROJ-123 status to In Progress
```

### 2. Documentation Search Agent

**Capabilities:**
- Search internal documentation
- Understand context from current code
- Provide relevant code examples
- Link to specific doc sections
- Remember previous searches in conversation

**Usage:**
```
@docs How do I implement OAuth in our framework?
@docs Show me examples of rate limiting
@docs What's our convention for error handling?
```

### 3. Code Review Assistant Agent

**Features:**
- Analyze code for common issues
- Check against team style guide
- Suggest improvements
- Remember previous review feedback
- Learn from accepted suggestions

**Usage:**
```
@code-review Review this function for security issues
@code-review Check if this follows our Python style guide
@code-review Suggest performance improvements
```

### 4. CI/CD Status Skillset

**Skills:**
- `get_build_status` - Check build status
- `get_test_results` - Retrieve test results
- `trigger_deployment` - Start deployment
- `rollback_deployment` - Revert to previous version
- `get_pipeline_logs` - Fetch logs

**Usage:**
```
@cicd What's the status of the main branch build?
@cicd Deploy staging to production
@cicd Show me why the tests failed
```

## Security Best Practices

### 1. Authentication
```python
@app.before_request
def verify_request():
    # Verify request is from GitHub Copilot
    token = request.headers.get('Authorization')
    if not verify_github_token(token):
        abort(401, description="Unauthorized")
```

### 2. Input Validation
```python
def validate_input(data):
    required_fields = ['city', 'units']
    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing field: {field}")

    # Sanitize inputs
    data['city'] = sanitize_string(data['city'])
```

### 3. Rate Limiting
```python
from flask_limiter import Limiter

limiter = Limiter(app)

@app.route('/skill')
@limiter.limit("100/hour")
def skill_endpoint():
    pass
```

### 4. Data Privacy
```python
# Don't log sensitive information
@app.route('/skill', methods=['POST'])
def skill_endpoint():
    data = request.json
    # Mask sensitive fields before logging
    safe_data = {k: v for k, v in data.items() if k not in ['password', 'token']}
    logger.info(f"Request: {safe_data}")
```

## Deployment

### Hosting Options

#### 1. Serverless Functions
- **AWS Lambda**
- **Azure Functions**
- **Google Cloud Functions**
- **Vercel/Netlify Functions**

**Pros**: Auto-scaling, pay per use, easy setup
**Cons**: Cold start latency, execution time limits

#### 2. Container Platforms
- **Google Cloud Run**
- **AWS ECS/Fargate**
- **Azure Container Instances**

**Pros**: Flexible, stateful, full control
**Cons**: More complex, always running costs

#### 3. Traditional Servers
- **Heroku**
- **DigitalOcean**
- **AWS EC2**

**Pros**: Complete control, persistent state
**Cons**: Manual scaling, higher costs

### Deployment Example (Cloud Run)

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app
```

```bash
# Build and deploy
gcloud builds submit --tag gcr.io/PROJECT/skillset
gcloud run deploy skillset --image gcr.io/PROJECT/skillset --platform managed
```

## Publishing Your Extension

### 1. Prepare Documentation
- Clear description of functionality
- Usage examples
- Configuration instructions
- API reference

### 2. Register with GitHub
- Create GitHub App
- Configure OAuth (if needed)
- Set up webhooks
- Define permissions

### 3. Submit to Marketplace
- Complete marketplace listing
- Add screenshots/demos
- Set pricing (free or paid)
- Submit for review

### 4. Promote
- Blog post announcement
- Demo video
- Community engagement
- Gather user feedback

## Monitoring and Maintenance

### Metrics to Track
- Request volume
- Response time
- Error rates
- User satisfaction
- Feature usage

### Logging
```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/skill', methods=['POST'])
def skill_endpoint():
    logger.info(f"Request received: {request.json}")
    try:
        result = process_request(request.json)
        logger.info(f"Request successful")
        return jsonify(result)
    except Exception as e:
        logger.error(f"Request failed: {str(e)}")
        raise
```

## Key Takeaways

1. **Skillsets are ideal for simple, focused tasks**
2. **Agents provide full control for complex scenarios**
3. **Security and validation are critical**
4. **Start simple, iterate based on usage**
5. **Good documentation improves adoption**
6. **Monitor and optimize performance**

## Further Reading

- Module 08: Hands-on extension building exercises
- Module 09: Prompt Files for extension usage patterns
- GitHub Copilot Extensions Documentation

## References

[1] GitHub Copilot Extensions Documentation. [https://docs.github.com/en/copilot/building-copilot-extensions](https://docs.github.com/en/copilot/building-copilot-extensions)
[2] Copilot Skillsets Guide. [https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-skillset-for-your-copilot-extension](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-skillset-for-your-copilot-extension)
[3] Copilot Agents Guide. [https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension)
