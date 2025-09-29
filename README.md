# Circuito Hamiltoniano com Backtracking

Este repositório contém a implementação de um algoritmo de **backtracking** para encontrar todos os **Circuitos Hamiltonianos** em um grafo. O projeto foi desenvolvido como parte do Seminário 01 da disciplina de Projeto e Análise de Algoritmos (PAA).

-------------
### Sobre o Problema

Um **Circuito Hamiltoniano** é um caminho em um grafo que:
- Visita cada vértice exatamente uma vez
- Retorna ao vértice inicial, formando um circuito fechado

Este é um problema clássico da teoria dos grafos e pertence à classe NP-Completo, não havendo algoritmos conhecidos que o resolvam em tempo polinomial para grafos gerais.

-------------
### Estratégia Implementada

- Fixa o vértice inicial
- Para cada posição do caminho, tenta todos os vértices possíveis
- Verifica duas condições de segurança:
  - Existe aresta entre o último vértice do caminho e o candidato?
  - O vértice candidato já foi visitado?
- Ao completar o caminho, verifica se há conexão de volta ao início
-------------

## Estrutura do Código

### Classe Principal: `SolucionadorHamiltoniano`

#### Métodos Principais:

- `encontrar_todos_circuitos()`: Ponto de entrada, inicia a busca
- `_resolver_util(pos)`: Função recursiva que implementa o backtracking
- `seguro(v, pos)`: Verifica se um vértice pode ser adicionado ao caminho
- `_imprimir_solucao()`: Formata e exibe a solução encontrada


## Como Executar

1. **Clone o repositório**

2. **Execute o código:**
   ```bash
   python backtrack.py
   ```

## Exemplo de Uso

O código esta com um grafo de exemplo com 6 vértices (A, B, C, D, E, F):
Esse grafo é o grafo de exemplo no arquivo `grafo_example.png`
Caso queira testar com qualquer outro grafo é so passar a **Matriz Adjacencia**

```python
grafo_matriz = [
    [0, 1, 1, 1, 0, 0],  # A
    [1, 0, 1, 1, 0, 0],  # B
    [1, 1, 0, 0, 1, 1],  # C
    [1, 1, 0, 0, 1, 0],  # D
    [0, 0, 1, 1, 0, 1],  # E
    [0, 0, 1, 0, 1, 0],  # F
]
```

## Arquivos no Repositório

```
Seminario-01/
├── backtrack.py         # Implementação principal do algoritmo
├── grafo_example.png    # Grafo de exemplo que vamos usar no backtrack (Criamos no jupyter)
├── Seminario 1.pdf.     # PDF com as instruções para a atividade
├── apresentação         # Pasta com o ppt que utilizei no seminario
└── grafos.ipynb.        # Jupyter Notebook onde usamos a lib NetworkX para visualizarmos nosso grafo!

```

## YouTube

**Apresentação do Algoritmo**: [Link será adicionado em breve]

---

**Desenvolvido por**: Caio Vasconcelos Silva Andrade  
**Disciplina**: Projeto e Análise de Algoritmos (PAA)  
**Instituição**: UFS - Universidade Federal de Sergipe