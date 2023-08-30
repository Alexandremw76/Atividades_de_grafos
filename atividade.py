class Grafo:
    # Método construtor que irá criar a matriz de adjacência e a lista de adjacência do grafo.
    def __init__(self, arquivo):
        # Abrir o arquivo especificado para leitura.
        with open(arquivo) as f:
            # Ler a primeira linha do arquivo e extrair o número de vértices do grafo.
            numero_de_vers_ = [int(x) for x in next(f).split()]
            self.numero_de_vers = numero_de_vers_[0]
            
            # Inicializar as estruturas de dados para a matriz de adjacência e a lista de adjacência.
            self.matriz_ad = []
            self.list_ad = []

            # Preencher a matriz de adjacência lendo as linhas restantes do arquivo.
            for line in f:
                # Dividir a linha em números inteiros e adicioná-los à matriz de adjacência.
                self.matriz_ad.append([int(x) for x in line.split()])

        # Construir a lista de adjacência a partir da matriz de adjacência.
        for i in range(len(self.matriz_ad)):
            list_temp = []
            for j in range(len(self.matriz_ad)):
                # Se houver uma aresta entre os vértices i e j, adicionar j à lista de adjacência de i.
                if self.matriz_ad[i][j] == 1:
                    list_temp.append(j)
            # Adicionar a lista de adjacência temporária à lista de adjacência global.
            self.list_ad.append(list_temp)

    # calcular graus apartir da lista de ad    
    def calcular_graus_graf(self):# calcular graus apartir da lista de ad  
        max = 0
        min = len(self.list_ad[0])
        for i in range(len(self.list_ad)):
            if len(self.list_ad[i]) > max:
                max = len(self.list_ad[i])
            if len(self.list_ad[i]) < min:
                min = len(self.list_ad[i])
        print("grau maximo = ",max)
        print("grau minimo = ",min)
   
    #sequencia de graus do grafo
    def seque_vertice(self):
        # Inicializar uma lista para armazenar a sequência de graus dos vértices.
        seq_lista = []
        
        # Iterar sobre a lista de adjacência para calcular o grau de cada vértice.
        for i in range(len(self.list_ad)):
            # O grau de um vértice é o número de vizinhos na lista de adjacência.
            grau = len(self.list_ad[i])
            seq_lista.append(grau)  # Adicionar o grau à lista de sequência de graus.
        
        # Ordenar a lista de sequência de graus em ordem crescente.
        seq_lista.sort()
        
        # Imprimir a sequência de graus do grafo.
        print("Sequência de graus do grafo:", seq_lista)
        
        # Retornar a lista de sequência de graus.
        return seq_lista
    

    #funçao para mostrar grau e vizinhança de um vertice
    def grau_vizi_de_vertice(self, vertice):
        # Calcular o grau do vértice contando o número de vizinhos na lista de adjacência.
        grau = len(self.list_ad[vertice])
        
        # Imprimir o grau do vértice.
        print("Grau do vértice {0} é = {1}".format(vertice, grau))
        
        # Imprimir a vizinhança aberta do vértice.
        print("Vizinhança aberta do vértice", vertice)
        print(self.list_ad[vertice])
        
        # Criar a vizinhança fechada do vértice, que inclui o próprio vértice e seus vizinhos.
        viz_fechada = []
        viz_fechada.append(vertice)  # Adicionar o próprio vértice.
        viz_fechada.extend(self.list_ad[vertice])  # Adicionar os vizinhos à lista.
        
        # Imprimir a vizinhança fechada do vértice.
        print("Vizinhança fechada do vértice", vertice)
        print(viz_fechada)

    #funçao para verificar adjacencia entre vertices
    def ver_adjacencia(self,v,u):

        if self.matriz_ad[v][u] == 1:
            print("vertices sao adjacentes")
        else:
            print("vertices nao sao adjacentes") 

    def ver_regularidade(self):
        # Obter a lista de sequência de graus dos vértices.
        lista = self.seque_vertice()
        
        # Iterar sobre a lista de sequência de graus para verificar a regularidade.
        for i in range(len(lista) - 1):
            # Comparar o grau atual com o próximo grau na lista.
            if lista[i] != lista[i + 1]:
                print("O grafo não é regular.")
                return False
        
        # Se todos os graus forem iguais, o grafo é regular.
        print("O grafo é regular e possui regularidade de {0}".format(lista[i]))
        return True  # Se chegar ao final da lista, retornar True.
    
    def contar_arestas(self):
        num_aresta = 0  # Inicializa o contador de arestas.
        # Itera por todas as combinações de vértices (i, j) onde i < j.
        for i in range(len(self.matriz_ad)):
            for j in range(len(self.matriz_ad)):
                num_aresta += self.matriz_ad[i][j]  # Soma o valor da aresta (i, j).
        return num_aresta//2 # divide por dois para nao haver arestas duplicadas
    
    # conta todos os vertices e compara com n = n*(n-1)/2 se for igual o grafo e completo
    
    def ver_completude(self):
        n = self.numero_de_vers  #número de vértices no grafo.
        n_aresta = self.contar_arestas()  # número de arestas no grafo.

        # Calcula o número máximo de arestas em um grafo completo com n vértices.
        max_aresta = n * (n - 1) // 2

        # Verifica se o número de arestas no grafo é igual ao máximo possível.
        if n_aresta == max_aresta:
            print("O grafo é completo.")
        else:
            print("O grafo não é completo pois possui {0} arestas e para ser completo deveria possuir {1} arestas ".format(n_aresta,max_aresta))

    def ver_vet_universal(self): #Um vértice v é universal quando está conectado por arestas a todos os demais vértices
        n = self.numero_de_vers - 1  #n = numeros de vertices -1(pq o vertice nao pode estar ligado a ele proprio)
        lista_ver_uni = []  # Inicializa a lista para armazenar os vértices universais.

        # Itera por todos os vértices para verificar se são universais.
        for i in range(len(self.list_ad)):
            if len(self.list_ad[i]) == n:
                lista_ver_uni.append(i)  # Adiciona o vértice à lista se for universal.

        print("Vértices universais:", lista_ver_uni)
        return lista_ver_uni
    
    def ver_vet_isolado(self): # um vertice é dito isolado se nao possuir vizinho ou seja sua lista de adjacencia tem tamanho = 0
        lista_ver_isolados = []  # Inicializa a lista para armazenar os vértices isolados.

        # Itera por a lista de adjacencia de todo os vértices para verificar se são isolados.
        for i in range(len(self.list_ad)):
            if len(self.list_ad[i]) == 0: # compara se o tamanho da lista é 0, (vazia)
                lista_ver_isolados.append(i)  # Adiciona o vértice à lista se for isolado.

        print("Vértices isolados:", lista_ver_isolados)
        return lista_ver_isolados

    def ver_sub_grafo(self, vertices_B, arestas_b): # Um subgrafo em um grafo é um subconjunto dos vértices e arestas do grafo original que pode forma um novo grafo caso exista no grafo.
        # Verifica se os vértices B pertencem ao grafo.
        for n in vertices_B: # n vai iterar sober a lista de vertice_b
            if n >= len(self.matriz_ad):
                print("O vértice {0} não pertence ao grafo.".format(n))
                return 0
        
        # Verifica se as arestas b existem no grafo.
        for i, j in arestas_b:
            if self.matriz_ad[i][j] == 0:
                print("A aresta ({0}, {1}) não existe no grafo.".format(i, j))
            else:
                print("Forma um sub-grafo.")

    def ver_passeio(self, vertices_B):

        #Um passeio é uma sequência de vértices onde cada vértice consecutivo na sequência
        #é conectado por uma aresta no grafo, permitindo percorrer de um vértice para o próximo
        #seguindo as arestas.

        # Verifica se existe uma aresta entre vértices consecutivos na lista.
        for i in range(len(vertices_B) - 1):
            vertice_atual = vertices_B[i]
            vertice_prox = vertices_B[i + 1]
            
            # Verifica se há uma aresta entre os vértices atuais e próximos.
            if self.matriz_ad[vertice_atual][vertice_prox] == 0:
                print("Não forma um passeio.")
                return False

        print("Forma um passeio.")
        return True
   
    def ver_caminho(self, vertices_B):
        #um caminho é um passeio onde nao se repete vertices ou seja é uma sequencia de vertices destintos
        for i in range(len(vertices_B) - 1):
            vertice_atual = vertices_B[i]
            vertice_prox = vertices_B[i + 1]
            
            # Verifica se o vértice atual aparece mais de uma vez na sequência.
            if vertices_B.count(vertice_atual) > 1:
                print("Não forma um caminho, existem vértices repetidos.")
                return False
            
            # Verifica se existe uma aresta entre vértices consecutivos na sequência.
            if self.matriz_ad[vertice_atual][vertice_prox] == 0:
                print("Não forma um caminho.")
                return False
            
        print("Forma um caminho.")
        return True
    
    def ver_ciclo(self, vertices_B): 
        # um ciclo é uma sequência de vértices e arestas que começa e termina no mesmo vértice, 
        #percorrendo um caminho através das arestas de forma que não repita nenhum vértice
        inicio = vertices_B[0]
        fim = vertices_B[-1]
        
        # Verifica se o começo é diferente do fim, condição para ser um ciclo.
        if inicio != fim:
            print("O começo é diferente do fim. Não forma um ciclo.")
            return False
        
        inicio = 1  # Segundo vértice.
        fim = len(vertices_B) - 1  # Penúltimo vértice.
        
        # Verifica se há vértices repetidos entre o intervalo
        for i in range(inicio, fim):
            if vertices_B.count(vertices_B[i]) > 1:
                print("Existem vértices repetidos na sequência.")
        
        # Verifica se há arestas entre vértices consecutivos na sequência.
        for i in range(len(vertices_B) - 1):
            vertice_atual = vertices_B[i]
            vertice_prox = vertices_B[i + 1]
            if self.matriz_ad[vertice_atual][vertice_prox] == 0:
                print("Não forma um ciclo.")
                return False
        print("Forma um ciclo.")
        return True
    
    def ver_trilha(self, vertice_b):
        #uma trilha é um caminho onde nao se repete arestas
        lista_arestas_visitadas = []

        # Cria uma lista de pares de vértices consecutivos para formar as arestas
        for i in range(len(vertice_b) - 1):
            aresta = (vertice_b[i], vertice_b[i + 1]) # forma um par de vertices que representam as arestas
            lista_arestas_visitadas.append(sorted(aresta)) # ordenar aresta pra garantir que ex : (0,1) e (1,0) sejam iguais pois representam a mesma arestas
            
        # Verifica a repetição de arestas na sequência.
        for i in range(len(lista_arestas_visitadas) - 1):
            if lista_arestas_visitadas[i] == lista_arestas_visitadas[i + 1]:
                print("Não forma uma trilha.")
                return False
        # Verifica se a sequência forma um caminho.
        if self.ver_caminho(vertice_b) == True:
            print("Forma uma trilha.")
        else:
            print("Não forma uma trilha.")
            
    def ver_clique(self, vertices): # um clique é um subconjunto de vértices de um grafo no qual todos os vértices estão conectados entre si por arestas
        # Itera sobre todos os pares de vértices no conjunto.
        for i in vertices:
            for j in vertices:
                if i != j:  # comparamos vért diferentes.
                    # Verifica se a aresta entre os vértices i e j está ausente.
                    if self.matriz_ad[i][j] != 1:
                        print("Não é um clique, a aresta ({0}, {1}) está ausente.".format(i, j))
                        return False

        print("É um clique, todas as arestas entre os vértices estão presentes.")
        return True
    
    def maximal_clique(self, vertices): # é clique que nao pode ser estendido
        # Verifica se o conjunto de vértices passado é um clique.
        if not self.ver_clique(vertices):
            return False
        
        # Itera sobre todos os vértices que não estão no conjunto de entrada.
        for v in range(len(self.matriz_ad)):
            if v not in vertices: # verifica se um vertice v que nao esta presente no clique original esta conectado a todos o vertice que fazem parte do clique
                conectado_a_todos = True
                
                # Verifica se o vértice v está conectado a todos os vértices no clique.
                for u in vertices:
                    if self.matriz_ad[v][u] == 0:
                        conectado_a_todos = False
                        break  # Se não houver aresta entre v e u, pula para o próximo v.
                    
                if conectado_a_todos: # se houver um vertice v ligado a todos os vertices u o clique nao é maximal pois pode ser extendido com o vertcice v
                    print("Não é um clique maximal.")
                    return False
        
        print("É um clique maximal.")
        return True

class Grafo_Complemento(Grafo):
    def __init__(self,matriz_ad_grafo,num_ver):
        self.numero_de_vers = num_ver
        self.matriz_ad = matriz_ad_grafo
        for i in range(len(self.matriz_ad)):
            for j in range ((len(self.matriz_ad[0]))):
                if self.matriz_ad[i][j] == 0:
                    self.matriz_ad[i][j] = 1
                else:
                    self.matriz_ad[i][j] = 0
        self.list_ad = []
        for i in range(len(self.matriz_ad)):
            list_temp = [] 
            for j in range(len(self.matriz_ad)):
                if self.matriz_ad[i][j] == 1:
                    list_temp.append(j)
            self.list_ad.append(list_temp) 
    def ver_con_independente(self, vertices): # usa mesma funçao do clique
        for i in vertices:
            for j in vertices:
                if i != j:
                    if self.matriz_ad[i][j]!=1:
                        print("NAO é independente")
                        return(False)
        print("é independente")
        return True 


