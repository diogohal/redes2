import socket
import os
import time

HOST = 'localhost'
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print(f"=== Servidor UDP escutando em {HOST}:{PORT} ===\n")

BUFFER_SIZE = 1024
ack_message = "ACK"

while True:
    print("[INFO] Aguardando informações sobre o arquivo...")
    file_info, client_addr = server_socket.recvfrom(BUFFER_SIZE)
    file_name, file_size = file_info.decode('utf-8').split('|')
    file_size = int(file_size)
    print(f"[INFO] Recebendo arquivo '{file_name}' de {client_addr} (Tamanho: {file_size} bytes)\n")
    
    with open(f"recebido_{file_name}", "wb") as f:
        total_bytes = 0
        packets_received = 0
        packets_lost = 0
        start_time = time.time()
        
        while total_bytes < file_size:
            try:
                server_socket.settimeout(5.0)  # Timeout para evitar travamento
                data, addr = server_socket.recvfrom(BUFFER_SIZE)
                if addr == client_addr:
                    f.write(data)
                    total_bytes += len(data)
                    packets_received += 1
                    print(f"[RECEBIDO] Pacote {packets_received}: {len(data)} bytes | Total: {total_bytes}/{file_size} bytes")
                    server_socket.sendto(ack_message.encode('utf-8'), client_addr)  # Envia ACK
            except socket.timeout:
                print("[AVISO] Timeout: Pacote não recebido.")
                packets_lost += 1

        end_time = time.time()

    print("\n[INFO] Transferência concluída.")
    print(f"[INFO] Tamanho final recebido: {total_bytes} bytes")
    print(f"[INFO] Pacotes recebidos: {packets_received}")
    print(f"[INFO] Pacotes perdidos: {packets_lost}")
    print(f"[INFO] Tempo total de recepção: {end_time - start_time:.2f} segundos\n")