import numpy as np

def load_graph(input_path,delimiter=','):
    if delimiter is None:
        delimiter = ','
    graph_matrix = np.loadtxt(input_path, delimiter=delimiter)
    return graph_matrix