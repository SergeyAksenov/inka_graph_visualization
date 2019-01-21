from generating_positions import *
from layout_evaluation import *

LAYOUT_FUNCTIONS = [spring_layout]
WIDTHS = [0.25, 0.5, 0.75, 1.0]
NODE_SIZES = [150,200,250,300]


def generate_params(graph):
    params_list = []
    for layout_func in LAYOUT_FUNCTIONS:
        positions = layout_func(graph)
        for width in WIDTHS:
            for node_size in NODE_SIZES:
                params = {"width" : width,
                          "node_size" : node_size,
                          "positions" : positions}
                params_list.append(params)
    return params_list


def select_params(params_list, graph):
    best_params = params_list[0]
    best_inka_score = 0.
    for params in params_list:
        inka_score = evaluate_params(params, graph)
        if inka_score > best_inka_score:
            best_inka_score = inka_score
            best_params = params
    return best_params


def select_best_params(graph):
    possible_params = generate_params(graph)
    params = select_params(possible_params, graph)
    return params