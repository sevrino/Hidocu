from flask import render_template, Blueprint, request, jsonify, url_for
from werkzeug.utils import secure_filename
import base64 as b
import sqlite3

bp = Blueprint('routes', __name__, template_folder='../templates', static_folder='../static')

@bp.route('/')
def main():
    return render_template('index.html')