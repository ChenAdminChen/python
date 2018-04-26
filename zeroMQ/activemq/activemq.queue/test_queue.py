import time
import sys

import stomp

class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('received an error "%s" in test_queue' % message)
    def on_message(self, headers, message):
        print('received a message "%s" in test_queue' % message)

conn = stomp.Connection([("192.168.0.180",61613)])
conn.set_listener('', MyListener())
conn.start()
conn.connect('admin', 'password', wait=True)

conn.subscribe(destination='/queue/test', id=1, ack='auto')

#conn.send(body=' '.join(sys.argv[1:]), destination='/queue/test')

time.sleep(2)
conn.disconnect()