from flask import render_template, Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import base64 as b
import sqlite3
from flask_restx import Api, Resource
from db import *

con = sqlite3.connect('db/main.db')
bp = Blueprint('routes', __name__, template_folder='../templates', static_folder='../public')

@bp.route('/')
def main():
    return render_template('index.html')

@bp.route('/upload', methods=['POST'])
def upload():
    param = request.get_json()
    inputDB(param)
    return jsonify({"status": "ok"})