import time
import numpy as np

def multiplicacao_sequencial(A, B):
    inicio = time.time()
    resultado = np.dot(A, B)
    fim = time.time()
    return resultado, (fim - inicio) * 1000
