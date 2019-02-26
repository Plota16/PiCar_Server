from bluetooth import *
from enum import Enum
import time

class Movment(Enum):
    forward = "Going forward"
    stop = "Stopping"
    backward = "Going backward"


class Turning(Enum):
    left = "Turning left"
    right = "Turning right"
    straight = "Going straight"


class Lights(Enum):
    on = "on"
    off = "off"


class Car:
    def __init__(self):
        self.movement = Movment.stop
        self.turning = Turning.straight
        self.lights = Lights.off

    def turn_right(self):
        self.turning = Turning.right

    def turn_left(self):
        self.turning = Turning.left

    def go_straight(self):
        self.turning = Turning.straight

    def go_forward(self):
        self.movement = Movment.forward

    def go_backward(self):
        self.movement = Movment.backward

    def stop(self):
        self.movement = Movment.stop



server_sock = BluetoothSocket(RFCOMM)
server_sock.bind(("", PORT_ANY))
server_sock.listen(1)


port = server_sock.getsockname()[1]

uuid = "52d82dc4-3628-4b3e-ae69-a1fec1384e4f"

advertise_service(server_sock, "AquaPiServer",
                  service_id=uuid,
                  service_classes=[uuid, SERIAL_PORT_CLASS],
                  profiles=[SERIAL_PORT_PROFILE],
                  #                   protocols = [ OBEX_UUID ]
                  )
print("waiting for connection on RFCOMM channel %d" % port)
client_sock, client_info = server_sock.accept()
print("Accepted connection from ", client_info)
client_sock.setblocking(0)
car = Car()

while True:

    print(car.movement.value + " " + car.turning.value)
    time.sleep(0.1)

    try:
        data = client_sock.recv(1024)
        if len(data) == 0: break
        #print("received [%s]" % data)

        if data == b'go':
            car.go_forward()
        elif data == b'go_back':
            car.go_backward()
        elif data == b'stop':
            car.stop()
        elif data == b'left':
            car.turn_left()
        elif data == b'right':
            car.turn_right()
        elif data == b'straight':
            car.go_straight()
        else:
            data = 'WTF!'
            print("WTF")



        #client_sock.send(data)
        #print("sending [%s]" % data)

    except IOError:
        pass

    except KeyboardInterrupt:

        print("disconnected")

        client_sock.close()
        server_sock.close()
        print("all done")
        break