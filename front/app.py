from flask import Flask, render_template
import logger, requests, os, re
from routes import app

logger.log()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)