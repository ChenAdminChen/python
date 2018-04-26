import zmq
import random
import sys
import time


context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555" )

while True:
    topic = random.randrange(9999,10005)
    messagedata = random.randrange(1,215) - 80
    print("%d %d" % (topic, messagedata))
    socket.send_string("%d %d" % (topic, messagedata))
    time.sleep(1)