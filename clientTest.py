import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
#host_ip = socket.gethostbyname(host) #change to ip of server device if not being run locally
host_ip = "169.254.7.163"

port = 12345
client.connect((host_ip, 12345))
client.send('I am CLIENT'.encode())
from_server = client.recv(4096)
client.close()
print(from_server.decode('ascii'))