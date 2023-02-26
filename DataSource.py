import sys
import matplotlib.pyplot as plt
import networkx as nx

graph1 = {
    "tableNodes": [
        ["A", 0, None],
        ["B", sys.maxsize, None],
        ["C", sys.maxsize, None],
        ["D", sys.maxsize, None],
        ["E", sys.maxsize, None],
        ["F", sys.maxsize, None]
    ],
    "tableEdges": [
        ["A", "B", 2],
        ["A", "D", 8],
        ["B", "D", 5],
        ["B", "E", 6],
        ["D", "E", 3],
        ["D", "F", 2],
        ["E", "F", 1],
        ["E", "C", 9],
        ["F", "C", 3]
    ],
    "origin": "A",
    "destination": "C",

    "posNodes": {
        "A": (1, 7),
        "B": (3, 11),
        "C": (9, 7),
        "D": (3, 3),
        "E": (6, 11),
        "F": (6, 3)
    }
}
