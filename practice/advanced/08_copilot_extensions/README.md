# Module 08 – Copilot Extensions: Building Skillsets and Custom Agents

## 🎯 Overview

GitHub Copilot Extensions allow you to extend Copilot's capabilities by integrating external services, APIs, and custom logic. This module teaches you how to build both **Skillsets** (simple, task-specific extensions) and **Agents** (complex, full-control extensions).

## What are Copilot Extensions?

Copilot Extensions integrate external tools and services directly into your Copilot Chat experience. They enable Copilot to:

- Access external APIs and databases
- Retrieve real-time data
- Perform custom operations
- Integrate third-party services
- Execute custom business logic

## Skillsets vs Agents

### 🎯 Skillsets (Simple Extensions)

**Best for**: Straightforward tasks like data retrieval, simple operations

**Characteristics**:
- Up to 5 specific skills per skillset
- GitHub handles routing and response generation
- Minimal code required
- Quick to build and deploy
- Limited control over conversation flow

**Use Cases**:
- Fetch data from APIs
- Query databases
- Look up documentation
- Retrieve tickets from project management tools
- Search internal knowledge bases

### 🤖 Agents (Complex Extensions)

**Best for**: Complex integrations requiring full control

**Characteristics**:
- Complete control over request processing
- Custom response generation
- Can use any LLM (not just GitHub's)
- Manage conversation context
- Handle complex workflows
- More code but more flexibility

**Use Cases**:
- Multi-step workflows
- Custom reasoning logic
- Integration with multiple services
- Stateful conversations
- Complex data transformations
- Custom authentication flows

## Architecture

```
User Input → Copilot Chat → GitHub Copilot Platform → Your Extension
                                                              ↓
                                                    External APIs/Services
                                                              ↓
Your Extension → Response Processing → GitHub Platform → Copilot Chat → User
```

## Exercise 1: Understanding Skillsets

### Scenario: Weather Lookup Skillset

Build a simple skillset that fetches weather data.

### Skillset Definition

```json
{
  "schema_version": "1",
  "name": "weather-lookup",
  "description": "Fetch current weather for any city",
  "skills": [
    {
      "name": "get_weather",
      "description": "Get current weather for a specified city",
      "function": {
        "name": "get_weather",
        "description": "Retrieves current weather data",
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
      "endpoint": "https://your-api.com/weather"
    }
  ]
}
```

### Implementation (Python/Flask)

```python
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/weather', methods=['POST'])
def get_weather():
    data = request.json
    city = data.get('city')
    units = data.get('units', 'metric')

    # Call actual weather API (example: OpenWeatherMap)
    api_key = 'YOUR_API_KEY'
    url = f'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'units': units,
        'appid': api_key
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        return jsonify({
            'city': city,
            'temperature': weather_data['main']['temp'],
            'description': weather_data['weather'][0]['description'],
            'humidity': weather_data['main']['humidity']
        })
    else:
        return jsonify({'error': 'City not found'}), 404

if __name__ == '__main__':
    app.run(port=5000)
```

### Testing

Once deployed, users can ask:
```
@weather-lookup What's the weather in London?
```

## Exercise 2: Building a Simple Agent

### Scenario: Code Analysis Agent

Build an agent that analyzes code complexity and suggests improvements.

### Agent Structure

```python
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/agent', methods=['POST'])
def agent_endpoint():
    """
    Main agent endpoint that receives Copilot requests
    """
    data = request.json

    # Extract message and context
    messages = data.get('messages', [])
    user_message = messages[-1]['content'] if messages else ''

    # Process request
    response = process_request(user_message, messages)

    return jsonify({
        'choices': [{
            'message': {
                'role': 'assistant',
                'content': response
            }
        }]
    })

def process_request(user_message, conversation_history):
    """
    Custom logic to process user requests
    """
    # Extract code from message
    code = extract_code_from_message(user_message)

    if not code:
        return "Please provide code to analyze."

    # Analyze code
    analysis = analyze_code_complexity(code)
    suggestions = generate_suggestions(analysis)

    # Format response
    response = f"""
## Code Analysis Results

**Complexity Score**: {analysis['complexity']}/10

**Metrics**:
- Lines of Code: {analysis['lines']}
- Cyclomatic Complexity: {analysis['cyclomatic']}
- Maintainability Index: {analysis['maintainability']}

**Suggestions**:
{chr(10).join(f"- {s}" for s in suggestions)}
"""

    return response

def analyze_code_complexity(code):
    """
    Analyze code and return metrics
    """
    # Simplified analysis (use real tools like radon in production)
    lines = len(code.split('\n'))

    # Count control flow statements
    cyclomatic = code.count('if ') + code.count('for ') + code.count('while ')

    # Simple complexity score
    complexity = min(10, (lines // 10) + cyclomatic)

    return {
        'lines': lines,
        'cyclomatic': cyclomatic,
        'complexity': complexity,
        'maintainability': max(0, 100 - (complexity * 10))
    }

def generate_suggestions(analysis):
    """
    Generate improvement suggestions based on analysis
    """
    suggestions = []

    if analysis['complexity'] > 7:
        suggestions.append("Consider breaking down complex functions")

    if analysis['lines'] > 100:
        suggestions.append("Function is too long, consider splitting")

    if analysis['cyclomatic'] > 10:
        suggestions.append("High cyclomatic complexity, refactor conditional logic")

    if not suggestions:
        suggestions.append("Code looks good! Well structured and maintainable.")

    return suggestions

def extract_code_from_message(message):
    """
    Extract code block from markdown message
    """
    # Simple extraction (improve for production)
    if '```' in message:
        parts = message.split('```')
        if len(parts) >= 2:
            code = parts[1]
            # Remove language identifier
            if '\n' in code:
                code = code.split('\n', 1)[1]
            return code.strip()
    return message

if __name__ == '__main__':
    app.run(port=5000)
```

### Usage

```
@code-analyzer Analyze this function:

```python
def complex_function(data):
    result = []
    for item in data:
        if item > 0:
            if item % 2 == 0:
                result.append(item * 2)
            else:
                result.append(item * 3)
    return result
```
```

## Exercise 3: Multi-Skill Skillset

### Scenario: Database Query Skillset

Build a skillset with multiple related skills.

### Skills:
1. **execute_query** - Run SQL query
2. **list_tables** - Show available tables
3. **describe_table** - Show table schema
4. **query_history** - Show recent queries
5. **optimize_query** - Suggest query improvements

### Implementation Outline

```python
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DB_PATH = 'example.db'

@app.route('/execute_query', methods=['POST'])
def execute_query():
    data = request.json
    query = data.get('query')

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()

        return jsonify({
            'success': True,
            'results': results,
            'row_count': len(results)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@app.route('/list_tables', methods=['POST'])
def list_tables():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = [row[0] for row in cursor.fetchall()]
        conn.close()

        return jsonify({
            'tables': tables
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/describe_table', methods=['POST'])
def describe_table():
    data = request.json
    table_name = data.get('table_name')

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = cursor.fetchall()
        conn.close()

        return jsonify({
            'table': table_name,
            'columns': [
                {
                    'name': col[1],
                    'type': col[2],
                    'nullable': not col[3],
                    'primary_key': bool(col[5])
                }
                for col in columns
            ]
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Implement query_history and optimize_query similarly
```

## Exercise 4: Advanced Agent with State

### Scenario: Conversational Code Review Agent

Build an agent that maintains conversation state for iterative code reviews.

### Features:
- Remember previous code submissions
- Track suggested improvements
- Follow up on implemented changes
- Generate diff reports

### Key Implementation Points

```python
# Store conversation state
conversation_states = {}

@app.route('/agent', methods=['POST'])
def code_review_agent():
    data = request.json
    session_id = data.get('session_id', 'default')
    messages = data.get('messages', [])

    # Get or create state
    if session_id not in conversation_states:
        conversation_states[session_id] = {
            'code_history': [],
            'suggestions': [],
            'iterations': 0
        }

    state = conversation_states[session_id]

    # Process message
    user_message = messages[-1]['content']
    response = process_code_review(user_message, state)

    return jsonify({
        'choices': [{
            'message': {
                'role': 'assistant',
                'content': response
            }
        }]
    })

def process_code_review(message, state):
    # Extract code
    code = extract_code_from_message(message)

    if code:
        # Store in history
        state['code_history'].append(code)
        state['iterations'] += 1

        # Compare with previous version if exists
        if len(state['code_history']) > 1:
            previous_code = state['code_history'][-2]
            improvements = compare_versions(previous_code, code)
            response = f"Great! I see you've made changes. Here's what improved:\n\n"
            response += "\n".join(f"✅ {imp}" for imp in improvements)
            response += "\n\n"
        else:
            response = "Thanks for sharing your code. Let me review it:\n\n"

        # Perform review
        issues = review_code(code)

        if issues:
            response += "**Issues found:**\n"
            response += "\n".join(f"❌ {issue}" for issue in issues)
            state['suggestions'] = issues
        else:
            response += "**No issues found!** This code looks good. 🎉"
            state['suggestions'] = []

        return response
    else:
        return "Please provide code to review."
```

## Deployment Options

### 1. GitHub Actions
- Use GitHub-hosted runners
- Serverless execution
- Free for public repos

### 2. Cloud Platforms
- AWS Lambda
- Azure Functions
- Google Cloud Functions
- Vercel/Netlify for simple APIs

### 3. Container Platforms
- Docker containers
- Kubernetes
- Cloud Run

### 4. Traditional Servers
- VPS (DigitalOcean, Linode)
- Dedicated servers
- On-premises

## Security Best Practices

### 1. Authentication
```python
@app.before_request
def verify_github_signature():
    # Verify request is from GitHub
    signature = request.headers.get('X-GitHub-Signature')
    if not verify_signature(request.data, signature):
        abort(401)
```

### 2. Input Validation
```python
def validate_input(data):
    required_fields = ['city', 'units']
    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing required field: {field}")
```

### 3. Rate Limiting
```python
from flask_limiter import Limiter

limiter = Limiter(app, key_func=lambda: request.headers.get('X-Client-ID'))

@app.route('/api/skill')
@limiter.limit("100 per hour")
def skill_endpoint():
    # Handle request
    pass
```

### 4. Error Handling
```python
@app.errorhandler(Exception)
def handle_error(error):
    return jsonify({
        'error': 'Internal server error',
        'message': str(error) if app.debug else 'An error occurred'
    }), 500
```

## Testing Your Extension

### 1. Local Testing
```bash
# Start your server locally
python app.py

# Use curl to test
curl -X POST http://localhost:5000/weather \
  -H "Content-Type: application/json" \
  -d '{"city": "London", "units": "metric"}'
```

### 2. Integration Testing
```python
import unittest
import json

class TestWeatherSkillset(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_weather_success(self):
        response = self.app.post('/weather',
            data=json.dumps({'city': 'London', 'units': 'metric'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('temperature', data)

    def test_get_weather_invalid_city(self):
        response = self.app.post('/weather',
            data=json.dumps({'city': 'InvalidCity123'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 404)
```

### 3. End-to-End Testing
Test directly in Copilot Chat:
```
@your-extension Test query
```

## Publishing Your Extension

### Steps:
1. **Package your extension**
   - Create manifest file
   - Document API endpoints
   - Prepare examples

2. **Deploy to production**
   - Choose hosting platform
   - Set up monitoring
   - Configure logging

3. **Register with GitHub**
   - Submit to GitHub Marketplace
   - Provide OAuth app details
   - Set up webhooks

4. **Promote your extension**
   - Write documentation
   - Create demo videos
   - Share in community

## Example Projects

### 1. Slack Integration
Query Slack channels and messages directly from Copilot Chat.

### 2. Jira Ticket Manager
Create, update, and query Jira tickets without leaving VS Code.

### 3. Documentation Search
Search internal wikis and documentation.

### 4. Code Metrics Dashboard
Get real-time metrics about your codebase.

### 5. CI/CD Status
Check build and deployment status.

## Best Practices

1. **Keep skillsets focused** - One skillset = one domain
2. **Use agents for complexity** - Multi-step workflows need agents
3. **Handle errors gracefully** - Always return meaningful error messages
4. **Document thoroughly** - Clear descriptions help Copilot use your extension
5. **Test extensively** - Edge cases matter
6. **Monitor usage** - Track how your extension is used
7. **Version your API** - Plan for backwards compatibility

## Troubleshooting

### Extension not responding?
- Check server is running
- Verify endpoint URLs
- Check authentication

### Copilot not calling your extension?
- Improve skill descriptions
- Make function parameters clearer
- Test with more specific prompts

### Slow response times?
- Add caching
- Optimize database queries
- Use async operations

## Key Takeaways

1. **Skillsets are great for simple, focused tasks**
2. **Agents provide full control for complex scenarios**
3. **Security is critical** - validate all inputs
4. **Good documentation helps Copilot use your extension**
5. **Testing is essential** - test locally before deploying

## Next Steps

- Explore **Prompt Files** (Module 09) to create reusable prompts for your extensions
- Try **Vision for Copilot** (Module 10) to add image processing to extensions

## Resources

- [GitHub Copilot Extensions Documentation](https://docs.github.com/en/copilot/building-copilot-extensions)
- [Skillsets API Reference](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-skillset-for-your-copilot-extension)
- [Agent Development Guide](https://docs.github.com/en/copilot/building-copilot-extensions/building-a-copilot-agent-for-your-copilot-extension)
- [Example Extensions Repository](https://github.com/github/copilot-extensions-examples)
