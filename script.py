import sqlite3
from flask import Flask,redirect,url_for,render_template,request,abort
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage

#initialize flask web app 
app = Flask(__name__)


conn=sqlite3.connect(r'C:\Users\ghosh\AppData\Local\Programs\Python\Python39\Flask_project\password.db')


#creating user and password database in sqlite3 system if password.db is not present in parents folder. 

command='''CREATE TABLE  if not Exists user_list (name TEXT NOT NULL,pass TEXT NOT NULL)'''


#telling us about the creator
@app.route("/")
def login():
   return render_template('upload.html')
 
 

#from log in page we are taking name and password  and storeing them in database (sqlite3)
@app.route('/detail',methods=["POST","GET"])
def detail():
   if request.method=='POST':
      name=request.form['Uname']
      password=request.form['Pass']
      conn=sqlite3.connect(r'C:\Users\ghosh\AppData\Local\Programs\Python\Python39\Flask_project\password.db')
      c=conn.cursor()
      c.execute("insert into user_list(name,pass) values(?,?)",('human','steel'))
      conn.commit()
      conn.close()
      return render_template('result.html',user=name,password=password)


@app.route('/show') #this thing is not working  it is redirecting to the detail  page only 
def show():
   while true:
      conn=sqlite3.connect(r'C:\Users\ghosh\AppData\Local\Programs\Python\Python39\Flask_project\password.db')
      cur=conn.cursor()
      command='Select * from user_list'
      cur.execute(command)
      datas=cur.fetchall()
      return render_template("display.html",datas=datas)



if __name__=="__main__":
   app.run(debug=True)