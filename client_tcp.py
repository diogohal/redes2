import socket
import os
import time

HOST = 'localhost'
PORT = 12345

file_path = "texto1mb.txt"  

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

print(f"Conectado ao servidor {HOST}:{PORT}")

try:
    file_size = os.path.getsize(file_path)
    print(f"Enviando arquivo de {file_size} bytes...")
    
    start_time = time.time()
    with open(file_path, "rb") as f:
        while chunk := f.read(1024):
            client_socket.sendall(chunk)
    end_time = time.time()
    
    print(f"Arquivo enviado com sucesso.")
    print(f"Tempo total de envio: {end_time - start_time:.2f} segundos.")
finally:
    client_socket.close()
    print("Conexão encerrada.")
