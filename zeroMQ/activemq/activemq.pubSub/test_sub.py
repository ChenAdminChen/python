import time
import sys

import stomp

class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('received an error "%s" in test_sub' % message)
    def on_message(self, headers, message):
        print('received a message "%s" in test_sub' % message)

conn = stomp.Connection([("192.168.0.180",61613)])
conn.set_listener('', MyListener())
conn.start()
conn.connect('admin', 'password', wait=True)

conn.subscribe(destination='/topic/test', id=1, ack='auto')

time.sleep(100)
conn.disconnect()