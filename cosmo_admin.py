from flask import Flask, request, render_template
from flask.ext.socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		print "Logging in"
		return "Login in"
	else:
		print "Showing the logging form"
		return render_template('login.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

## Definicion de los websockets
@socketio.on('my event', namespace='/test')
def test_message(message):
	print 'Sending ' + message['data']
	emit('my response', {'data': message['data']})

@socketio.on('my broadcast event', namespace='/test')
def test_message(message):
	print 'Broadcasting ' + message['data']
	emit('my response', {'data': message['data']}, broadcast=True)

@socketio.on('connect', namespace='/test')
def test_connect():
	print 'Connecting client'
	emit('my response', {'data': 'Connected'})

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
	print 'Client disconnected'

if __name__ == '__main__':
	app.debug = True
	socketio.run(app)
