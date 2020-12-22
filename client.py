import threading
import socket

nickname = input('Choose your nickname')

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('52.53.175.159', 55555))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message=='Nick':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print('An error occured!!!!')
            client.close()
            break
def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))
receive_thread = threading.Thread(target=receive)
receive_thread.start()
write_thread = threading.Thread(target=write)
write_thread.start()