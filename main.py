from flask import Flask,render_template,url_for,request,redirect
from database import * 
import demjson
print("hello")
app=Flask(__name__)

'''~~~~~~~~~HOME~~~~~~~~~`'''
@app.route('/',methods=['post','get'])
def home():
	return render_template('home.html')

'''~~~~~~~~REGISTER~~~~~~~~'''
@app.route('/register.html',methods=['post','get'])
def register():
	if "submit" in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		gender=request.form['gender']
		date=request.form['date']
		email=request.form['email']
		phone=request.form['phone']
		password=request.form['password']
		q = "insert into login (user_name,password,login_type) values('%s','%s','care_taker')"%(email,password)
		rep=insert(q)
		q="insert into care_takers (login_id,fname,lname,gender,dob,email,phone,ct_status) values('%s','%s','%s','%s','%s','%s','%s','active')" %(rep,fname,lname,gender,date,email,phone)
		rep=insert(q)
		
	return render_template('register.html')

'''~~~~~~~~LOGIN~~~~~~~~~'''
@app.route('/login.html',methods=['post','get'])
def login():
	if "login" in request.form:
		username=request.form['username']
		password=request.form['password']
		q="select * from login where user_name='%s' and password='%s'" %(username,password)
		res=select(q)
		print(res)
		if len(res)>0:
			if res[0]['login_type']=='admin':
				return redirect(url_for('admin'))
			elif res[0]['login_type']=='care_taker':
				return redirect(url_for('caretaker'))
	return render_template('login.html')

@app.route('/admin',methods=['post','get'])
def admin():
	q = "select * from users"
	res = select(q)
	print(res)
	return render_template('admin.html',data=res)

@app.route('/caretaker',methods=['post','get'])
def caretaker():
	return render_template('caretaker.html')


@app.route('/api/login',methods=['post','get'])
def api_login():
	a = {'status':"success"}
	return demjson.encode(a)

	
app.run(debug=True)