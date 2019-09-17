from flask import Flask,redirect,url_for,render_template,request,flash
from flask_mail import Mail,Message
from random import randint
from db import Register,Base,User
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

app=Flask(__name__)
engine=create_engine("sqlite:///iiit.db",connect_args={'check_same_thread':False},echo=True)
Base.metadata.bind=engine
DBsession=sessionmaker(bind=engine)
session=DBsession()

app.secret_key='1234'
# app.config['MAIL_SERVER']='smtp.gmail.com'
# app.config['MAIL_PORT']=465
# app.config['MAIL_USERNAME']='kalyanc1242@gmail.com'
# app.config['MAIL_PASSWORD']='anees1243'
# app.config['MAIL_USE_TLS']=False
# app.config['MAIL_USE_SSL']=True

# mail=Mail(app)
# otp=randint(000000,999999)
# app.secret_key='sdfsd'

# @app.route("/email")
# def email():
# 	return render_template("email.html")

# @app.route("/email_verify", methods=['POST','GET'])
# def verify_email():
# 	email=request.form['mail']
# 	msg=Message('One Time Password',sender='kalyanc1242@gmail.com',recipients=[email])
# 	msg.body=str(otp)
# 	mail.send(msg)
# 	return render_template('verify.html')

# @app.route("/verify", methods=['POST','GET'])
# def email_validate():
# 	user_otp=request.form['otp']
# 	if otp==int(user_otp):
# 		return "valid"

# 	else:
# 		return "Not valid"

@app.route('/show', methods=['POST','GET'])
def showData():
	register3=session.query(Register).all()
	return render_template('show.html',reg=register3)

@app.route('/add',methods=['post','get'])
def addData():
	if request.method=='POST':
		newData=Register(name=request.form['name'],
			email=request.form['email'],
			des=request.form['des'])
		session.add(newData)
		session.commit()
		flash('new Data is added')
		return redirect(url_for('showData'))
	else:
		return render_template('add.html')

@app.route('/<int:register_id>/edit',methods=['post','get'])
def editData(register_id):
	editeddata=session.query(Register).filter_by(id=register_id).one()
	if request.method=='POST':
		editeddata.name=request.form['name']
		editeddata.email=request.form['email']
		editeddata.des=request.form['des']
		session.add(editeddata)
		session.commit()
		return redirect(url_for('showData'))
		flash("Edited data")
	else:
		return render_template('edit.html',register=editeddata)


@app.route('/<int:register_id>/delete',methods=['POST','GET'])
def deleteData(register_id):
	deleteddata=session.query(Register).filter_by(id=register_id).one()
	if request.method=='POST':
		session.delete(deleteddata)
		session.commit()
		flash("deleteddata")
		return redirect(url_for('showData'))
	else:
		return render_template('delete.html',register=deleteddata)
if __name__=='__main__':
	app.run(debug=True)