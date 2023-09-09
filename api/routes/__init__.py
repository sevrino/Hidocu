from flask import Flask
from . import main

app = Flask(__name__)

app.register_blueprint(main.bp)

if __name__ == '__main__':
    app.run()