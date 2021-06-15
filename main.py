from flask import render_template

from flask_socketio import send


from app import app, socketio


# sid --> when a client connect, a session id
# is generated. All the requests by that client
# will have the sid assigned at first.
# environ --> dictionary that has all the details
# of client request.


# socket conection message when a new client connect
# The print appears in server side and the send msg
# appears to client
@socketio.on('connect')
def handle_connection():
    print('A new user has just connected')


# socket handle_message when the client send a new one
@socketio.on('message')
def handle_message(msg):
    print('Message: ' + msg)
    # Returns the msg sent by a client
    send(msg, broadcast=True)
    # Broadcast the client's msg to everyone
    # connected at that momment


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    socketio.run(app, port=5000, debug=True)
    # It's similar to app.run() but it wrapes the app and
    # adds socket.io functionality
