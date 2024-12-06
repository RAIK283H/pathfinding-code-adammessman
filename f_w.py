import graph_data
import math
import sys


def euclidian_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Creates n x n matrix, where n is size of the graph
def create_blank_matrix(graph):
    matrix = [sys.maxsize] * len(graph)
    for i in range(len(matrix)):
        matrix[i] = [sys.maxsize] * len(matrix)
    return matrix

# Converts adjacency list to adjacency matrix
def create_adj_matrix_from_list(graph):
    # Creates the inital matrix with -1 as default value signifying no path between nodes
    # In case of direction: 
    # matrix[a] = matrix the node is coming from
    # matrix[a][b] = node a to node b, (row a, column b)
    # matrix[b][a] = node b to node a, (row b, column a)
    matrix = create_blank_matrix(graph)

    for index in range(len(graph)):
        node_coords = graph[index][0]
        adjaceny_list = graph[index][1]
        for adj_node in adjaceny_list:
                adj_node_coords = graph[adj_node][0]
                edge_weight = euclidian_distance(node_coords, adj_node_coords)
                matrix[index][adj_node] = edge_weight

    return matrix

# Floyd-Warshall Algo
def floyd_warshall_algorithm(graph_matrix, parents):
     for k in range(len(graph_matrix)):
          for i in range(len(graph_matrix)):
               for j in range(len(graph_matrix)):
                    if (graph_matrix[i][k] + graph_matrix[k][j] < graph_matrix[i][j]):
                        graph_matrix[i][j] = graph_matrix[i][k] + graph_matrix[k][j]
                        parents[i][j] = k

# Reconstructs the paths              
def floyd_warshall_path(parents, start_node, end_node):
    path = []
    parent = parents[start_node][end_node]
    while parent is not sys.maxsize:
        path.insert(0, parent)
        parent = parents[start_node][parent]
    path.insert(0, start_node)
    path.append(end_node)
    return path

def main():
    # Initializes needed data
    current_graph = graph_data.graph_data[3]
    start_node_index = 0
    end_node_index = len(current_graph) - 1

    # Initializes the needed matricies 
    matrix = create_adj_matrix_from_list(current_graph)
    parents = create_blank_matrix(current_graph)

    # Runs Flyod-Warshall Algo
    floyd_warshall_algorithm(matrix, parents)
    print(floyd_warshall_path(parents, start_node_index, end_node_index))

main()

