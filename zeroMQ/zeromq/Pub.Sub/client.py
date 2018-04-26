import sys
import zmq

# http://learning-0mq-with-pyzmq.readthedocs.io/en/latest/pyzmq/patterns/pubsub.html

# Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)  #订阅信息

print("Collecting updates from weather server...")
socket.connect ("tcp://localhost:5555")

	
# Subscribe to zipcode, default is NYC, 10001
topicfilter = "10001"
socket.setsockopt_string(zmq.SUBSCRIBE, topicfilter)

# Process 5 updates
total_value = 0
for update_nbr in range (5):
    string = socket.recv()
    topic, messagedata = string.split()
    total_value += int(messagedata)
    print(str(topic), messagedata)

print("Average messagedata value for topic '%s' was %dF" % (topicfilter, total_value / update_nbr))