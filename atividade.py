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
        print("vizinhos do grafo:",num)
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
grafo1 = Grafo("grafo.txt")

grafo1.mostrar_matriz_ad(0)
grafo1.mostrar_lista_ad(0)
grafo1.mostrar_num_verts()
grafo1.calcular_graus_graf()
grafo1.seque_vertice()
