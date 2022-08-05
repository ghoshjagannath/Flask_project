
import sqlite3
from flask import Flask,redirect,url_for,render_template,request

#initialize flask web app 
app = Flask(__name__)


conn=sqlite3.connect(r'C:\Users\ghosh\AppData\Local\Programs\Python\Python39\Flask_project\password.db')


#creating user and password database in sqlite3 system if password.db is not present in parents folder. 

command='''CREATE TABLE  if not Exists user_list (name TEXT NOT NULL,pass TEXT NOT NULL)'''


#telling us about the creator
@app.route("/")
def login():
   return render_template('welcome.html')
 
 


#from log in page we are taking name and password  and storeing them in database (sqlite3)
@app.route('/detail',methods=["POST","GET"])
def detail():
   if request.method=='POST':
      name=request.form['Uname']
      password=request.form['Pass']
      with open(r'C:\Users\ghosh\AppData\Local\Programs\Python\Python39\Flask_project\password.db') as conn:
         c=conn.cursor()
         c.execute("insert into user_list('name','pass') values(?,?)"(name,password))
         conn.commit()
         c.close()
         conn.close()
         return 'Success'



if __name__=="__main__":
   app.run(debug=True)