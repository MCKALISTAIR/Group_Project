# -*- coding: utf-8 -*-
from flask import Flask, flash, session, render_template, url_for, request, session, redirect, abort, json
from werkzeug.utils import secure_filename
import os
# from flask.ext.uploads import UploadSet, configure_uploads, IMAGES
#from flask_pymongo import PyMongo
# import bcrypt

UPLOAD_FOLDER = 'static/testimage'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

app.secret_key = 'qGseyftsYb9rdYIIfz2cXjhJT9ZJwIxI8Pr0YvUd'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def storyTime(form, filename):
    storyTime= {}
    storyTime["Title"] = form["Title"]
    storyTime["ParaOne"] = form["StoryPara"]
    storyTime["ParaTwo"] = form["StoryParaTwo"]
    storyTime["ParaThree"] = form["StoryParaThree"]
    storyTime["ParaFour"] = form["StoryParaFour"]
    storyTime["Quote"] = form["Quote"]
    storyTime["filename"] = form["filename"]
    return storyTime

with open('newstories.json') as in_file:
    data = json.load(in_file)
    in_file.close()

@app.route("/", methods=['POST','GET'])
def main():
    return render_template('main.html', data=data)

@app.route("/textupload", methods=['GET','POST'])
def text():
    if request.method == "POST" and "filename" in request.files:
        file = request.files['filename']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    if request.method == "POST" and "Title" in request.form:
        data[request.form["Title"]] = storyTime(request.form, filename)
        with open('newstories.json', 'w') as outfile:
            json.dump(data, outfile)
        flash("Your Story Has Been Posted!")
        return render_template("main.html", data=data, filename=filename)
    return render_template("textupload.html", data=data)


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

@app.route("/<storyTime>/", methods=['POST','GET'])
def story(storyTime):
    return render_template('storytemp.html', data=data, storyTime=storyTime)

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

@app.errorhandler(400)
def page_not_found(error4):
    return render_template('403.html'), 400

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
