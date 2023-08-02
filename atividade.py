class Grafo:
    # metodo construtor que ira fazer lista de ad e matriz de ad
    def __init__(self, arquivo):
        with open(arquivo) as f:
            self.numero_de_vers = [int(x)for x in next (f).split()]
            self.matriz_ad= []
            self.list_ad = []
            # fazer matriz de ad
            for line in f:
                self.matriz_ad.append([int(x) for x in line.split()])
            # fazer lista de ad apartir da matriz de ad
        for i in range(len(self.matriz_ad)):
            list_temp = [] 
            for j in range(len(self.matriz_ad)):
                if self.matriz_ad[i][j] == 1:
                    list_temp.append(j)
            self.list_ad.append(list_temp)    

    # metodos para teste             
    def mostrar_matriz_ad(self,num):
        print("matriz de ad do vertice:",num)
        print(self.matriz_ad[num])
    def mostrar_lista_ad(self,num):
        print("vizinhaça  do grafo:",num)
        print(self.list_ad[num])
    def mostrar_num_verts(self):
        print("numero de vertice ",self.numero_de_vers)
    ##########################################################
   
    # calcular graus apartir da lista de ad    
    def calcular_graus_graf(self):
        max = 0
        min = len(self.list_ad[0])
        for i in range(len(self.list_ad)):
            if len(self.list_ad[i]) > max:
                max = len(self.list_ad[i])
            if len(self.list_ad[i]) < max:
                min = len(self.list_ad[i])
        print("grau maximo = ",max)
        print("grau minimo = ",min)
   
    #sequencia de graus do grafo
    def seque_vertice(self):
        seq_lista = []
        for i in range(len(self.list_ad)):
            seq_lista.append(len(self.list_ad[i]))  
        
        seq_lista.sort()
        print("sequencia de graus do grafo",seq_lista)
        return seq_lista
    

    #funçao para mostrar grau e vizinhança de um vertice
    def grau_vizi_de_vertice(self,num):
        grau = len(self.list_ad[num])
        print("grau do vertice {0} é = {1}".format(num,grau))
        print("vizinhaça aberta do grafo",num)
        print(self.list_ad[num])
        print("vizinhaça fechada do grafo",num)
        viz_fechada = []
        viz_fechada.append(num)
        viz_fechada.append(self.list_ad[num])
        print(viz_fechada)


    #funçao para verificar adjacencia entre vertices
    def ver_adjacencia(self,v,u):
        list = self.list_ad[v]
        print(list)
        if list.count(u) == True:
            print("vertices sao adjacentes")
        else:
            print("vertices nao sao adjacentes") 


    def ver_regularidade(self): # comparar se todos os graus da lista de sequencias de graus de vertices é igual
        lista = self.seque_vertice()
        for i in range(len(lista) - 1): 
            if(lista[i] != lista[i + 1]): 
                print("grafo nao é regular")
                return False
        print("grafo é regular, e possui regularidade de {0}".format(lista[i])) 
        return True # caso chegue ao final da lista, retornamos True.
    
    # conta todas as aresta do grafo [pula uma linha da matriz a cada iteraçao]
    def contar_arestas(self):
        num_aresta = 0
        n = len(self.matriz_ad)

        for i in range(n):
            for j in range(i + 1, n):
                num_aresta += self.matriz_ad[i][j] #i + 1 para evitar contar as arestas duas vezes. [pula uma linha da matriz a cada iteraçao]

        return  num_aresta
    
    # conta todos os vertices e compara com n = n*(n-1)/2 se for igual o grafo e completo
    def ver_completude(self):
        n = self.numero_de_vers[0]
        n_aresta=self.contar_arestas()
        n = n*(n-1)/2
        if n_aresta == n:
            print("grafo é completo")
        else:
            print("grafo nao é completo")

    def ver_vet_universal(self): # retorna a lista com todos os vertices universais (compara a tamanho da lista de ad de todos os vertice com tolta de vertices -1)
        n = self.numero_de_vers[0]-1
        lista_ver_uni = []
        for i in range(len(self.list_ad)):
            if len(self.list_ad[i]) == n:
                lista_ver_uni.append(i)
        print("vertices universais",lista_ver_uni)
        return lista_ver_uni
    
    def ver_vet_isolado(self): # retorna a lista com todos os vertices isolados (compara a tamanho da lista de ad de todos os vertice com 0)
        lista_ver_isolados = []
        for i in range(len(self.list_ad)):
            if len(self.list_ad[i]) == 0:
                lista_ver_isolados.append(i)
        print("vertices isolados",lista_ver_isolados)
        return lista_ver_isolados

    def ver_sub_grafo(self, vertices_B,arestas_b):
        for i in range(len(vertices_B)):
            n = vertices_B[i]
            if(n >= len(self.matriz_ad)):
                #print("Vertice nao pertence a o grafo")
                return 0
        for i in range(len(arestas_b)):
            i ,j = arestas_b[i]
            if(self.matriz_ad[i][j] == 0):
                print("aresta nao existe") 
            else:
                print("forma um sub-grafo") 

    def ver_passeio(self, vertices_B):
        for i in range(len(vertices_B) - 1):
            vertice_atual = vertices_B[i]
            vertice_prox = vertices_B[i + 1]
            if self.matriz_ad[vertice_atual][vertice_prox] == 0:
                print("Não forma um passeio.")
                return False

        print("Forma um passeio.")
        return True
    def ver_passeio(self, vertices_B):
        for i in range(len(vertices_B) - 1):
            vertice_atual = vertices_B[i]
            vertice_prox = vertices_B[i + 1]
            if self.matriz_ad[vertice_atual][vertice_prox] == 0:
                print("Não forma um passeio.")
                return False

        print("Forma um passeio.")
        return True 
    def ver_caminho(self, vertices_B):
        for i in range(len(vertices_B) - 1):
            vertice_atual = vertices_B[i]
            vertice_prox = vertices_B[i + 1]
            if vertices_B.count(vertice_atual) > 1:
                print("Não forma um caminho, existem vertices repetidos.")
                return False
            if self.matriz_ad[vertice_atual][vertice_prox] == 0:
                print("Não forma um caminho.")
                return False
        print("Forma um caminho.")
        return True 
    
    def ver_ciclo(self,vertices_B):
        começo = vertices_B[0]
        fim = vertices_B[-1]
        if(começo != fim ):
            print("começo diferente do fim")
            return False
        começo = 1# segundo
        fim = len(vertices_B)-1# penultimo
        for i in range(começo,fim): # verifica se existe repetiçao no vertices apos o inico 
           if vertices_B.count(vertices_B[i]) > 1: 
                print("existem vertices repetidos")
        for i in range(len(vertices_B) - 1):
            vertice_atual = vertices_B[i]
            vertice_prox = vertices_B[i + 1]
            if self.matriz_ad[vertice_atual][vertice_prox] == 0:
                print("Não forma um ciclo.")
                return False
        print("Forma um ciclo")
    def ver_trilha(self,vertice_b):
        lista_arestas_passados = []
        for i in range(len(vertice_b)-1):
            lista = []
            lista.insert(i, vertice_b[i])
            lista.insert(i, vertice_b[i+1])
            lista.sort()
            lista_arestas_passados.append(lista)
        for i in range(len(lista_arestas_passados)-1):
            if(lista_arestas_passados[i] == lista_arestas_passados[i+1]):
                    print(lista_arestas_passados[i],lista_arestas_passados[i+1])
                    print("nao forma uma trilha")
                    return False
        if(self.ver_caminho(vertice_b) == True):
            print("forma um trilha")
        else:
            print("nao forma um trilha")
grafo1 = Grafo("grafo.txt")

#grafo1.mostrar_matriz_ad(0)
#grafo1.mostrar_lista_ad(4)
#grafo1.mostrar_num_verts()
#grafo1.calcular_graus_graf()
#grafo1.seque_vertice()
#grafo1.grau_vizi_de_vertice(0)
#grafo1.ver_adjacencia(4,2)
#grafo1.ver_regularidade()
#grafo1.contar_arestas()
#grafo1.ver_completude()
#grafo1.ver_vet_universal()
#grafo1.ver_vet_isolado()
vertices_B = [0, 2, 3]  # conjunto de vertices
vertices_c = [0,1,4] # conjunto de vertices com ciclo
arestas_b = [(0, 2), (2, 3),(0,3)] # par de arestas
#grafo1.ver_sub_grafo(vertices_B,arestas_b)
#grafo1.ver_passeio(vertices_c)
#grafo1.ver_caminho(vertices_c)
#grafo1.ver_ciclo(vertices_c)
grafo1.ver_trilha(vertices_c)
