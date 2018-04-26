import stomp
import sys



class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('send an error "%s" in test_queue_server' % message)
    def on_message(self, headers, message):
        print('send a message "%s" in test_queue_server' % message)

conn = stomp.Connection([("192.188.3.101", 61613)])
conn.set_listener('', MyListener())
conn.start()
conn.connect('admin', 'password', wait=True)
conn.send(body=' '.join(sys.argv[1:]), destination='/queue/test')
conn.disconnect()