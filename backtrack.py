class SolucionadorHamiltoniano:
    def __init__(self, grafo):
        """
        - num_vertices: O número de vértices no grafo.
        - grafo: A matriz de adjacência representando o grafo.
        - caminho: Uma lista para armazenar o caminho sendo construído.
        - vertices_map: Um dicionário para mapear índices (0, 1, 2...) para nomes ('A', 'B', 'C'...).
        """
        self.num_vertices = len(grafo) # Vamos pegar o número de vértices a partir do grafo (Através do tamanho da matriz)
        self.grafo = grafo # Matriz de adjacência (UNICA VARIAVEL QUE PRECISAMOS PASSAR PARA A CLASSE, TOD O RESTO É CALCULADO A PARTIR DELA)
        self.caminho = [-1] * self.num_vertices # Lista para guardar o caminho (inicialmente vazia, com -1)
        self.vertices_map = {i: chr(ord('A') + i) for i in range(self.num_vertices)} # Mapeamento besta, so para fica 0 = A, 1 = B, 2 = C ...
        self.contador_solucoes = 0
        
    def encontrar_todos_circuitos(self):

        # Função para encontrar todos os circuitos Hamiltonianos no grafo.
        # Inicia a busca por todos os circuitos Hamiltonianos.
        # Começamos com o primeiro vértice no caminho. (PARA MEU EXEMPLO)

        # Podemos escolher qualquer vértice para começar, mas aqui escolhi o 0 (A)
        ver_inicio = 0 # VARIAVEL IMPORANTE, SO MUDAR PARA ESCOLHER O VERTICE QUE ELE VAI COMEÇAR (NAO QUE MUDE O RESULTADO FINAL, MAS A ORDEM DE IMPRESSÃO)
        self.caminho[0] = ver_inicio
        print(f"Inicando a busca pelo vertice: '{self.vertices_map[ver_inicio]}'")
        self._resolver_util(1) # Chamamos a função, mas não dependemos mais do seu retorno
        if self.contador_solucoes == 0:
            print("Nenhum Circuito Hamiltoniano encontrado.")
        else:
            print(f"\nTotal de {self.contador_solucoes} circuitos encontrados.")

    def _resolver_util(self, pos):
       
        # Função recursiva para tentar encontrar o vertice valido para a posição 'pos' no caminho.
        # CASO BASE: Se todos os vértices estão no caminho (ENCONTRAMOS UMA SOLUÇÃO)
        if pos == self.num_vertices:
            # Verifica se o último vértice se conecta ao primeiro (SE SÃO IGUAIS, SE FOREM TEMOS UM CIRCUITO)
            if self.grafo[self.caminho[pos - 1]][self.caminho[0]] == 1:
                # SOLUÇÃO ENCONTRADA!
                self._imprimir_solucao()
                self.contador_solucoes += 1
            # IMPORTANTE: não retornamos nada aqui para forçar o backtracking
            return

        # TENTATIVA E RECURSÃO (idêntico ao anterior)
        for v in range(self.num_vertices):
            if self.seguro(v, pos):
                self.caminho[pos] = v
                self._resolver_util(pos + 1)
                # BACKTRACK: Essencial para explorar outras possibilidades
                self.caminho[pos] = -1

        
        return False

    def seguro(self, v, pos):
        """
        Verifica se o vértice 'v' pode ser adicionado na posição 'pos' do caminho.
        """
        # 1. Verifica se há uma aresta entre o último vértice do caminho e 'v'.
        ultimo_vertice_no_caminho = self.caminho[pos - 1]
        if self.grafo[ultimo_vertice_no_caminho][v] == 0:
            return False

        # 2. Verifica se o vértice 'v' já não está no caminho.
        for vertice_no_caminho in self.caminho:
            if vertice_no_caminho == v:
                return False

        return True

    def _imprimir_solucao(self):
        # SO serve para PRINTAR na nossa forma bonitinha (A -> B -> C ...)
        caminho_legivel = [self.vertices_map[i] for i in self.caminho]
        print("Caminho:", " ---> ".join(caminho_legivel), "--->", caminho_legivel[0])




####### PARTE DA EXECUÇÃO DO CÓDIGO ########

# PLAY
if __name__ == "__main__":
    # Vamos criar o grafo em forma de matriz de adjacência
    # O GRAFO É IGUAL AO QUE CRIEI NO NOTEBOOK E USEI COMO EXEMPLO (LITERALMENTE O MESMO!)
    grafo_matriz = [
        [0, 1, 1, 1, 0, 0],  # A
        [1, 0, 1, 1, 0, 0],  # B
        [1, 1, 0, 0, 1, 1],  # C
        [1, 1, 0, 0, 1, 0],  # D
        [0, 0, 1, 1, 0, 1],  # E
        [0, 0, 1, 0, 1, 0],  # F
    ]

    # Como comentei la em cima, so precisamos chamar a classe com a matriz de adjacência
    resposta = SolucionadorHamiltoniano(grafo_matriz)
    resposta.encontrar_todos_circuitos()