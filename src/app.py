from fileinput import filename
from flask import Flask, render_template, request
from helps import do_stuff
from lib.root import Root
import os
from glob import glob

app = Flask(__name__)
app.static_folder = 'static'

UPLOAD_FOLDER = Root.out()
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
  ALLOWED_EXTENSIONS = { 'pdf', 'png', 'jpg', 'jpeg' }
  return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def index():
  pdf_filenames = []
  for filepath in glob(Root.assets("*.pdf")):
    pdf_filenames.append(os.path.basename(filepath))

  return render_template('index.jinja.html', pdf_filenames=pdf_filenames)

@app.route("/<string:pdf_name>")
def show(pdf_name):
  return render_template('show.jinja.html', pdf_name=pdf_name)

  # if request.method == 'POST':
  #   file = request.files['input_file']

  #   if file and allowed_file(file.filename):
  #     file.save(Root.join(app.config['UPLOAD_FOLDER'], 'sample.jpg'))

  # do_stuff()



