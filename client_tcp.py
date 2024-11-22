import socket

HOST = 'localhost' 
PORT = 12345        

# Criação do socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

print(f"Conectado ao servidor {HOST}:{PORT}")

try:
    while True:
        message = input("Digite uma mensagem (ou 'sair' para encerrar): ")
        if message.lower() == 'sair':
            break
        client_socket.sendall(message.encode('utf-8'))  # Envia mensagem
        response = client_socket.recv(1024)  # Recebe resposta
        print(f"Resposta do servidor: {response.decode('utf-8')}")
finally:
    client_socket.close()
    print("Conexão encerrada.")
