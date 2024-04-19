from flask import Flask, render_template , jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', message='Hello, Flask!')

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/api/data')
def get_data():
    data = {'message': 'Data fetched from server!'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
