from flask import Flask, render_template, make_response
from flask import redirect, request, jsonify, url_for
import io
import os
import uuid

app = Flask(__name__)
app.debug = True
app._static_folder = os.path.abspath("static/")
 
@app.route("/")
def index():
    title = 'main page'
    return render_template('index.html', title=title)
 
if __name__ == "__main__":
    app.run()