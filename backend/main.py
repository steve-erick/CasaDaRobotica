from flask import Flask
app = Flask(__name__)
from routes import *
from flask_hashing import Hashing
app.config['DEBUG'] = True   


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
hashing = Hashing(app)
