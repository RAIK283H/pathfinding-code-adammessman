import graph_data
import global_game_data
from numpy import random
import heapq 
import math

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
    # Inline assert statements for preconditions, such as graph needs to exist and we need to have been given a target (that exists in graph) 
    assert graph_data.graph_data[global_game_data.current_graph_index] is not None, "Graph does not exist."
    assert graph_data.graph_data[global_game_data.current_graph_index][global_game_data.target_node[global_game_data.current_graph_index]] is not None, "Target does not exist in the graph."

    current_graph = graph_data.graph_data[global_game_data.current_graph_index]
    random_path_nodes = []
    
    target_node_index = global_game_data.target_node[global_game_data.current_graph_index]
    exit_node_index = len(current_graph) - 1
        
    random_path_nodes.append(0)
    current_node_index = 0
    while ((target_node_index not in random_path_nodes) or (random_path_nodes[len(random_path_nodes) - 1] != exit_node_index)):
        current_node_index = get_random_node(current_graph, current_node_index)
        random_path_nodes.append(current_node_index)
    
    # Inline assert statements for postconditions, such as list of nodes needs to include end and target, last node needs to be ending node
    assert target_node_index in random_path_nodes, "The target node is missing from the path."
    assert exit_node_index in random_path_nodes, "The exit node is missing from the path."
    assert random_path_nodes[len(random_path_nodes) - 1] == exit_node_index, "The last node is not the exit node."

    return random_path_nodes
    


def dfs_path_until_found(start_index, current_graph, target_index):
    # Initializes the necessary structures
    path = []
    next_list = []
    next_list.append(start_index)

    visited = set()
    parents = {}

    # Loops until there is nothing in the stack or until a path is returned
    while next_list:
        current = next_list.pop(0)
        path.append(current)
        visited.add(current)
        adjacents = current_graph[current][1]
        # Returns path is target node is added
        if (current == target_index):
            return path
        # Traces back to parent if all of the adjacents are visited
        if all(element in visited for element in adjacents): 
            next_list.insert(0,parents[current])
        # Adds adjacents to the front of the stack if it has not been visited
        for i in range(len(adjacents)):
            adjacent = adjacents[i]
            if adjacent not in visited:
                parents[adjacent] = current
                next_list.insert(0, adjacent)

def get_dfs_path():

    # Sets travel nodes
    current_graph = graph_data.graph_data[global_game_data.current_graph_index]
    current_node_index = 0
    target_node_index = global_game_data.target_node[global_game_data.current_graph_index]
    exit_node_index = len(current_graph) - 1
    
    # Calls helper function to set path
    path = dfs_path_until_found(current_node_index, current_graph, target_node_index)
    path = path + dfs_path_until_found(target_node_index, current_graph, exit_node_index)

    # Postcondition Inline Testing
    assert target_node_index in path, 'Target Node Index is not in the path.'
    assert path[len(path) - 1] == exit_node_index, 'Path does not end at exit node.'
    for index in range(len(path) - 1):
        assert (path[index] in current_graph[path[index + 1]][1] or path[index] == path[index + 1]), 'Nodes are not connected by an edge.'

    return path

def bfs_path_until_found(start_index, current_graph, target_index):
    # Initializes the necessary structures
    path = []
    next_list = []
    next_list.append(start_index)

    visited = set()
    parents = {}
    parents[start_index] = None

    # Loops until there is nothing in the queue or until a path is returned
    while next_list:
        current = next_list.pop()
        visited.add(current)
        adjacents = current_graph[current][1]
        for i in range(len(adjacents)):
            adjacent = adjacents[i]
            if adjacent not in visited:
                next_list.insert(0, adjacent)
                parents[adjacent] = current
                # Returns path if target node is added
                if (adjacent == target_index):
                    current = adjacent
                    while parents[current] != None: 
                        path.insert(0, current)
                        current = parents[current]
                    return path
    return path

def get_bfs_path():

    current_graph = graph_data.graph_data[global_game_data.current_graph_index]
    current_node_index = 0
    target_node_index = global_game_data.target_node[global_game_data.current_graph_index]
    exit_node_index = len(current_graph) - 1

    path = bfs_path_until_found(current_node_index, current_graph, target_node_index)
    path  = path + bfs_path_until_found(target_node_index, current_graph, exit_node_index)

    # Postcondition Inline Testing
    assert target_node_index in path, 'Target Node Index is not in the path.'
    assert path[len(path) - 1] == exit_node_index, 'Path does not end at exit node.'
    for index in range(len(path) - 1):
        assert (path[index] in current_graph[path[index + 1]][1] or path[index] == path[index + 1]), 'Nodes are not connected by an edge.'

    return path

def euclidian_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2) 

def dijkstra_helper(current_graph, start_node_index, target_node_index):
    visited = set()

    frontier = []
    heapq.heapify(frontier)
    heapq.heappush(frontier, (0, start_node_index))
    parents = {}
    parents[start_node_index] = None

    while frontier:
        distance, current_node_index = heapq.heappop(frontier)
        current_node_coords = current_graph[current_node_index][0]
        if (current_node_index == target_node_index):
            # Return the path if target is found
            path = []
            while parents[current_node_index] != None: 
                path.insert(0, current_node_index)
                current_node_index = parents[current_node_index]

            print(path)
            
            return path
        neighbors = current_graph[current_node_index][1]
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                parents[neighbor] = current_node_index
                neighbor_coords = current_graph[neighbor][0]
                heapq.heappush(frontier, (distance + euclidian_distance(current_node_coords, neighbor_coords), neighbor))

    return

def get_dijkstra_path():

    # Sets travel nodes
    current_graph = graph_data.graph_data[global_game_data.current_graph_index]
    current_node_index = 0
    target_node_index = global_game_data.target_node[global_game_data.current_graph_index]
    exit_node_index = len(current_graph) - 1

    path = dijkstra_helper(current_graph, current_node_index, target_node_index)

    return path
