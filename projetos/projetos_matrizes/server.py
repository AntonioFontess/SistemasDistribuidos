import socket
import pickle
import numpy as np

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 8888))  
server.listen(1)

print("[Servidor] Aguardando conexão...")
conn, addr = server.accept()
print(f"[Servidor] Conectado a {addr}")

# Usar makefile para leitura mais confiável com pickle
file = conn.makefile('rb')
try:
    A, B = pickle.load(file)
    print("[Servidor] Matrizes recebidas, realizando multiplicação...")

    resultado = np.dot(A, B)
    conn.sendall(pickle.dumps(resultado))
    print("[Servidor] Resultado enviado ✅")
finally:
    file.close()
    conn.close()
