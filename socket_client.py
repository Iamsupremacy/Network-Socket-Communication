import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('127.0.0.1',50443))

while True:
    data = input("Enter data to send: ")
    client_socket.send(data.encode())
    server_data = client_socket.recv(4096)
    if(server_data == ''):break
    print("[+] Server sent: ",server_data.decode())

client_socket.close()





