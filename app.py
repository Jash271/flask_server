from flask import Flask
from flask import request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
upload_folder = 'tokens'
app.config['UPLOAD_FOLDER'] = upload_folder

@app.route("/")
def hello_world():
    return "<p>Hello, World Jash!</p>"

@app.route("/accept_file",methods = ['POST','GET'])
def accept_file():
    print(request.files)
    file = request.files['file']
    #Save File
    #filename = 'Jash'+ "."+ file.filename.split(".")[-1]
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return {
        "ok":1
    }


if __name__ == "_main_":
  app.run()