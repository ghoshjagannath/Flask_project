import sqlite3
import os 

#basic level of module in flask
from flask import Flask,redirect,url_for,render_template,request,abort,flash,session
from flask_session import Session

# for wtf froms to be used
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired


#for file upload related  modules 
from werkzeug.utils import secure_filename
from formsubmit import *


#for security of password it is used
from werkzeug.security import generate_password_hash,check_password_hash

#initialize flask web app 
app = Flask(__name__)
app.config['UPLOAD_FOLDER']=r"C:/Users/ghosh/AppData/Local/Programs/Python/Python39/Flask_project/static/files/"
app.config['SECRET_KEY']='1234'

#####################################
# conn=sqlite3.connect(r'C:/Users/ghosh/AppData/Local/Programs/Python/Python39/Flask_project/password.db')
#creating user and password database in sqlite3 system if password.db is not present in parents folder. 
# command='''CREATE TABLE  if not Exists user_list (name TEXT NOT NULL,pass TEXT NOT NULL)'''

######################################




# telling us about the creator
#in this page we need to log in to the system 
@app.route("/")
def login():
   flash('You are successful')
   return render_template('login_page.html')


@app.route('/success',methods=['GET'])
def success():
   session['name']=request.form.get('username')
   data=session.pop('name')
 
 


if __name__=="__main__":
   app.run(debug=True)
