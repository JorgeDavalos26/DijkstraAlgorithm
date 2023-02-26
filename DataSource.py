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

graph2 = {
    "tableNodes": [
        ["A", 0, None],
        ["B", sys.maxsize, None],
        ["C", sys.maxsize, None],
        ["D", sys.maxsize, None],
        ["E", sys.maxsize, None],
        ["F", sys.maxsize, None],

        ["Z", sys.maxsize, None]
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
        ["F", "C", 3],

        ["A", "Z", 1],
        ["Z", "C", 1]
    ],
    "origin": "A",
    "destination": "C",

    "posNodes": {
        "A": (1, 7),
        "B": (3, 11),
        "C": (9, 7),
        "D": (3, 3),
        "E": (6, 11),
        "F": (6, 3),

        "Z": (9, 3)
    }
}

graph3 = {
    "tableNodes": [
        ["A", 0, None],
        ["B", sys.maxsize, None],
        ["C", sys.maxsize, None],
        ["D", sys.maxsize, None],
        ["E", sys.maxsize, None],
        ["F", sys.maxsize, None],
        ["P", sys.maxsize, None],
        ["Q", sys.maxsize, None],
        ["R", sys.maxsize, None],
        ["S", sys.maxsize, None]
    ],
    "tableEdges": [
        ["A", "B", 2],
        ["A", "D", 8],
        ["B", "D", 5],
        ["B", "E", 6],
        ["D", "E", 3],
        ["D", "F", 2],
        ["E", "F", 1],
        ["E", "P", 9],
        ["E", "R", 2],
        ["F", "R", 3],
        ["P", "Q", 1],
        ["R", "S", 1],
        ["R", "Q", 1],
        ["R", "S", 13],
        ["P", "S", 1],
        ["Q", "C", 1],
        ["S", "C", 1]
    ],
    "origin": "A",
    "destination": "C",

    "posNodes": {
        "A": (1, 7),
        "B": (3, 11),
        "C": (16, 7),
        "D": (3, 3),
        "E": (6, 11),
        "F": (6, 3),
        "P": (9, 11),
        "Q": (13, 11),
        "R": (9, 3),
        "S": (13, 3),
    }
}
