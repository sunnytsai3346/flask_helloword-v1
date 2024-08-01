from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/hello', methods=['GET'])
def hello():
    return jsonify(message='Hello, API!')

@app.route('/data', methods=['POST'])
def get_data():
    data = request.get_json()
    return jsonify(received=data)



if __name__ == '__main__':
    app.run(debug=True)