import graph_data
import math
import sys


def euclidian_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def create_blank_matrix(graph):
    matrix = [-1] * len(graph)
    for i in range(len(matrix)):
        matrix[i] = [-1] * len(matrix)
    return matrix

def create_adj_matrix_from_list(graph):
    # Creates the inital matrix with -1 as default value signifying no path between nodes
    # In case of direction: 
    # matrix[a] = matrix the node is coming from
    # matrix[a][b] = node a to node b, (row a, column b)
    # matrix[b][a] = node b to node a, (row b, column a)
    matrix = create_blank_matrix(graph)

    for node in graph:
        node_coords = node[0]
        adjaceny_list = node[1]
        for node in adjaceny_list:
                

    return matrix

def main():
    current_graph = graph_data.graph_data[4]
    print(create_adj_matrix_from_list(current_graph))

main()

