# 🎮 Super Trunfo — Algoritmos e Programação I

Projeto final da disciplina **Algoritmos e Programação I** — Universidade Presbiteriana Mackenzie.

Desenvolvimento de uma versão funcional do jogo **Super Trunfo**, utilizando exclusivamente conceitos fundamentais de lógica de programação e estruturas de dados básicas.

## 👩‍💻 Desenvolvedoras

- **Natália V. Cerqueira**
- **Gabrielly N. Rodrigues**

---

## 📚 Sobre o Projeto

Este projeto implementa o motor do jogo **Super Trunfo**, permitindo partidas:

- 🎯 **Single Player** (Jogador vs Computador)
- 👥 **Multiplayer** (Jogador vs Jogador)

O sistema foi desenvolvido respeitando as restrições da disciplina, com foco em:

- Manipulação de listas
- Listas aninhadas (matrizes)
- Estruturas condicionais
- Laços de repetição
- Aleatoriedade (`random`)
- Lógica de comparação de atributos

---

## ⚙️ Regras do Jogo

O jogo funciona da seguinte forma:

- Cada carta possui um **nome** e **atributos numéricos**.
- O baralho é embaralhado e dividido entre dois jogadores.
- Em cada rodada:
  - O jogador escolhe um atributo.
  - O atributo é comparado com a carta adversária.
- A carta com maior valor vence a rodada.
- Em caso de empate:
  - As cartas vão para um **monte de espera**.
  - O vencedor da próxima rodada recebe as cartas acumuladas.
- O jogo termina quando um jogador conquistar todas as cartas.

---

## 🗂️ Estrutura das Cartas

As cartas são representadas utilizando **listas de listas**, conforme exigido pela disciplina.

Exemplo:

```python
gabarito = [
    "Nome",
    "Velocidade (km/h)",
    "Tanque (litros)",
    "Ano (int)"
]

baralho = [
    ["Ferrari F40", 324, 120, 1987],
    ["Bugatti Chiron", 420, 100, 2016],
    ["Audi R8", 330, 83, 2021]
]