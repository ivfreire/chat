from flask import Flask, session, redirect, render_template, request, url_for
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.secret_key = 'secret cat'
io = SocketIO(app)

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


@io.on('connect')
def connect():
	if 'username' in session:
		emit('new-user', { 'username': session['username'] }, broadcast=True)

@io.on('new-message')
def receive(data):
	if 'message' in data:
		emit('new-message', {
			'username': session['username'],
			'message': data['message']
		}, broadcast=True)

@io.on('disconnect')
def disconnect():
	emit('remove-user', { 'username': session['username'] }, broadcast=True)