
from constants import *
from main import app
from flask import request, Response
from werkzeug.utils import secure_filename
import json
import os
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging


@app.route('/check', methods=["GET", "POST"])
def just_to_check():
    print("APP IS TAKING REQUESTS !! CONGRATSS ")
    response = Response(
        status=200,
        response=json.dumps('SUCCESSFUL'),
        mimetype='application/json'
    )
    return render_template('home.html')
