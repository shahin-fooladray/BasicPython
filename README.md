# Basic Python Todo App

A simple, interactive todo list web application built with Flask.

## Features
- Add new tasks
- Delete existing tasks
- Clean, modern interface
- Responsive design

## Setup Instructions

1. Install Python 3.x if not already installed
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python app.py
   ```

4. Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

## Deployment

To deploy this application on a web server:

1. Install the requirements on your server
2. Use gunicorn to serve the application:
   ```
   gunicorn app:app
   ```

3. Configure your web server (Apache/Nginx) to proxy requests to gunicorn

## Project Structure
- `app.py` - Main Flask application
- `templates/` - HTML templates
- `static/` - CSS and other static files
- `requirements.txt` - Project dependencies 