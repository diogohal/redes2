import socket
import os
import time

# Configurações do servidor
HOST = '10.254.225.23'
PORT = 12345
BUFFER_SIZE = 2048

# Criando socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"=== Servidor escutando em {HOST}:{PORT} ===\n")
while True:
    # Aceitando a conexão do cliente
    conn, addr = server_socket.accept()
    print(f"[INFO] Conexão estabelecida com {addr}\n")

    # Criando um arquivo para salvar os dados recebidos
    with open("arquivo_recebido", "wb") as f:
        print("[INFO] Recebendo arquivo...")

        # Inicializando variáveis para controle da recepção
        total_bytes = 0
        chunk_count = 0
        start_time = time.time()
        
        # Loop para receber os dados em chunks
        while True:
            data = conn.recv(BUFFER_SIZE)
            if not data:
                break
            f.write(data)
            total_bytes += len(data)
            chunk_count += 1
            print(f"[RECEBIDO] Chunk {chunk_count}: {len(data)} bytes | Total recebido: {total_bytes} bytes")
        
        end_time = time.time()

    # Informações do LOG
    print("\n[INFO] Arquivo recebido com sucesso.")
    print(f"[INFO] Tamanho total do arquivo: {total_bytes} bytes")
    print(f"[INFO] Tempo total de recepção: {end_time - start_time:.2f} segundos\n")
    conn.close()
    print("[INFO] Conexão encerrada.\n")
    break
