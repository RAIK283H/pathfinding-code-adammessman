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
    parents = create_blank_matrix(graph)

    for index in range(len(graph)):
        node_coords = graph[index][0]
        adjaceny_list = graph[index][1]
        for adj_node in adjaceny_list:
                adj_node_coords = graph[adj_node][0]
                edge_weight = euclidian_distance(node_coords, adj_node_coords)
                matrix[index][adj_node] = edge_weight
                
                # TODO: CHECK THIS
                parents[index][adj_node] = index

    return matrix

def floyd_warshall_algorithm(graph_matrix, parents):
     for k in range(len(graph_matrix)):
          for i in range(len(graph_matrix)):
               for j in range(len(graph_matrix)):
                    if (graph_matrix[i][k] + graph_matrix[k][j] < graph_matrix[i][j]):
                        graph_matrix[i][j] = graph_matrix[i][k] + graph_matrix[k][j]
                        parents[i][j] = k
                    
                    # graph_matrix[i][j] = min(graph_matrix[i][j], graph_matrix[i][k] + graph_matrix[k][j])

def floyd_warshall_path(parents, start_node, end_node):
    path = []
    parent = parents[start_node][end_node]
    while parent is not None:
        path.insert(0, parent)
        parent = parents[start_node][parent]

def main():
    current_graph = graph_data.graph_data[1]
    print(create_adj_matrix_from_list(current_graph))

main()

