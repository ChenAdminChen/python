import stomp
import sys
import time


class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('send an error "%s" in test_queue_server' % message)
    def on_message(self, headers, message):
        print('send a message "%s" in test_queue_server' % message)

conn = stomp.Connection([("192.168.0.180", 61613)])
conn.set_listener('', MyListener())
conn.start()
conn.connect('admin', 'password', wait=True)

#conn.send(body=' '.join(sys.argv[1:]), destination='/topic/test')
for i in range(1,10000):
	print('send '+str(i))
	conn.send(body=str(i), destination='/topic/test')
	time.sleep(1)
	
conn.disconnect()