import zmq  
   
context = zmq.Context()  
socket = context.socket(zmq.PAIR)
socket.connect("tcp://127.0.0.1:5555")  
