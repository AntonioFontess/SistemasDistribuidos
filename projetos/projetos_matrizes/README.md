# 🧮 Multiplicação de Matrizes: Sequencial, Paralela e Distribuída (TCP)

Este projeto realiza a multiplicação de matrizes utilizando três abordagens:

- ✅ Sequencial (usando NumPy)
- ⚙️ Paralela (com `threading`)
- 🌐 Distribuída (usando Cliente/Servidor via TCP com `socket`)

 ## 🧠 Objetivo
Este projeto tem finalidade educacional para demonstrar:

A diferença de desempenho entre abordagens sequenciais, paralelas e distribuídas

Como implementar uma arquitetura cliente-servidor com TCP usando Python

Técnicas básicas de medição de tempo e manipulação de matrizes

Ao final, os tempos de execução de cada abordagem são comparados e salvos em `tempoAlgoritmos.txt`.

---

### 📁 Estrutura do Projeto
mat_mult_project/

├── client.py # Cliente TCP - envia matrizes e recebe resultado

├── server.py # Servidor TCP - realiza a multiplicação

├── sequencial.py # Multiplicação sequencial com NumPy

├── paralelo.py # Multiplicação paralela usando threads

├── main.py # Script principal que executa tudo e salva os tempos

├── tempoAlgoritmos.txt # Arquivo com os tempos medidos


---

## 🧪 Tecnologias utilizadas

- Python 3.x
- `numpy`
- `socket`
- `threading`
- `pickle`

---

## 🚀 Como Executar

### 1. Instale o NumPy (se ainda não tiver):
   pip install numpy

### 2. Abra dois terminais: 
```bash

Terminal 1 – Servidor:
python server.py

Terminal 2 – Cliente (executa tudo):
python main.py

Exemplo de Execução:
Tempo Sequencial: 1.00 ms
Tempo Paralelo: 511.10 ms
Tempo Distribuído: 2.00 ms

