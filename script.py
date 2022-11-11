###############################################################################################################
import sqlite3
import os 

#basic level of module in flask
from flask import Flask,redirect,url_for,render_template,request,abort,flash,session
from flask_session import Session

#for file upload related  modules 
from werkzeug.utils import secure_filename


#for security of password it is used
from werkzeug.security import generate_password_hash,check_password_hash


#importing essential modules for other workds
import re


#importing PyPdf2 module for pdf manipilation
from PyPDF2 import PdfFileReader,PdfFileReader
from pprint import pprint
   
###################################################################################################################

#initialize flask web app 
app = Flask(__name__)
app.config['SECRET_KEY']='1234'
app.config['UPLOAD_FOLDER']=r"C:\Users\ghosh\AppData\Local\Programs\Python\Python39\Flask_project"
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024

# telling us about the creator
#in this page we need to log in to the system 

@app.route("/")
def Home():
   return render_template('new.html')

@app.route("/log")
def log():
   return render_template('login_page.html')


@app.route('/reg')
def reg():
   return render_template('register.html')




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
         connect=sqlite3.connect(r"C:\\Program Files\\DB Browser for SQLite\\password.db")
         cursor=connect.cursor()
         
         #query-1 , if the user is already in the data base then we will return to the login page
         query="select email from password_table"
         cursor.execute(query)
         x=cursor.fetchall()
      
         
         # this function only check if the email address is available  in database , if it is 
         # available in the database then it will redirect into the login page 
         # if is not available in database then it will insert into database with password 
        
        # if email is in list of password table  
         if email in [y[0] for y in x]:
            connect.close()
            return render_template('login_page.html')
         
         else:
            #if email address is not present then password in 
            #encrypted format is storeed into the database 
            query2="insert into password_table values(?,?)"
            cursor.execute(query2,(email,psw))
            connect.commit()
            connect.close()
            return render_template('new.html',data='You are successful into this system')
         
         

      else:
         #if email address is not in right format then registration form
         # is returned again 
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
         connect=sqlite3.connect(r"C:\\Program Files\\DB Browser for SQLite\\password.db")
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
            z=cursor.fetchall()
            connect.close()
            
            # return render_template('new.html',data=x)
            
            if z[0][0] == generate_password_hash(psw):
               return render_template('login_success.html')
            else:
               return render_template('login_page.html')
              
         else:
            #if email is not into the email list then we will redirect him/her to 
            #the register page  for user creation .
            
            return render_template('register.html')
         
      else:
         return render_template('login_error.html',data='your input for email is not valid')
      
      
################################################################################################################
      
#document data extraction for future use 
      
@app.route('/extraction', methods=['POST','GET'])
def extraction():
   if request.method=='POST':
      file=request.files['doc']
      reader=PdfFileReader(file)
      page=reader.getPage(0)
      x=page.extractText()
      
      return render_template('new.html',data=x)
      
         
     
if __name__=="__main__":
   app.run(debug=True)






    
        


