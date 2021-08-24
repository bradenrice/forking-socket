import os
import socketserver
import time
import random


class ForkingEchoRequestHandler(socketserver.BaseRequestHandler):

    def setup(self):
        cur_pid = os.getpid()
        print(f'{cur_pid}: Incomming request...')
        return

    def handle(self):
        # Echo the back to the client
        data = self.request.recv(1024)
        cur_pid = os.getpid()
        response = b'%d: %s' % (cur_pid, data)
        print(response)
        time.sleep(random.randint(3, 5))
        self.request.send(response)
        return
    
    def finish(self):
        cur_pid = os.getpid()
        print(f'{cur_pid}: finishing request...')
        return


class ForkingEchoServer(socketserver.ForkingMixIn,
                        socketserver.TCPServer,
                        ):
    pass


if __name__ == '__main__':
    import socket
    import threading

    address = ('localhost', 6000)  # let the kernel assign a port
    server = ForkingEchoServer(address,
                               ForkingEchoRequestHandler)
    ip, port = server.server_address  # what port was assigned?
    print(ip)
    print(port)

    server.serve_forever()