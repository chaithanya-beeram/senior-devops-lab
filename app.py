from flask import Flask
import os
app = Flask(__name__)
@app.route('/')
def home():
    return f"<h1>Build #1: Success</h1><p>Running on: {os.getenv('HOSTNAME')}</p>"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
