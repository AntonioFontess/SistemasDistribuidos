# Sistema de Reserva de Quartos - Java RMI

Este é um sistema simples de **reserva de quartos** implementado em Java utilizando **RMI (Remote Method Invocation)**.

## 📚 Descrição

O sistema segue o modelo **cliente/servidor**, onde:

- O **servidor (`ServidorHotel`)** mantém os dados dos quartos disponíveis e os registros dos hóspedes.
- O **cliente (`ClienteHotel`)** interage com o servidor remotamente para:
  - Listar quartos disponíveis
  - Reservar quartos
  - Listar hóspedes registrados

Não há escolha de data na reserva: **todas as reservas são para o mesmo período fixo**.

---

## 🏨 Tipos de Quartos

| Tipo | Descrição           | Quantidade | Preço (R$) |
|------|---------------------|------------|------------|
| 0    | Quarto Individual   | 10         | 100,00     |
| 1    | Quarto Duplo        | 20         | 150,00     |
| 2    | Quarto Duplo Luxo   | 5          | 200,00     |
| 3    | Quarto Triplo       | 3          | 250,00     |
| 4    | Quarto Quádruplo    | 2          | 300,00     |

---

## ⚙️ Funcionalidades

- `listagem()`: Mostra quantos quartos estão disponíveis por tipo.
- `reserva(int tipo, String nome)`: Reserva um quarto do tipo especificado para o hóspede.
- `hospede()`: Lista todos os hóspedes que fizeram reserva.

---
## 🧱 Estrutura do Projeto
│
├── GerenciadorQuartos.java     # Interface remota

├── ServidorHotel.java          # Implementação do servidor

├── ClienteHotel.java           # Aplicação cliente

├── Quarto.java                 # Classe auxiliar com tipo, preço e hóspede


## 🚀 Como executar

### 1. Compile os arquivos Java:
```bash
javac *.java

Inicie o registro RMI:
start rmiregistry

Execute o servidor:
java ServidorHotel

Em outro terminal, execute o cliente:
java ClienteHotel





