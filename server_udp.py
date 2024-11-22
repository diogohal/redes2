import socket

HOST = 'localhost'  
PORT = 12345        

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print(f"Servidor UDP escutando em {HOST}:{PORT}...")

while True:
    data, addr = server_socket.recvfrom(1024)  # Recebe até 1024 bytes
    print(f"Mensagem recebida de {addr}: {data.decode('utf-8')}")
    server_socket.sendto(b"Mensagem recebida!", addr) 
