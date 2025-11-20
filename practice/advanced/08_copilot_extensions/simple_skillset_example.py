"""
Simple Copilot Skillset Example
A basic weather lookup skillset to demonstrate the concept
"""

from flask import Flask, request, jsonify
import random  # For demo purposes - replace with real API call

app = Flask(__name__)

@app.route('/weather', methods=['POST'])
def get_weather():
    """
    Endpoint for weather lookup skill

    Expected request format:
    {
        "city": "London",
        "units": "metric"  # optional, defaults to metric
    }
    """
    data = request.json

    # Validate input
    if not data or 'city' not in data:
        return jsonify({
            'error': 'Missing required field: city'
        }), 400

    city = data.get('city')
    units = data.get('units', 'metric')

    # Validate units
    if units not in ['metric', 'imperial']:
        return jsonify({
            'error': 'Invalid units. Must be "metric" or "imperial"'
        }), 400

    # In a real implementation, call actual weather API
    # For demo, return mock data
    weather_data = generate_mock_weather(city, units)

    return jsonify(weather_data)


def generate_mock_weather(city, units):
    """
    Generate mock weather data for demonstration
    Replace this with actual API call in production
    """
    # Mock temperature generation
    temp = random.randint(15, 30) if units == 'metric' else random.randint(60, 85)
    unit_symbol = '°C' if units == 'metric' else '°F'

    conditions = ['Sunny', 'Cloudy', 'Partly Cloudy', 'Rainy', 'Clear']

    return {
        'city': city,
        'temperature': f"{temp}{unit_symbol}",
        'condition': random.choice(conditions),
        'humidity': f"{random.randint(30, 80)}%",
        'wind_speed': f"{random.randint(5, 25)} km/h",
        'description': f"Current weather in {city}"
    }


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'weather-skillset'
    })


if __name__ == '__main__':
    print("Starting Weather Skillset server...")
    print("Endpoint: http://localhost:5000/weather")
    print("Health check: http://localhost:5000/health")
    app.run(host='0.0.0.0', port=5000, debug=True)
