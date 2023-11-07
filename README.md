# Python Hello App for Production

This is a simple Flask app that can be used as a template for a production-ready Python web application. It uses the Gunicorn WSGI server to serve the Flask app, which allows for better performance and scalability compared to the Flask development server.

## Requirements

- Python 3.10 or higher
- Flask 2.3 or higher
- Gunicorn 20.1.0 or higher
- Jinja2 3.1.2 or higher

## Usage

Clone this repository:

```bash
https://github.com/ZioGuillo/python-hello-app-for-prod.git
cd python-hello-app-for-prod'
```

## Install the dependencies

```bash
pip install -r requirements.txt
```

## Start the app using Gunicorn

```bash
gunicorn wsgi:app
```

Open your web browser and go to <http://localhost:5000>. You should see a "Hello, World!" message.

### Customization

To customize the app, you can modify the app.py file to add additional routes and functionality.  
You can also modify the HTML templates in the templates directory to change the look and feel of the app.

For example, a new route /random has been added, which returns six random numbers between 1 and 99. Here's how to use it:

To get six random numbers between 1 and 99, make a GET request to:

```bash
http://localhost:5000/random

```

If you want to simulate a lottery draw, use the /randomball route, which returns five random numbers between 1 and 69 and one random number between 1 and 26.

```bash
http://localhost:5000/randomball
```

## Stocks Information

We have added a new feature to retrieve real-time stock information using the `Alpha Vantage API`.  
To get started, follow these steps:

Sign up for an Alpha Vantage API key on their official website.

Set your API key as an environment variable in your system.  
You can do this by adding the following line to your profile configuration file (e.g., .bashrc, .zshrc, or .profile):

```bash
export ALPHA_VANTAGE_API_KEY=YOUR_API_KEY
```

Be sure to replace `YOUR_API_KEY` with the actual API key you obtained.

Save the changes and reload your shell or run `source ~/.bashrc` (or the respective file) to apply the environment variable.

Now, you can use the */get_stock_price* and */get_stock_data* routes in your Python App for Production to retrieve stock information.  

Here are some examples:

To get the current price of a stock (e.g., AAPL), make a GET request to:

```bash
http://localhost:5000/stocks/get_stock_price?symbol=AAPL
```

To retrieve intraday stock data, use the /get_stock_data route with parameters. For example, to get intraday data for NKE with a 1-minute interval:

```bash
http://localhost:5000/stocks/get_stock_data/TIME_SERIES_INTRADAY?symbol=NKE&interval=1min
```

Feel free to customize the routes and data retrieval according to your requirements.

### Deployment

To deploy the app to a production server, you can use a process manager like systemd or supervisor to manage the Gunicorn process. You should also configure Gunicorn to use multiple workers and bind to a UNIX socket or a port other than 8000 for better performance and security.

To run the app in a Docker container, use the following commands:

```bash
docker build -t hello_app_prod .
```

then

For port 80:

```bash
    docker run -d -p 80:5000 hello_app_prod
```

For port 5000:

```bash
    docker run -d -p 5000:5000 hello_app_prod
```

### Conclusion

Using this app as a starting point, you can build more complex Python web applications with confidence, knowing that you are building on a stable and well-tested foundation. Happy coding!
