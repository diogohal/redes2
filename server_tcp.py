import socket

HOST = 'localhost' 
PORT = 12345        

# Criação do socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Servidor escutando em {HOST}:{PORT}...")

while True:
    conn, addr = server_socket.accept()
    print(f"Conexão estabelecida com {addr}")
    
    while True:
        data = conn.recv(1024)  # Recebe dados, ate 1024
        if not data:
            break
        print(f"Recebido: {data.decode('utf-8')}")
        conn.sendall(b"Mensagem recebida!")  # Responde ao cliente
    
    conn.close()
    print("Conexão encerrada.")
