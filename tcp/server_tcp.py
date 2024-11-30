import socket
import os
import time

HOST = '10.254.225.23'
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"=== Servidor escutando em {HOST}:{PORT} ===\n")

while True:
    conn, addr = server_socket.accept()
    print(f"[INFO] Conexão estabelecida com {addr}\n")

    with open("arquivo_recebido", "wb") as f:
        print("[INFO] Recebendo arquivo...")
        total_bytes = 0
        chunk_count = 0
        start_time = time.time()
        
        while True:
            data = conn.recv(1024)
            if not data:
                break
            f.write(data)
            total_bytes += len(data)
            chunk_count += 1
            print(f"[RECEBIDO] Chunk {chunk_count}: {len(data)} bytes | Total recebido: {total_bytes} bytes")
        
        end_time = time.time()

    print("\n[INFO] Arquivo recebido com sucesso.")
    print(f"[INFO] Tamanho total do arquivo: {total_bytes} bytes")
    print(f"[INFO] Tempo total de recepção: {end_time - start_time:.2f} segundos\n")
    conn.close()
    print("[INFO] Conexão encerrada.\n")
    break
