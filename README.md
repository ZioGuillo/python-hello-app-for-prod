# Python Hello App for Production
This is a simple Flask app that can be used as a template for a production-ready Python web application. It uses the Gunicorn WSGI server to serve the Flask app, which allows for better performance and scalability compared to the Flask development server.

## Requirements
- Python 3.6 or higher
- Flask 2.0 or higher
- Gunicorn 20.1.0 or higher

## Usage
Clone this repository:
```
https://github.com/ZioGuillo/python-hello-app-for-prod.git
cd python-hello-app-for-prod'
```
## Install the dependencies:
```
pip install -r requirements.txt
```
## Start the app using Gunicorn:
```
gunicorn wsgi:app
```
Open your web browser and go to http://localhost:8000. You should see a "Hello, World!" message.

### Customization
To customize the app, you can modify the app.py file to add additional routes and functionality. You can also modify the HTML templates in the templates directory to change the look and feel of the app.

### Deployment
To deploy the app to a production server, you can use a process manager like systemd or supervisor to manage the Gunicorn process. You should also configure Gunicorn to use multiple workers and bind to a UNIX socket or a port other than 8000 for better performance and security.

### Conclusion
Using this app as a starting point, you can build more complex Python web applications with confidence, knowing that you are building on a stable and well-tested foundation. Happy coding!
