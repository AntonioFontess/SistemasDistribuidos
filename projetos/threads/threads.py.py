import threading
import random
import copy

#aluno: Antonio Fontes RA:2454106

def generate_random_sudoku():
    # Sudoku válido base
    valid_sudoku = [
        [2, 3, 7, 8, 4, 1, 5, 6, 9],
        [1, 8, 6, 7, 9, 5, 2, 4, 3],
        [5, 9, 4, 3, 2, 6, 7, 1, 8],
        [3, 1, 5, 6, 7, 4, 8, 9, 2],
        [4, 6, 9, 5, 8, 2, 1, 3, 7],
        [7, 2, 8, 1, 3, 9, 4, 5, 6],
        [6, 4, 2, 9, 1, 8, 3, 7, 5],
        [8, 5, 3, 4, 6, 7, 9, 2, 1],
        [9, 7, 1, 2, 5, 3, 6, 8, 4]
    ]
    
    # Faz uma cópia profunda do Sudoku válido
    sudoku = copy.deepcopy(valid_sudoku)
    
    # 50% de chance de gerar um Sudoku inválido
    if random.choice([True, False]):
        # Escolhe uma linha aleatória para modificar
        row = random.randint(0, 8)
        
        # Escolhe duas colunas diferentes na mesma linha
        col1, col2 = random.sample(range(9), 2)
        
        # Troca dois valores na linha para criar uma duplicata
        sudoku[row][col1], sudoku[row][col2] = sudoku[row][col2], sudoku[row][col1]
        
        # Garante que seja inválido adicionando uma duplicata explícita
        duplicate_value = random.randint(1, 9)
        col = random.randint(0, 8)
        sudoku[row][col] = duplicate_value
        sudoku[row][(col + 1) % 9] = duplicate_value
    
    return sudoku

def check_row(sudoku, row_index, results, result_index):
    seen = [False] * 10
    for num in sudoku[row_index]:
        if num < 1 or num > 9 or seen[num]:
            results[result_index] = False
            return
        seen[num] = True
    results[result_index] = True

def check_col(sudoku, col_index, results, result_index):
    seen = [False] * 10
    for i in range(9):
        num = sudoku[i][col_index]
        if num < 1 or num > 9 or seen[num]:
            results[result_index] = False
            return
        seen[num] = True
    results[result_index] = True

def check_subgrid(sudoku, subgrid_index, results, result_index):
    start_row = (subgrid_index // 3) * 3
    start_col = (subgrid_index % 3) * 3
    seen = [False] * 10
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            num = sudoku[i][j]
            if num < 1 or num > 9 or seen[num]:
                results[result_index] = False
                return
            seen[num] = True
    results[result_index] = True

def validate_sudoku(sudoku):
    results = [False] * 27  # 9 linhas + 9 colunas + 9 subgrids
    threads = []
    
    # Threads para linhas
    for i in range(9):
        t = threading.Thread(target=check_row, args=(sudoku, i, results, i))
        threads.append(t)
        t.start()
    
    # Threads para colunas
    for j in range(9):
        idx = 9 + j
        t = threading.Thread(target=check_col, args=(sudoku, j, results, idx))
        threads.append(t)
        t.start()
    
    # Threads para subgrids
    for k in range(9):
        idx = 18 + k
        t = threading.Thread(target=check_subgrid, args=(sudoku, k, results, idx))
        threads.append(t)
        t.start()
    
    # Aguarda todas as threads terminarem
    for t in threads:
        t.join()
    
    return all(results)

def print_sudoku(sudoku):
    print("Sudoku atual:")
    for i, row in enumerate(sudoku):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        print(" ".join(str(x) for x in row[:3]) + " | " + 
              " ".join(str(x) for x in row[3:6]) + " | " + 
              " ".join(str(x) for x in row[6:]))

if __name__ == "__main__":
    while True:
        input("\nPressione Enter para gerar e validar um novo Sudoku...")
        sudoku = generate_random_sudoku()
        
        print_sudoku(sudoku)
        
        print("\nValidando com 27 threads...")
        
        is_valid = validate_sudoku(sudoku)
        print("\nResultado:", "VÁLIDO" if is_valid else "INVÁLIDO")
        
        choice = input("\nDeseja continuar? (s/n): ").lower()
        if choice != 's':
            break