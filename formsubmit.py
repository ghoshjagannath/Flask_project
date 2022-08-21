from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

from flask import Flask,render_template


app=Flask(__name__)
app.config['SECRET_KEY']='123'

class Form(FlaskForm):  
   name = StringField("Candidate Name ")  
   submit = SubmitField("Submit")  
  

@app.route("/base")
def base():
   return render_template('base.html')
 


@app.route('/', methods=['GET', 'POST'])
def submit():
    form = Form()
    if form.validate_on_submit():
       return redirect(url_for("/welcome.html"))
    return render_template('wtf.html', form=form)
 
 
 



if __name__=='__main__':
   app.run(debug=True)