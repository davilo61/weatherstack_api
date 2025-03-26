from flask import Flask, request, render_template, jsonify
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Get API key from environment variables
API_KEY = os.getenv('WEATHERSTACK_API_KEY')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    try:
        zipcode = request.form.get('zipcode')
        if not zipcode:
            return jsonify({'error': 'Please provide a valid zipcode.'}), 400
        
        # Weatherstack API URL with imperial units (Fahrenheit)
        url = f'http://api.weatherstack.com/current?access_key={API_KEY}&query={zipcode}&units=f'
        
        # Make the API request
        response = requests.get(url, timeout=10)  # Added timeout
        response.raise_for_status()  # Raise exception for HTTP errors
        data = response.json()
        
        if 'error' in data:
            return jsonify({'error': data['error']['info']}), 400
        
        # Extract the necessary weather data
        location = data['location']['name']
        region = data['location'].get('region', '')
        country = data['location'].get('country', '')
        temperature = data['current']['temperature']
        weather_desc = data['current']['weather_descriptions'][0] if data['current']['weather_descriptions'] else 'No description available'
        
        # Add more weather details
        feels_like = data['current'].get('feelslike', '')
        humidity = data['current'].get('humidity', '')
        wind_speed = data['current'].get('wind_speed', '')
        
        # Return enhanced weather data
        return jsonify({
            'location': f"{location}, {region}, {country}".strip(', '),
            'temperature': temperature,
            'description': weather_desc,
            'feels_like': feels_like,
            'humidity': humidity,
            'wind_speed': wind_speed
        })
    
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'API request failed: {str(e)}'}), 500
    except (KeyError, ValueError, TypeError) as e:
        return jsonify({'error': f'Error processing weather data: {str(e)}'}), 500
    except Exception as e:
        return jsonify({'error': f'Unexpected error: {str(e)}'}), 500

if __name__ == '__main__':
    # Check if API key is available
    if not API_KEY:
        print("Warning: WEATHERSTACK_API_KEY not found in environment variables.")
        print("Please create a .env file with your API key.")
    
    # Only enable debug in development
    debug_mode = os.getenv('FLASK_ENV') == 'development'
    app.run(debug=debug_mode)