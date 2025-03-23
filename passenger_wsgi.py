import os
import sys
import logging
import traceback

# Configure logging
logging.basicConfig(
    filename='passenger_error.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

try:
    # Log the current directory and Python path
    current_dir = os.getcwd()
    logging.info(f"Current directory: {current_dir}")
    logging.info(f"Python path before: {sys.path}")
    logging.info(f"Python executable: {sys.executable}")

    # Add virtual environment site-packages
    VIRTUALENV = "/home/fooladra/virtualenv/public_html/apps/BasicPython/3.9"
    SITE_PACKAGES = os.path.join(VIRTUALENV, "lib/python3.9/site-packages")
    
    if os.path.exists(SITE_PACKAGES):
        if SITE_PACKAGES not in sys.path:
            sys.path.insert(0, SITE_PACKAGES)
            logging.info(f"Added site-packages to path: {SITE_PACKAGES}")
    else:
        logging.warning(f"Site-packages not found at: {SITE_PACKAGES}")
        # List directory contents to help debug
        parent_dir = os.path.dirname(SITE_PACKAGES)
        if os.path.exists(parent_dir):
            logging.info(f"Contents of {parent_dir}: {os.listdir(parent_dir)}")

    # Add the application directory to Python path
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    if APP_ROOT not in sys.path:
        sys.path.insert(0, APP_ROOT)
        logging.info(f"Added app root to path: {APP_ROOT}")

    # List files in APP_ROOT to verify app.py exists
    logging.info(f"Contents of {APP_ROOT}: {os.listdir(APP_ROOT)}")
    logging.info(f"Final Python path: {sys.path}")

    # Import the Flask application
    try:
        from app import app as application
        logging.info("Successfully imported Flask application")
        
        # Log Flask app configuration
        logging.info(f"Flask app config: {application.config}")
        logging.info(f"Flask app URL map: {application.url_map}")
    except ImportError as e:
        logging.error(f"Failed to import Flask application: {str(e)}")
        logging.error(f"Traceback: {traceback.format_exc()}")
        raise

except Exception as e:
    logging.error(f"Error in passenger_wsgi.py: {str(e)}")
    logging.error(f"Traceback: {traceback.format_exc()}")
    raise 