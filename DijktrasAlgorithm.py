import sys
import matplotlib.pyplot as plt
import networkx as nx

tabla = [
    ["A", 0, None],
    ["B", sys.maxsize, None],
    ["C", sys.maxsize, None],
    ["D", sys.maxsize, None],
    ["E", sys.maxsize, None],
    ["F", sys.maxsize, None]
]

pesos = [
    ["A", "B", 2],
    ["A", "D", 8],
    ["B", "D", 5],
    ["B", "E", 6],
    ["D", "E", 3],
    ["D", "F", 2],
    ["E", "F", 1],
    ["E", "C", 9],
    ["F", "C", 3]
]

def dijkstra(origen, destino, pesoAcumulado):
    # parametro de salida de la recursividad
    if destino == origen:
        return

    pesosAux = []

    # recolectar las conexiones - peso del nodo visitado
    for filaPesos in pesos:
        if filaPesos[0] == origen:
            pesosAux.append(filaPesos)
    
    # actualizar la tabla
    for filaPesosAux in pesosAux:
        for filaTabla in tabla:
            if filaTabla[0] == filaPesosAux[1]:
                if pesoAcumulado + filaPesosAux[2] < filaTabla[1]:
                    filaTabla[1] = filaPesosAux[2] + pesoAcumulado
                    filaTabla[2] = filaPesosAux[0]
                    print(tabla)
                    print("----------------------------------")
                break

    # escoger el minimo camino
    aux = ["?", sys.maxsize, "?"] # empezammos con infinito como minimo
    for filaPesosAux in pesosAux:
        for filaTabla in tabla:
            if filaPesosAux[1] == filaTabla[0]:
                if filaTabla[1] < aux[1]:
                    aux = filaTabla
                break
    # aux termina teniendo la lista que tiene menos peso

    print(aux)

    # acumular
    pesoAcumulado = aux[1]

    # dijkstra
    dijkstra(aux[0], destino, pesoAcumulado)


# llamar el algoritmo de Dijkstra (con A como origen, con C como destino, 0 como acumulador inicial)
origen = "A"
destino = "C"
dijkstra(origen, destino, 0)

# obtener una lista que nos definira el camino final mas optimo
camino = []
aBuscar = destino
while aBuscar != origen:
    for filaTabla in tabla:
        if aBuscar == filaTabla[0]:
            camino.append(filaTabla[0])
            aBuscar = filaTabla[2]
            break
camino.append(origen)
camino.reverse()

# imprimir el camino
print("**********************************************")
print(camino)

# ------------------------------------------------------------------------------------
G = nx.Graph()
G.graph["Name"] = "ay que cambiarlo"

G.add_nodes_from([
    ("A", {"Label":"A"}),
    ("B", {"Label":"B"}),
    ("C", {"Label":"C"}),
    ("D", {"Label":"D"}),
    ("E", {"Label":"E"}),
    ("F", {"Label":"F"})
])

G.add_edges_from([
    ("A", "B", {"weight": 2}),
    ("A", "D", {"weight": 8}),
    ("B", "D", {"weight": 5}),
    ("B", "E", {"weight": 6}),
    ("D", "E", {"weight": 3}),
    ("D", "F", {"weight": 2}),
    ("E", "F", {"weight": 1}),
    ("E", "C", {"weight": 9}),
    ("F", "C", {"weight": 3})
])

edgesQueSiFunciona = [
    ('A', 'B'), ('A', 'D'), ('B', 'D'), ('B', 'E'), ('E', 'C'), ('F', 'C'), ('D', 'E'), ('D', 'F'), ('E', 'F')
]

pos = {
    "A": (1, 7),
    "B": (3, 11),
    "C": (9, 7),
    "D": (3, 3),
    "E": (6, 11),
    "F": (6, 3) 
}



pos_node_attributes = {}
for node,(x,y) in pos.items():
    pos_node_attributes[node] = (x+0.5, y-1.5)

node_labels = {n: (d["Label"]) for n,d in G.nodes(data=True)}

edge_labels = {(u,v):d["weight"] for u,v,d in G.edges(data=True)}

node_colors = ["green" if n in camino else "lightgray" for n in G.nodes()]

caminoTuplas = []
for k, nodo in enumerate(camino):
    if k+1 >= len(camino):
        break
    caminoTuplas.append((camino[k], camino[k+1]))
print(caminoTuplas)
edge_colors = ["green" if n in caminoTuplas else "lightgray" for n in edgesQueSiFunciona]

print(edge_colors)

nx.draw(G, pos=pos, with_labels=True, node_color=node_colors, node_size=3000, font_color="white", font_size=20, 
    font_family="Times New Roman", edge_color=edge_colors, width=5)

nx.draw_networkx_labels(G, pos=pos_node_attributes, labels=node_labels, font_color="black", font_size=12, 
    font_family="Times New Roman")
    
nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels, label_pos=0.5)

plt.margins(0.2)
plt.show()






























