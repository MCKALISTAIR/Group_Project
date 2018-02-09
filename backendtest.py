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

@app.route("/adminlanding", methods=['POST','GET'])
def admin():
    return render_template('admin.html')

@app.route("/storypage", methods=['POST','GET'])
def video():
    return render_template('videoupload.html')



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)



































































