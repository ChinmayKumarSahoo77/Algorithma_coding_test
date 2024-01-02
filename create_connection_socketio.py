# Create a socket client and server with socket io library pass random value between server and client.

import socketio
import eventlet

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
 '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

eventlet.wsgi.server(eventlet.listen(('', 5000)), app)

@sio.event
def connect(sid, environ):
    print('server connected to client with session ID =  ',sid)

def my_message(sid,data):
    sio.send(data)
    print('data sent from server ')

@sio.event
def response(sid,recdata):
    print(recdata)


# sio = socketio.Client()

# @sio.event
# def connect():
#     print('connection established')

# @sio.event
# def message(data):
#     print(data)

# @sio.event
# def send_message():
#     sio.emit(event = 'response', data = {'message': 'HI from client'})
#     print('data sent to server')

# sio.connect('http://localhost:3000') 

# @sio.event
# def disconnect():
#  print('disconnected from server=>CLIENT')