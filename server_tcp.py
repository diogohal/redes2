import socket
import os
import time

HOST = 'localhost'
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Servidor escutando em {HOST}:{PORT}...")

while True:
    conn, addr = server_socket.accept()
    print(f"Conexão estabelecida com {addr}")
    
    with open("arquivo_recebido", "wb") as f:
        print("Recebendo arquivo...")
        total_bytes = 0
        start_time = time.time()
        while True:
            data = conn.recv(1024)
            if not data:
                break
            f.write(data)
            total_bytes += len(data)
        end_time = time.time()
    
    print(f"Arquivo recebido com sucesso. Tamanho: {total_bytes} bytes.")
    print(f"Tempo total de recepção: {end_time - start_time:.2f} segundos.")
    
    conn.close()
    print("Conexão encerrada.")
    break
