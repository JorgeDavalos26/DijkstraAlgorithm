import sys
import matplotlib.pyplot as plt
import networkx as nx

class DijkstrasAlgorithm:
    def __init__(self, graph):
        self.tableNodes = graph["tableNodes"]
        self.tableEdges = graph["tableEdges"]
        self.origin = graph["origin"]
        self.destination = graph["destination"]
    
    def dijkstra(self, origin, destination, weightAccum = 0):
        # parametro de salida de la recursividad
        if destination == origin:
            return

        edgesList = []

        # recolectar las conexiones - peso del nodo visitado
        for row in self.tableEdges:
            if row[0] == origin:
                edgesList.append(row)
        
        # actualizar la tabla
        for rowEdgesList in edgesList:
            for rowNodes in self.tableNodes:
                if rowEdgesList[1] == rowNodes[0]:
                    if (weightAccum + rowEdgesList[2]) < rowNodes[1]:
                        rowNodes[1] = rowEdgesList[2] + weightAccum
                        rowNodes[2] = rowEdgesList[0]
                        print(self.tableNodes)
                        print("----------------------------------")
                    break

        # escoger el minimo camino
        minimumNode = ["", sys.maxsize, ""] # empezammos con infinito como minimo
        for rowEdgesList in edgesList:
            for rowNodes in self.tableNodes:
                if rowNodes[0] == rowEdgesList[1]:
                    if rowNodes[1] < minimumNode[1]:
                        minimumNode = rowNodes
                    break
        # minimumPath termina teniendo la lista que tiene menos peso

        print(minimumNode)

        # acumular
        weightAccum = minimumNode[1]

        # dijkstra (recursivity)
        self.dijkstra(minimumNode[0], destination, weightAccum)

    def run(self):
        # llamar el algoritmo de Dijkstra (con A como origen, con C como destino, 0 como acumulador inicial)
        self.dijkstra(self.origin, self.destination)

        # obtener una lista que nos definira el camino final mas optimo
        finalPath = []
        toFind = self.destination
        while toFind != self.origin:
            for rowNodes in self.tableNodes:
                if toFind == rowNodes[0]:
                    finalPath.append(rowNodes[0])
                    toFind = rowNodes[2]
                    break
        
        finalPath.append(self.origin)
        finalPath.reverse()

        return {
            "tableNodes": self.tableNodes,
            "finalPath": finalPath
        }



































