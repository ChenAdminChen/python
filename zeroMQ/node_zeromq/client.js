var zmq = require('./node_modules/zeromq');

console.log("Collecting updates from weather server…");

// Socket to talk to server
var subscriber = zmq.socket('sub');

// Subscribe to zipcode, default is NYC, 10001


 subscriber.subscribe("");

// process 100 updates

 subscriber.on('message', function(data) {
 	var piece = data.toString();
  console.log(piece)
 });

subscriber.connect("tcp://192.168.0.105:5555");
