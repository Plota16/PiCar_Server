from bluetooth import *
from enum import Enum
import time
from Car import *
from Enums import *


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
#client_sock.setblocking(0)
client_sock.settimeout(0.1)
car = Car()

while True:

    print(car.movement.value + " " + car.turning.value + " " + car.lights.value)
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
        elif data == b'lights_up':
            car.lights_on()
        elif data == b'lights_down':
            car.lights_off()
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