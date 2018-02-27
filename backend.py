# -*- coding: utf-8 -*-
import json
from flask import Flask, flash, session, render_template, url_for, request, session, redirect, abort
#from flask_pymongo import PyMongo
# import bcrypt
app = Flask(__name__)
app.secret_key = 'qGseyftsYb9rdYIIfz2cXjhJT9ZJwIxI8Pr0YvUd'

@app.route("/", methods=['POST','GET'])
def main():
    return render_template('main.html')

@app.route("/textupload", methods=['POST','GET'])
def text():
    """
    try:
        if request.method == "POST":
            openFile = open("stories.json","w")
            story = {}
            story['title'] = 'title'
            story['para1'] = 'paragraph_one'
            serialisedData = json.dumps(stories)
            openFile.write(serialisedData)
            openFile.close()
    except Exception as e:
        return render_template('admin.html')
        """
    return render_template('textupload.html')

@app.route("/admin", methods=['POST','GET'])
def admin():
    if session.get('status', None) != "admin":
        return redirect(url_for('main'))
    else:
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

@app.route("/carouselchange", methods=['POST','GET'])
def carouselchange():
    return render_template('carouselchange.html')

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
            return render_template('admin.html')
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
    return render_template('403.html'), 404

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

def putData(data):
    try:

           # ADD VALIDATION HERE
        openFile.write(serialisedData)          # IF INVALID DO NOT PROCEED WITH WRITE!
        openFile.close()

        return
    except ValueError:
        print("Coundn't write file data: ", sys.exc_info()[0])
        raise

    except:
        print("Unexpected error when writing file: ", sys.exc_info()[0])
        raise

#paragraph_one = request.form['ParaOne']
#paragraph_two = request.form['ParaTwo']
#paragraph_three = request.form['ParaThree']
#paragraph_four = request.form['ParaFour']
#quote = request.form['quote']
#story['para2'] = paragraph_two
#story['para3'] = paragraph_three
#story['para4'] = paragraph_four
