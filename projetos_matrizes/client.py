import socket
import pickle
import time

def distribuido(A, B):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("localhost", 8888))  

    inicio = time.time()
    s.sendall(pickle.dumps((A, B)))

    s.shutdown(socket.SHUT_WR)

    # Receber resultado
    data = b""
    while True:
        packet = s.recv(4096)
        if not packet:
            break
        data += packet

    resultado = pickle.loads(data)
    fim = time.time()
    s.close()
    return resultado, (fim - inicio) * 1000
