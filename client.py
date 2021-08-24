import socket
import multiprocessing 

ip = 'localhost'
port = 6000

def mp_request():
# Connect to the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

# Send the data
    message = 'Hello, world'.encode()
    print('Sending : {!r}'.format(message))
    len_sent = s.send(message)

# Receive a response
    response = s.recv(1024)
    print('Received: {!r}'.format(response))

    s.close()

jobs = []

for i in range(3):
    jobs.append(multiprocessing.Process(target=mp_request, args=()))

for proc in jobs:
    proc.start()

for proc in jobs:
    proc.join()
