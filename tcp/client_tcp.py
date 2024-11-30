import socket
import os
import time

# Configurações do servidor UDP
HOST = '10.254.225.23'
PORT = 12345
BUFFER_SIZE = 1024
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Arquivo a transmitido
file_path = "texto2gb.txt"  

print(f"=== Conectado ao servidor {HOST}:{PORT} ===\n")
try:
    # Obtendo informações do arquivo
    file_size = os.path.getsize(file_path)
    print(f"[INFO] Iniciando envio do arquivo: {file_path}")
    print(f"[INFO] Tamanho total do arquivo: {file_size} bytes\n")
    
    # Inicializando variáveis para controle do envio
    start_time = time.time()
    sent_bytes = 0
    chunk_count = 0

    # Abrindo o arquivo em modo leitura binária
    with open(file_path, "rb") as f:
        # Loop para ler o arquivo em chunks
        while chunk := f.read(BUFFER_SIZE):
            client_socket.sendall(chunk)
            sent_bytes += len(chunk)
            chunk_count += 1
            percent_complete = (sent_bytes / file_size) * 100
            print(f"[ENVIADO] Chunk {chunk_count}: {len(chunk)} bytes | Total enviado: {sent_bytes} bytes "
                  f"({percent_complete:.2f}%)")
    
    end_time = time.time()
    
    # Informações do LOG
    print("\n[INFO] Arquivo enviado com sucesso.")
    print(f"[INFO] Tamanho total enviado: {sent_bytes} bytes")
    print(f"[INFO] Tempo total de envio: {end_time - start_time:.2f} segundos\n")
finally:
    client_socket.close()
    print("[INFO] Conexão encerrada.\n")
