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




#importing essential modules for other workds
import re












#initialize flask web app 
app = Flask(__name__)
app.config['SECRET_KEY']='1234'



# telling us about the creator
#in this page we need to log in to the system 
@app.route("/")
def login():
   flash('You are successful')
   return render_template('login_page.html')


@app.route('/success',methods=["POST",'GET'])
def success():
   email_match=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
 
   if request.method=="POST":
      fname=request.form['fname']
      lname=request.form['lname']
      email=request.form['email']
      
      #This loop validate if this is valid fname, lname and email address also 
      #other wise it will rise error message for this 
      
   
      if fname !=None and lname !=None and (re.fullmatch(email_match, email)):
         return render_template('login_success.html',user=(fname,lname,email))
      else:
         if not re.fullmatch(email_match, email):
            msg='Email not valid'
            return render_template('login_error.html',msg=msg)
         else:
            msg='Something else is wrong'
            return render_template('login_error.html',msg=msg)
 


if __name__=="__main__":
   app.run(debug=True)
