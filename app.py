from flask import Flask, flash, redirect, render_template, request, session, abort
from werkzeug import secure_filename

app = Flask(__name__)

@app.route("/")
def index():
    name="TEST NAME"
    return render_template('basic.html',name=name)

@app.route('/upload', methods = ['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return "File saved successfully"
 

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)