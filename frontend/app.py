from flask import Flask, render_template_string
import requests

app = Flask(__name__)

BACKEND_URL = 'http://backend:5000/info'

@app.route('/')
def index():
    try:
        resp = requests.get(BACKEND_URL)
        data = resp.json()
        message = data.get('message', 'No message')
        value = data.get('data', 'No data')
    except Exception as e:
        message = f'Error: {e}'
        value = ''
    return render_template_string('<h1>Hello world!</h1><p>{{message}}</p><p>Data: {{value}}</p>', message=message, value=value)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
