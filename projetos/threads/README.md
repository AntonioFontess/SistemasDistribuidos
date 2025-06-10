# 🧩 Validador de Sudoku com Threads em Python

Este projeto implementa uma aplicação em **Python com 27 threads** para verificar se uma matriz 9x9 representa uma solução válida para o quebra-cabeça **Sudoku**.

---

## 📚 Referência do Exercício

📘 Livro: *Fundamentos de Sistemas Operacionais*  
✍️ Autores: Abraham Silberschatz, Peter B. Galvin, Greg Gagne  
📍 Página: 110  
📌 Tema: Threads e Concorrência

---

## 🧠 Descrição do Projeto

Um Sudoku válido deve obedecer às seguintes regras:

- Cada **linha** deve conter os dígitos de 1 a 9, sem repetição.
- Cada **coluna** deve conter os dígitos de 1 a 9, sem repetição.
- Cada um dos **nove subgrids 3x3** deve conter os dígitos de 1 a 9, sem repetição.

### Estratégia com Threads

O programa utiliza:
- 9 threads para verificar cada **linha**
- 9 threads para verificar cada **coluna**
- 9 threads para verificar cada **subgrid 3x3**

Totalizando **27 threads** que validam a matriz simultaneamente.

---

## 🧾 Estrutura
threads/

├── threads.py # Script principal com geração e validação de Sudoku



---

## 🚀 Como Executar

1. Execute o script no terminal:
```bash
python threads.py

