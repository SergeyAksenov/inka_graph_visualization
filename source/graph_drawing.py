import networkx as nx

from parameters_selection import *
from matplotlib import pyplot as plt

def draw_graph(graph_matrix, output_path):
    graph = nx.from_numpy_matrix(graph_matrix)
    params = select_best_params(graph)

    nx.draw_networkx(graph,
                     width=params['width'],
                     node_size=params['node_size'],
                     pos=params['positions'])

    plt.savefig(output_path)
