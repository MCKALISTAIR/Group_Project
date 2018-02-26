# -*- coding: utf-8 -*-
import json
from flask import Flask, render_template, url_for, request, session, redirect, abort
#from flask_pymongo import PyMongo
# import bcrypt

app = Flask(__name__)

#Mongo DB
# app.config['MONGO_DBNAME'] = 'group_project_login'
# app.config['MONGO_URI'] = 'mongodb://40205331:rangers17@ds125198.mlab.com:25198/group_project_login'
# mongo = PyMongo(app)

@app.route("/", methods=['POST','GET'])
def main():
    try:        
        if request.method == "POST":
            text = request.form['password']
            if text == "password":
                return redirect(url_for('admin'))
            else:
                return render_template("main.html")
    except Exception as e:
        return redirect(url_for('story'))
    return render_template('main.html')

@app.route("/textupload", methods=['POST','GET'])
def text():
    try:
        if request.method == "POST":
            file = 'stories.json'
            stories = {}
            stories['title'] = request.form['title']
            stories['para1'] = request.form['StoryPara']
            stories['para2'] = request.form['StoryParaTwo']
            stories['para3'] = request.form['StoryParaThree']
            stories['para4'] = request.form['StoryParaFour']
            stories['quote'] = request.form['Quote']
            with open(file, 'a') as f:
                json.dump(stories, f)
    except Exception as e:
        return render_template('admin.html')
    return render_template('textupload.html')

@app.route("/admin", methods=['POST','GET'])
def admin():
    return render_template('admin.html')

@app.route("/analyticstestpage", methods=['POST','GET'])
def analyticstestpage():
    return render_template('analyticstestpage.html')

@app.route("/uploadinstructions", methods=['POST','GET'])
def uploadinstructions():
    return render_template('uploadinstructions.html')

@app.route("/morestories", methods=['POST','GET'])
def morestories():
    return render_template('morestories.html')

@app.route("/story", methods=['POST','GET'])
def story():
    return render_template('storytemp.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
