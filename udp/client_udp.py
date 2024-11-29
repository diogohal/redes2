import socket
import os
import time

HOST = 'localhost'
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

file_path = "../texto1mb.txt"  
BUFFER_SIZE = 1024
ack_message = "ACK"

print(f"=== Conectando ao servidor UDP {HOST}:{PORT} ===\n")

try:
    file_size = os.path.getsize(file_path)
    file_name = os.path.basename(file_path)
    print(f"[INFO] Enviando informações do arquivo: {file_name} (Tamanho: {file_size} bytes)")
    client_socket.sendto(f"{file_name}|{file_size}".encode('utf-8'), (HOST, PORT))
    
    with open(file_path, "rb") as f:
        sent_bytes = 0
        packets_sent = 0
        packets_acknowledged = 0
        start_time = time.time()
        
        while sent_bytes < file_size:
            chunk = f.read(BUFFER_SIZE)
            client_socket.sendto(chunk, (HOST, PORT))
            packets_sent += 1
            sent_bytes += len(chunk)
            print(f"[ENVIADO] Pacote {packets_sent}: {len(chunk)} bytes | Total: {sent_bytes}/{file_size} bytes")
            
            try:
                client_socket.settimeout(2.0)  
                response, addr = client_socket.recvfrom(BUFFER_SIZE)
                if response.decode('utf-8') == ack_message:
                    packets_acknowledged += 1
            except socket.timeout:
                print(f"[AVISO] Timeout: Sem ACK para o pacote {packets_sent}. Reenviando...")
                sent_bytes -= len(chunk)
                packets_sent -= 1
                f.seek(sent_bytes)  

        end_time = time.time()

    print("\n[INFO] Transferência concluída.")
    print(f"[INFO] Tamanho final enviado: {sent_bytes} bytes")
    print(f"[INFO] Pacotes enviados: {packets_sent}")
    print(f"[INFO] Pacotes confirmados (ACKs): {packets_acknowledged}")
    print(f"[INFO] Tempo total de envio: {end_time - start_time:.2f} segundos\n")
finally:
    client_socket.close()
    print("[INFO] Conexão encerrada.")
