import socket

# Configurações do servidor
HOST = 'localhost'  # Escuta localmente
PORT = 12345        # Porta para escutar

# Criação do socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print(f"Servidor UDP escutando em {HOST}:{PORT}...")

while True:
    data, addr = server_socket.recvfrom(1024)  # Recebe até 1024 bytes
    print(f"Mensagem recebida de {addr}: {data.decode('utf-8')}")
    server_socket.sendto(b"Mensagem recebida!", addr)  # Responde ao cliente
