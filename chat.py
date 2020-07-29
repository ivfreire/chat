from flask import Flask, session, redirect, render_template, request, url_for
app = Flask(__name__)

app.secret_key = 'secret cat'

@app.route('/')
def index():
	if 'username' in session:
		return render_template('index.html', username=session['username'])
	else:
		return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
	session['username'] = request.form['username']
	return redirect('/')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
	if 'username' in session:
		session.pop('username', None)
	return redirect('/')