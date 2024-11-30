import socket
import time

HOST = ''
PORT = 12345
BUFFER_SIZE = 1024
TIMEOUT = 2  # Timeout em segundos

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

# Define o timeout para o socket
server_socket.settimeout(TIMEOUT)

print(f"=== Servidor UDP escutando em {HOST}:{PORT} ===\n")

while True:
    print("[INFO] Aguardando informações sobre o arquivo...")
    try:
        file_info, client_addr = server_socket.recvfrom(BUFFER_SIZE)
    except:
        break
        
    file_name, file_size = file_info.decode('utf-8').split('|')
    file_size = int(file_size)
    print(f"[INFO] Recebendo arquivo '{file_name}' de {client_addr} (Tamanho: {file_size} bytes)\n")
    
    with open(f"recebido_{file_name}", "wb") as f:
        total_bytes = 0
        packets_received = 0
        start_time = time.time()

        while total_bytes < file_size:
            try:
                data, addr = server_socket.recvfrom(BUFFER_SIZE)
                if addr == client_addr:
                    f.write(data)
                    total_bytes += len(data)
                    packets_received += 1
                    print(f"[RECEBIDO] Pacote {packets_received}: {len(data)} bytes | Total: {total_bytes}/{file_size} bytes")
            except socket.timeout:
                print(f"[ERRO] Timeout atingido! Nenhum dado recebido por {TIMEOUT} segundos.")
                break

        end_time = time.time()

    print("\n[INFO] Transferência concluída.")
    print(f"[INFO] Tamanho final recebido: {total_bytes} bytes")
    print(f"[INFO] Pacotes recebidos: {packets_received}")
    print(f"[INFO] Tempo total de recepção: {end_time - start_time:.2f} segundos\n")
