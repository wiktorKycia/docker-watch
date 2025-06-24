from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/info')
def info():
    return jsonify({'message': 'Hello from the backend!', 'data': 42})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
