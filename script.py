###############################################################################################################
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


###################################################################################################################

#initialize flask web app 
app = Flask(__name__)
app.config['SECRET_KEY']='1234'



# telling us about the creator
#in this page we need to log in to the system 

@app.route("/")
def Home():
   return render_template('login_page.html')


###################################################################################################################
#this function will do for register action

@app.route('/register',methods=['POST','GET'])
def register():
   if request.method=='POST':
      email=request.form['email']
      psw=request.form['password']
      
      
      email_match=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
      pattern=re.compile(email_match)
      if pattern.match(email):
         
         #connection with sqlite3 database for query to data 
         connect=sqlite3.connect(r"C:/Users/ghosh/AppData/Local/Programs/Python/Python39/Flask_project/password.db")
         cursor=connect.cursor()
         
         #query-1 , if the user is already in the data base then we will return to the login page
         query="select email from password_table"
         cursor.execute(query)
         x=cursor.fetchall()
         
         # this function only check if the email address is available  in database , if it is 
         # available in the database then it will redirect into the login page 
         # if is not available in database then it will insert into database with password 
         
         if email in [y[0] for y in x]:
               return render_template('login_page.html')
         else:
               query2="insert into password_table values(?,?)"
               cursor.execute(query2,(email,psw))
               connect.commit()
               connect.close()
               return render_template('new.html',data='You are successful into this system')
         
         

      else:
         return render_template('register.html')

##################################################################################################################

#If login is successful then This function is called here 

@app.route('/success',methods=["POST",'GET'])
def success():
   if request.method=="POST":
      email=request.form['email']
      psw=request.form['password']
      
      
      email_match=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
      pattern=re.compile(email_match)
      if pattern.match(email):
         
          #connection with sqlite3 database for query to data 
         connect=sqlite3.connect(r"C:/Users/ghosh/AppData/Local/Programs/Python/Python39/Flask_project/password.db")
         cursor=connect.cursor()
         
         #query-1 , if the user is already in the data base then we will return to the login page
         query="select email from password_table"
         cursor.execute(query)
         x=cursor.fetchall()
         
         # this function only check if the email address is available  in database , if it is 
         # available in the database then it will redirect into the login page 
         # if is not available in database then it will insert into database with password 
         
         if email in [y[0] for y in x]:
            #in this function we will verify if the email is in the email list 
            # if it is in the list then retrieve the password and verify with input's ones 
            # it is same then we will let them go to the user_page
            #other wise refresh login page 
            
            query="select password from password_table where email=?"
            cursor.execute(query,(email,))
            x=cursor.fetchall()
            
            # return render_template('new.html',data=x)
            
            if x[0][0] == psw:
               return render_template('login_success.html',data='You are successfully accessed your user ground')
            else:
               return render_template('login_page.html')
              
         else:
            #if email is not into the email list then we will redirect him/her to 
            #the register page  for user creation .
            
            return render_template('register.html')
         
      else:
         return render_template('login_error.html',data='your input for email is not valid')
      
      
################################################################################################################
      
      
      
              
         
         
     
if __name__=="__main__":
   app.run(debug=True)






    
        


