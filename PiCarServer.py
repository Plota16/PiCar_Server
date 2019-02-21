from bluetooth import *


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
while True:
    print("Waiting for connection on RFCOMM channel %d" % port)

    client_sock, client_info = server_sock.accept()
    print("Accepted connection from ", client_info)

    try:
        data = client_sock.recv(1024)
        if len(data) == 0: break
        print("received [%s]" % data)
        print(data)
        if data == 'up':
            print("Go forward")
        elif data == 'down':
            print("Go backward")
        elif data == 'left':
            print("Turn left")
        elif data == 'right':
            print("Turn right")
        else:
            data = 'WTF!'

        client_sock.send(data)
        print("sending [%s]" % data)

    except IOError:
        pass

    except KeyboardInterrupt:

        print("disconnected")

        client_sock.close()
        server_sock.close()
        print("all done")

        break