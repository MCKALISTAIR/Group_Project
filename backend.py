# -*- coding: utf-8 -*-
import json
from flask import Flask, flash, session, render_template, url_for, request, session, redirect, abort
#from flask_pymongo import PyMongo
# import bcrypt
app = Flask(__name__)
app.secret_key = 'qGseyftsYb9rdYIIfz2cXjhJT9ZJwIxI8Pr0YvUd'

@app.route("/", methods=['POST','GET'])
def main():
    flash("Hello, I'm a flash!")
    return render_template('main.html')

@app.route("/textupload", methods=['POST','GET'])
def text():
    try:
        if request.method == "POST":
            file = 'stories.json'
            '''stories['para1'] = request.form['StoryPara']
            stories['para2'] = request.form['StoryParaTwo']
            stories['para3'] = request.form['StoryParaThree']
            stories['para4'] = request.form['StoryParaFour']
            stories['quote'] = request.form['Quote']

            with open(file, 'a') as f:
                json.dump(stories, f)'''
            with open(file, 'r') as f:
                data = json.load(f)
    except Exception as e:
        print(e)
    return render_template('textupload.html')

@app.route("/admin", methods=['POST','GET'])
def admin():
    if session.get('status', None) != "admin":
        abort(403)
    else:
        return render_template('admin.html')

@app.route("/analyticstestpage", methods=['POST','GET'])
def analyticstestpage():
    if session.get('status', None) != "admin":
        abort(403)
    else:
        return render_template('analyticstestpage.html')

@app.route("/uploadinstructions", methods=['POST','GET'])
def uploadinstructions():
    if session.get('status', None) != "admin":
        abort(403)
    else:
        return render_template('uploadinstructions.html')

@app.route("/morestories", methods=['POST','GET'])
def morestories():
    return render_template('morestories.html')

@app.route("/carouselchange", methods=['POST','GET'])
def carouselchange():
    if session.get('status', None) != "admin":
        abort(403)
    else:
        return render_template('carouselchange.html')

@app.route("/videoinstructions", methods=['POST','GET'])
def videoinstructions():
    if session.get('status', None) != "admin":
        abort(403)
    else:
        return render_template('videoinstructions.html')

@app.route("/story", methods=['POST','GET'])
def story():
    return render_template('storytemp.html')


@app.route('/logout')
def logout():
    session['user'] = ""
    session['status'] = ""
    flash('You have been logged out')
    return redirect(url_for('main'))

@app.route("/login", methods=['POST','GET'])
def login():
    # Check that the user supplied details in the POST
    if request.method == 'POST':
        if request.form['passwd'] == "":
            flash('You must enter a password')
            return render_template('main.html')
        else:
            #this has to change when the database gets done
            if request.form['passwd'] == "password":
                session['user'] = "Admin"
                session['status'] = "admin"

                return redirect(url_for('admin'))

            else:
                flash('Wrong password fool')
                return redirect(url_for('main'))
    else:
        return render_template('admin.html')


@app.errorhandler(403)
def page_not_found(error4):
    return render_template('403.html'), 403

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

'''def readFile(file, title):
    try:
        with open(file, 'r') as filepath:
            print('jjgjg')
            data = json.load(filepath)
            for r in data:
                if r['title'] == title:
                    print(r['title'])
                    print('loool')
    except Exception as e:
        return render_template('admin.html')'''
