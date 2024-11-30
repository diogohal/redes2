import socket
import os
import time

HOST = '10.254.225.23'
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

file_path = "texto2gb.txt"
BUFFER_SIZE = 1024

print(f"=== Conectando ao servidor UDP {HOST}:{PORT} ===\n")

try:
    file_size = os.path.getsize(file_path)
    file_name = os.path.basename(file_path)
    print(f"[INFO] Enviando informações do arquivo: {file_name} (Tamanho: {file_size} bytes)")
    client_socket.sendto(f"{file_name}|{file_size}".encode('utf-8'), (HOST, PORT))
    
    with open(file_path, "rb") as f:
        sent_bytes = 0
        packets_sent = 0
        start_time = time.time()
        
        while sent_bytes < file_size:
            chunk = f.read(BUFFER_SIZE)
            client_socket.sendto(chunk, (HOST, PORT))
            packets_sent += 1
            sent_bytes += len(chunk)
            print(f"[ENVIADO] Pacote {packets_sent}: {len(chunk)} bytes | Total: {sent_bytes}/{file_size} bytes")
        
        end_time = time.time()

    print("\n[INFO] Transferência concluída.")
    print(f"[INFO] Tamanho final enviado: {sent_bytes} bytes")
    print(f"[INFO] Pacotes enviados: {packets_sent}")
    print(f"[INFO] Tempo total de envio: {end_time - start_time:.2f} segundos\n")
finally:
    client_socket.close()
    print("[INFO] Conexão encerrada.")
