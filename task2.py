import os
from flask import Flask, request, redirect,render_template, url_for, flash,jsonify,abort
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/index', methods=['GET'])
def index():
    return 'Welcome'

@app.route('/upload')
def upload_file():
   return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def uploaded_file():
   if request.method == 'POST':
      file_name = request.files["file_name"]
      return file_name.read() 

if __name__ == '__main__':
   app.run(debug = True)
    