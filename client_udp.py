import socket

# Configurações do cliente
HOST = 'localhost'  # Endereço do servidor
PORT = 12345        # Porta usada pelo servidor

# Criação do socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(f"Conectando ao servidor UDP {HOST}:{PORT}")

try:
    while True:
        message = input("Digite uma mensagem (ou 'sair' para encerrar): ")
        if message.lower() == 'sair':
            break
        client_socket.sendto(message.encode('utf-8'), (HOST, PORT))  # Envia mensagem
        response, addr = client_socket.recvfrom(1024)  # Recebe resposta
        print(f"Resposta do servidor: {response.decode('utf-8')}")
finally:
    client_socket.close()
    print("Conexão encerrada.")
