#!/bin/bash

# Set the paths
VENV_PATH="/home/fooladra/virtualenv/public_html/apps/BasicPython/3.9"
APP_PATH="/home/fooladra/public_html/apps/BasicPython"

# Navigate to app directory
cd $APP_PATH

# Activate virtual environment
source $VENV_PATH/bin/activate

# Upgrade pip
python -m pip install --upgrade pip

# Install requirements with detailed output
python -m pip install -v --no-cache-dir -r requirements.txt

# Verify installation
python check_dependencies.py

# Print virtual environment information
echo "Virtual Environment Python: $(which python)"
echo "Installed packages:"
pip list 