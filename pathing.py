import graph_data
import global_game_data
from numpy import random

def set_current_graph_paths():
    global_game_data.graph_paths.clear()
    global_game_data.graph_paths.append(get_test_path())
    global_game_data.graph_paths.append(get_random_path())
    global_game_data.graph_paths.append(get_dfs_path())
    global_game_data.graph_paths.append(get_bfs_path())
    global_game_data.graph_paths.append(get_dijkstra_path())


def get_test_path():
    return graph_data.test_path[global_game_data.current_graph_index]

# Gets a random node. Nodes that have not been visited will be given priority over visited nodes.  
def get_random_node(current_graph, current_node_index):
    node_options = current_graph[current_node_index][1]
    random_node_index = random.randint(0, len(node_options))
    return node_options[random_node_index]


def get_random_path():
    current_graph = graph_data.graph_data[global_game_data.current_graph_index]
    random_path_nodes = []
    
    target_node_index = global_game_data.target_node[global_game_data.current_graph_index]
    exit_node_index = len(current_graph) - 1
        
    target_found = False
    exit_found = False
    
    random_path_nodes.append(0)
    current_node_index = 0
    while ((target_node_index not in random_path_nodes) or (random_path_nodes[len(random_path_nodes) - 1] != exit_node_index)):
        current_node_index = get_random_node(current_graph, current_node_index)
        random_path_nodes.append(current_node_index)
    
    return random_path_nodes
    


def get_dfs_path():
    return [1,2]


def get_bfs_path():
    return [1,2]


def get_dijkstra_path():
    return [1,2]
