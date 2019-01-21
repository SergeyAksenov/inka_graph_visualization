import argparse
from graph_loading import load_graph
from graph_drawing import draw_graph


parser = argparse.ArgumentParser()

parser.add_argument("--input",
                    required=True,
                    help="path to input csv file")


parser.add_argument("--output",
                    required=True,
                    help="where to save picture")

parser.add_argument("--sep",
                    help="delimiter used in input csv")


def main():
    args = parser.parse_args()
    graph_path =  args.input
    output_path = args.output
    delimiter = args.sep

    graph_matrix = load_graph(graph_path, delimiter)

    draw_graph(graph_matrix, output_path)


if __name__ == '__main__':
    main()