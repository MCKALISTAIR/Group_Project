# -*- coding: utf-8 -*-
from flask import Flask, render_template, url_for, request, session, redirect, abort
# from flask_pymongo import PyMongo
# import bcrypt

app = Flask(__name__)

#Mongo DB
# app.config['MONGO_DBNAME'] = 'group_project_login'
# app.config['MONGO_URI'] = 'mongodb://40205331:rangers17@ds125198.mlab.com:25198/group_project_login'
# mongo = PyMongo(app)

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

@app.route("/analyticstestpage", methods=['POST','GET'])
def analyticstestpage():
    return render_template('analyticstestpage.html')

@app.route("/uploadinstructions", methods=['POST','GET'])
def uploadinstructions():
    return render_template('uploadinstructions.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

@app.route("/socpage", methods=['POST','GET'])
def socpage():
    return render_template('socpage.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
