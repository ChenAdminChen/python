import zmq  
context = zmq.Context()  
socket = context.socket(zmq.PAIR)  
socket.bind("tcp://127.0.0.1:5555") 