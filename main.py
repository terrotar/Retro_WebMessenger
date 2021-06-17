from flask import render_template, redirect, request, url_for

from flask_socketio import disconnect, send, emit, join_room, leave_room

from flask_login import current_user, login_user, logout_user

from app import app, socketio, db
from app.models import User


# sid --> when a client connect, a session id
# is generated. All the requests by that client
# will have the sid assigned at first.
# environ --> dictionary that has all the details
# of client request.


# socket conection message when a new client connect
# The print appears in server side and the send msg
# appears to client


@socketio.on('connect')
def handle_connect():
    if(current_user.is_authenticated):
        emit(f"{current_user.username} has joined the room.",
             broadcast=True)
        print(f"{current_user.username} has logged in.")
    else:
        return False


@socketio.on('disconnect')
def handle_disconnect():
    emit(f"{current_user.username} has left room.",
         broadcast=True)
    print(f"{current_user.username} has logged out.")


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


@app.route('/register', methods=['GET', 'POST'])
def register():
    if(request.method == "GET"):
        return render_template('register_page.html')
    if(request.method == "POST"):
        email = request.form['email']
        password = request.form['pwd']
        username = request.form['username']
        name = request.form['name']
        # Check if username, name and email are unique
        all_users = User.query.all()
        # Loop to run all_users in db and do the check's
        for user in all_users:
            if(user.username == username or
               user.name == name or
               user.email == email):
                return render_template('register_page.html',
                                       info_error=True)
        user = User(username=username,
                    password=password,
                    name=name,
                    email=email)
        db.session.add(user)
        db.session.commit()
        # I was using render_template('index.html') but
        # it was raising and error because the url of browser
        # was loading index.html but with '/register' in the end...
        return redirect(url_for('index'))
    else:
        return render_template('register_page.html',
                               info_error=True)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if(request.method == 'POST'):
        email = request.form['email']
        pwd = request.form['pwd']
        # Check email and password of input
        user = User.query.filter_by(email=email).first()
        if(not user or not user.verify_password(pwd)):
            return render_template('index.html',
                                   login_error=True)
        else:
            login_user(user)
            return render_template('login_page.html')
    if(request.method == 'GET'):
        return render_template('login_page.html')


@app.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return render_template('index.html')


@app.route('/<username>/delete', methods=['GET', 'POST'])
def delete_user(username):
    if(request.method == 'GET'):
        return render_template('delete_account.html')
    if(request.method == 'POST'):
        pwd = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.verify_password(pwd):
            db.session.delete(user)
            db.session.commit()
            return render_template('index.html')
        else:
            return render_template('delete_account.html',
                                   password_error=True)


@app.route('/<username>/change_info', methods=['GET', 'POST'])
def change_info(username):
    if(request.method == 'GET'):
        return render_template('change_info.html')
    if(request.method == 'POST'):
        new_email = request.form['email']
        new_username = request.form['username']
        new_name = request.form['name']
        new_password = request.form['new_password']
        old_password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.verify_password(old_password):
            user.email = new_email
            user.name = new_name
            user.username = new_username
            user.password = new_password
            db.session.commit()
            return redirect(url_for('login'))
        else:
            return render_template('change_info.html',
                                   password_error=True)


@app.route('/teste_room', methods=['GET', 'POST'])
def teste_room():
    return render_template('room_01.html')


if __name__ == '__main__':
    socketio.run(app, port=5000, debug=True)
    # It's similar to app.run() but it wrapes the app and
    # adds socket.io functionality
