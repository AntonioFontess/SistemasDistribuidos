import time
import threading
import numpy as np

def multiplicacao_paralela(A, B):
    C = np.zeros((A.shape[0], B.shape[1]))
    inicio = time.time()

    def calcula_linha(i):
        for j in range(B.shape[1]):
            C[i][j] = sum(A[i][k] * B[k][j] for k in range(B.shape[0]))

    threads = []
    for i in range(A.shape[0]):
        t = threading.Thread(target=calcula_linha, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    fim = time.time()
    return C, (fim - inicio) * 1000
