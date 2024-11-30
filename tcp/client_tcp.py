import socket
import os
import time

HOST = '10.254.225.23'
PORT = 12345

file_path = "texto2gb.txt"  

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

print(f"=== Conectado ao servidor {HOST}:{PORT} ===\n")

try:
    file_size = os.path.getsize(file_path)
    print(f"[INFO] Iniciando envio do arquivo: {file_path}")
    print(f"[INFO] Tamanho total do arquivo: {file_size} bytes\n")
    
    start_time = time.time()
    sent_bytes = 0
    chunk_count = 0
    
    with open(file_path, "rb") as f:
        while chunk := f.read(1024):
            client_socket.sendall(chunk)
            sent_bytes += len(chunk)
            chunk_count += 1
            percent_complete = (sent_bytes / file_size) * 100
            print(f"[ENVIADO] Chunk {chunk_count}: {len(chunk)} bytes | Total enviado: {sent_bytes} bytes "
                  f"({percent_complete:.2f}%)")
    
    end_time = time.time()
    
    print("\n[INFO] Arquivo enviado com sucesso.")
    print(f"[INFO] Tamanho total enviado: {sent_bytes} bytes")
    print(f"[INFO] Tempo total de envio: {end_time - start_time:.2f} segundos\n")
finally:
    client_socket.close()
    print("[INFO] Conexão encerrada.\n")
