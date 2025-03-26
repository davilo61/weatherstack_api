# Weather App

A simple, responsive web application that provides current weather information based on ZIP code or city name using the Weatherstack API.

![Weather App Screenshot](https://via.placeholder.com/800x400?text=Weather+App+Screenshot)

## Features

- Get real-time weather data using the Weatherstack API
- Search by ZIP code or city name
- Responsive design that works on desktop and mobile devices
- Display of detailed weather information:
  - Current temperature
  - "Feels like" temperature
  - Weather description
  - Humidity levels
  - Wind speed
- Clean, modern UI with intuitive user experience
- Error handling for API failures and invalid inputs

## Project Structure

```
weather-app/
├── weatherstack.py       # Main Flask application
├── .env                  # Environment variables (API keys)
├── templates/
│   ├── index.html        # Main search page
│   └── weather.html      # Weather details template
├── static/               # CSS, JS, and images (auto-created by Flask)
├── .gitignore            # Git ignore file
└── README.md             # Project documentation
```

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **APIs**: Weatherstack API
- **Dependencies**: 
  - Flask
  - Requests
  - python-dotenv

## Setup and Installation

### Prerequisites

- Python 3.6+
- Weatherstack API key (get one at [weatherstack.com](https://weatherstack.com/))

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/weather-app.git
   cd weather-app
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`

4. Install required packages:
   ```bash
   pip install flask requests python-dotenv
   ```

5. Create a `.env` file in the project root and add your Weatherstack API key:
   ```
   WEATHERSTACK_API_KEY=your_api_key_here
   FLASK_ENV=development
   ```

6. Run the application:
   ```bash
   python weatherstack.py
   ```

7. Open your web browser and navigate to `http://localhost:5000`

## Usage

1. Enter a ZIP code or city name in the search field
2. Click "Get Weather" or press Enter
3. View the current weather conditions for your requested location

## Security Considerations

- API keys are stored in environment variables instead of being hardcoded
- Input validation is implemented to prevent injection attacks
- Error handling prevents exposure of sensitive information

## Error Handling

The application handles several types of errors:
- Invalid ZIP codes or location names
- API request failures
- Network timeouts
- Malformed API responses

## Future Improvements

- Add 5-day forecast feature
- Implement geolocation to automatically detect user's location
- Add unit conversion (Fahrenheit/Celsius)
- Implement caching to reduce API calls
- Add weather alerts and notifications
- Include weather maps and radar
- Add dark mode toggle

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- [Weatherstack API](https://weatherstack.com/) for providing weather data
- [Font Awesome](https://fontawesome.com/) for the icons
- [Flask](https://flask.palletsprojects.com/) for the web framework
