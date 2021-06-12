from flask import render_template

from flask_socketio import send


from app import app, socketio


# sid --> when a client connect, a session id
# is generated. All the requests by that client
# will have the sid assigned at first.
# environ --> dictionary that has all the details
# of client request.


@socketio.on('message')
def handleMessage(msg):
    print('Message: ' + msg)
    # Returns the msg sent by a client
    send(msg, broadcast=True)
    # Broadcast the client's msg to everyone
    # connected at that momment


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    socketio.run(app)
    # It's similar to app.run() but it wrapes the app and
    # adds socket.io functionality
