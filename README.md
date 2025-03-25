# Basic Python Todo App

A simple Flask-based Todo application that allows users to add and delete tasks.

## Features

- Add new todo items
- Delete existing todo items
- Clean and responsive UI
- Persistent storage

## Installation

1. Clone the repository:
```bash
git clone https://github.com/shahin-fooladray/BasicPython.git
cd BasicPython
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

## Deployment

### Option 1: Deploy on AWS Elastic Beanstalk

1. Install the AWS CLI and EB CLI:
```bash
pip install awscli awsebcli
```

2. Configure AWS credentials:
```bash
aws configure
```
Enter your AWS Access Key ID, Secret Access Key, and default region.

3. Initialize Elastic Beanstalk:
```bash
eb init
```
- Select your region
- Create new application
- Select Python platform
- Choose to use CodeCommit (optional)
- Choose to set up SSH (recommended)

4. Create and deploy the environment:
```bash
eb create
```

5. Open the application:
```bash
eb open
```

### Option 2: Deploy on Render (Recommended for Free Tier)

1. Create a free account on [Render](https://render.com)
2. Click "New +" and select "Web Service"
3. Connect your GitHub repository
4. Configure the service:
   - Name: `basic-python-todo`
   - Environment: `Python`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
5. Click "Create Web Service"

### Option 3: Deploy on cPanel

This application is configured for deployment on cPanel using Passenger. The deployment process is automated using GitHub Actions.

#### Manual Deployment

1. Upload all files to your cPanel server
2. Set up Python application in cPanel
3. Configure the application to use `passenger_wsgi.py` as the entry point
4. Restart the application

#### Automated Deployment

The application uses GitHub Actions for automated deployment. When you push to the main branch, the application will be automatically deployed to your cPanel server.

## Technologies Used

- Python 3.8+
- Flask
- HTML/CSS
- cPanel/Passenger
- Render (for free hosting)
- AWS Elastic Beanstalk (for production)

## License

This project is licensed under the MIT License - see the LICENSE file for details. 