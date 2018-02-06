# -*- coding: utf-8 -*-
from flask import Flask, render_template, url_for, request, session, redirect, abort

app = Flask(__name__)

@app.route("/", methods=['POST','GET'])
def main():
    return render_template('main.html')

@app.route("/uploadchoice", methods=['POST','GET'])
def uploadchoice():
    return render_template('uploadchoice.html')

@app.route("/textupload", methods=['POST','GET'])
def text():
    return render_template('textupload.html')

@app.route("/videoupload", methods=['POST','GET'])
def video():
    return render_template('videoupload.html')

@app.route("/uploadinstructions", methods=['POST','GET'])
def uploadinstructions():
    return render_template('uploadinstructions.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)















































