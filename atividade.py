class Grafo:
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
    def mostrar_matriz_ad(self,num):
        print("matriz de ad do vertice:",num)
        print(self.matriz_ad[num])
    def mostrar_lista_ad(self,num):
        print("vizinho do grafo:",num)
        print(self.list_ad[num])
    def mostrar_num_verts(self):
        print("numero de vertice ",self.numero_de_vers)

grafo1 = Grafo("grafo.txt")

grafo1.mostrar_matriz_ad(0)
grafo1.mostrar_lista_ad(0)
grafo1.mostrar_num_verts()
