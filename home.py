from flask import Flask

# Create a Flask app
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def home():
    return 'Hello, Flask!'

# Define a route for a custom page
@app.route('/about')
def about():
    return 'This is the about page.'

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
