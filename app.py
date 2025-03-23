from flask import Flask, render_template, request, redirect, url_for, jsonify
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Generate a secure random key

# Configure for production
app.config['ENV'] = 'production'
app.config['DEBUG'] = True  # Enable debugging temporarily
# Set the application root path
app.config['APPLICATION_ROOT'] = '/apps/BasicPython'

# Define URL prefix
URL_PREFIX = '/apps/BasicPython'

# Store todos in memory (will be reset when server restarts)
todos = []

def is_ajax():
    return request.headers.get('X-Requested-With') == 'XMLHttpRequest'

# Root route redirects to the app
@app.route('/')
def root():
    return redirect('/apps/BasicPython/')

# Main application routes
@app.route('/apps/BasicPython/')
@app.route('/apps/BasicPython')
def index():
    app.logger.info(f"Accessing index page. Request path: {request.path}")
    return render_template('index.html', todos=todos)

@app.route('/apps/BasicPython/add', methods=['POST'])
def add():
    try:
        app.logger.info(f"Add request received. Method: {request.method}")
        todo = request.form.get('todo')
        if todo:
            todos.append(todo)
            if is_ajax():
                return jsonify({'status': 'success', 'message': 'Task added successfully'})
        return redirect('/apps/BasicPython/')
    except Exception as e:
        app.logger.error(f"Error in add: {str(e)}")
        if is_ajax():
            return jsonify({'status': 'error', 'message': str(e)}), 500
        return redirect('/apps/BasicPython/')

@app.route('/apps/BasicPython/delete/<int:index>')
def delete(index):
    try:
        app.logger.info(f"Delete request received for index: {index}")
        if 0 <= index < len(todos):
            todos.pop(index)
            if is_ajax():
                return jsonify({'status': 'success', 'message': 'Task deleted successfully'})
        return redirect('/apps/BasicPython/')
    except Exception as e:
        app.logger.error(f"Error in delete: {str(e)}")
        if is_ajax():
            return jsonify({'status': 'error', 'message': str(e)}), 500
        return redirect('/apps/BasicPython/')

# Error handling
@app.errorhandler(404)
def not_found_error(error):
    app.logger.error(f"404 error: {request.url}")
    if is_ajax():
        return jsonify({'status': 'error', 'message': 'Not found'}), 404
    return redirect('/apps/BasicPython/')

@app.errorhandler(500)
def internal_error(error):
    app.logger.error(f"500 error: {str(error)}")
    if is_ajax():
        return jsonify({'status': 'error', 'message': 'Internal server error'}), 500
    return redirect('/apps/BasicPython/')

if __name__ == '__main__':
    app.run() 