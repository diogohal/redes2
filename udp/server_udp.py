import socket
import time

# Configurações do servidor
HOST = ''
PORT = 12345
BUFFER_SIZE = 2048
TIMEOUT = 2  # Timeout em segundos

# Criando socket e define seu timeout
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))
server_socket.settimeout(TIMEOUT)

print(f"=== Servidor UDP escutando em {HOST}:{PORT} ===\n")
while True:
    print("[INFO] Aguardando informações sobre o arquivo...")
    try:
        # Recebendo os metadados do arquivo (nome e tamanho)
        file_info, client_addr = server_socket.recvfrom(BUFFER_SIZE)
    except:
        break
    
    # Processando os metadados recebidos
    file_name, file_size = file_info.decode('utf-8').split('|')
    file_size = int(file_size)
    print(f"[INFO] Recebendo arquivo '{file_name}' de {client_addr} (Tamanho: {file_size} bytes)\n")
    
    # Criando arquivo local para salvar os dados recebidos
    with open(f"recebido_{file_name}", "wb") as f:
        total_bytes = 0
        packets_received = 0
        start_time = time.time()

        while total_bytes < file_size:
            try:
                # Recebendo dados do cliente
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

    # Informações do LOG
    print("\n[INFO] Transferência concluída.")
    print(f"[INFO] Tamanho final recebido: {total_bytes} bytes")
    print(f"[INFO] Pacotes recebidos: {packets_received}")
    print(f"[INFO] Tempo total de recepção: {end_time - start_time:.2f} segundos\n")
