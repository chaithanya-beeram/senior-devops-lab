from flask import Flask
import os
from datetime import datetime
app = Flask(__name__)
@app.route('/')
def home():
    # Combine everything into one string
    line1 = f"<h1>Build #1: Success</h1>"
    line2 = f"<h3>This is Chaybeeram running his first devops application</h3>"
    line3 = f"<p>Running on: {os.getenv('HOSTNAME')}</p>"
    line4 = f"<p>Application running at: {datetime.now()}</p>"
    
    return line1 + line2 + line3 + line4
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
