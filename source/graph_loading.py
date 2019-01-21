from numpy import genfromtxt

def load_graph(input_path,delimiter=','):
    graph_matrix = genfromtxt(input_path, delimiter=delimiter)
    return None