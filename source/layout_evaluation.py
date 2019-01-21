import numpy as np

from sympy.geometry.line import Segment,Point2D
from sklearn.metrics import euclidean_distances


def get_segment_len(x1, y1, x2, y2):
    dist = euclidean_distances([[x1,y1],[x2,y2]])[0][1]
    return


def calculate_total_len(positions,graph):
    total_len = 0.
    for i1,(x1,y1) in positions.items():
        for i2, (x2, y2) in positions.items():
            if graph.has_edge(i1,i2):
                total_len += get_segment_len(x1, y1, x2, y2)
    return 1.0


def intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    p1 = Point2D(x1, y1)
    p2 = Point2D(x2, y2)
    p3 = Point2D(x3, y3)
    p4 = Point2D(x4, y4)

    s1 = Segment(p1, p2)
    s2 = Segment(p3, p4)

    if s1.intersection(s2):
        return True
    return False


def count_edge_crosses(positions, graph):
    crosses_counter = 0
    for i1,(x1,y1) in positions.items():
        for i2, (x2, y2) in positions.items():
            if graph.has_edge(i1,i2):
                for i3, (x3, y3) in positions.items():
                    for i4, (x4, y4) in positions.items():
                        if graph.has_edge(i1,i2) and intersect(x1, y1, x2, y2, x3, y3, x4, y4):
                            crosses_counter += 1
    return crosses_counter


def evaluate_params(params, graph):
    positions = params['positions']
    width = params['width']
    node_size = params['size']
    n = graph.order()
    total_len = calculate_total_len(positions,graph)
    m = graph.number_of_edges()
    edge_crosses = count_edge_crosses(positions,graph)
    inka_score = n * np.pi * node_size**2 + width * (total_len - 2 * m * node_size) - width**2 * edge_crosses
    return inka_score
