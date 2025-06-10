import numpy as np
from sequencial import multiplicacao_sequencial
from paralelo import multiplicacao_paralela
from client import distribuido

# Matrizes para multiplicação
A = np.random.rand(100, 100)
B = np.random.rand(100, 100)

print("[MAIN] Iniciando multiplicação sequencial...")
_, tempo_seq = multiplicacao_sequencial(A, B)
print(f"[MAIN] Tempo sequencial: {tempo_seq:.2f} ms")

print("[MAIN] Iniciando multiplicação paralela...")
_, tempo_par = multiplicacao_paralela(A, B)
print(f"[MAIN] Tempo paralelo: {tempo_par:.2f} ms")

print("[MAIN] Iniciando multiplicação distribuída...")
_, tempo_dis = distribuido(A, B)
print(f"[MAIN] Tempo distribuído: {tempo_dis:.2f} ms")

# Salva os tempos
with open("tempoAlgoritmos.txt", "w") as f:
    f.write(f"Tempo Sequencial: {tempo_seq:.2f} ms\n")
    f.write(f"Tempo Paralelo: {tempo_par:.2f} ms\n")
    f.write(f"Tempo Distribuído: {tempo_dis:.2f} ms\n")

print("[MAIN] Tempos salvos em tempoAlgoritmos.txt ✅")
