# -*- coding: utf-8 -*-
import json
from flask import Flask, flash, session, render_template, url_for, request, session, redirect, abort
import os
# from flask.ext.uploads import UploadSet, configure_uploads, IMAGES
# from flask_mail import Mail, Message
#from flask_pymongo import PyMongo
# import bcrypt
app = Flask(__name__)
# photos = UploadSet('photos', IMAGES)

UPLOAD_FOLDER = 'static/testimage'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

# app.config['UPLOADED_PHOTOS_DEST'] = 'static/img'
# configure_uploads(app, photos)
app.secret_key = 'qGseyftsYb9rdYIIfz2cXjhJT9ZJwIxI8Pr0YvUd'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def storyTime(form, zipFolder):
    storyTime= {}
    storyTime["Title"] = form["Title"]
    storyTime["ParaOne"] = form["StoryPara"]
    storyTime["ParaTwo"] = form["StoryParaTwo"]
    storyTime["ParaThree"] = form["StoryParaThree"]
    storyTime["ParaFour"] = form["StoryParaFour"]
    storyTime["Quote"] = form["Quote"]
    storyTime["schoolSelect"] = form["schoolSelect"]
    storyTime["zipFolder"] = zipFolder
    return storyTime

with open('newstories.json') as in_file:
    data = json.load(in_file)
    in_file.close()

# app.config.update(
# 	#EMAIL SETTINGS
# 	MAIL_SERVER='smtp.gmail.com',
# 	MAIL_PORT=465,
# 	MAIL_USE_SSL=True,
# 	MAIL_USERNAME = 'napierplacementnoreply@gmail.com',
# 	MAIL_PASSWORD = 'Placement5000'
# 	)
# mail = Mail(app)
#app.config['MAIL_DEFAULT_SENDER'] = ‘allymckay5@gmail.com’
@app.route("/", methods=['POST','GET'])
def main():
    return render_template('main.html', data=data)
# @app.route("/test")
# def phptest():
#     return render_template('test.html')
#
# @app.route('/Send/', methods=['POST','GET'])
# def Send():
# 		try:
# 			#emaiil = request.form['email'] + request.form['email']
# 			msg = Message("Placement site access request",
# 			  sender="placmentnoreply@gmail.com",
# 			  recipients=["allymckay5@gmail.com"])
# 			msg.body = "Hello! This is an automated message to say that " + request.form['email'] + " has requested access to PLACEHOLDER. Please do not reply to this message, the mailbox is not monitored."
# 			mail.send(msg)
# 			flash('Request sent!')
# 			return redirect(url_for('main'))
# 		except Exception, e:
# 			return(str(e))

@app.route("/textupload", methods=['POST','GET'])
def text():
    if request.method == "POST" and "zipFolder" in request.files:
        f = request.files.getlist('zipFolder')
        for zipFile in f:
            filename = zipFile.filename.split('/')[0]
            zipFile.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    if request.method == "POST" and "Title" in request.form:
        data[request.form["Title"]] = storyTime(request.form, filename)
        with open('newstories.json', 'w') as outfile:
            json.dump(data, outfile)
        flash("Your Story Has Been Posted!")
        return render_template("main.html", data=data, zipFile=zipFile)
    return render_template("textupload.html", data=data)

def upload():
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        return filename
    return render_template('upload.html')

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

@app.route("/analyticstestpage2", methods=['POST','GET'])
def analyticstestpage2():
    if session.get('status', None) != "admin":
        abort(403)
    else:
        return render_template('analyticstestpage2.html')

@app.route("/analyticstestpage3", methods=['POST','GET'])
def analyticstestpage3():
    if session.get('status', None) != "admin":
        abort(403)
    else:
        return render_template('analyticstestpage3.html')

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

@app.route("/<storyTime>/", methods=['POST','GET'])
def story(storyTime):
    return render_template('storytemp.html', data=data, storyTime=storyTime)

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
