import graph_data 
import permutation
import math
import sys

def check_hamiltonian_cycle(permutations, graph):
    valid_cycles = []
    for permutation in permutations:
        # Checks to see if each node is connected to the next
        valid = True
        for index in range(len(permutation) - 1):
            if permutation[index + 1] not in graph[permutation[index]][1]:
                valid = False 
        if permutation[len(permutation) - 1] not in graph[permutation[0]][1]:
             valid = False
        if valid:
            valid_cycles.append(permutation)
    if len(valid_cycles) == 0:
        return False
    else: 
        return valid_cycles
    
def euclidian_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2) 

def optimal_hamiltonian_cycle(valid_cycles, graph):
    if valid_cycles == False:
        return False
    minimal_distance = sys.maxsize 
    optimal_paths = []
    for valid_cycle in valid_cycles:
        cycle_distance = 0
        for i in range(len(valid_cycle) - 1):
            cycle_distance += euclidian_distance(graph[valid_cycle[i]][0], graph[valid_cycle[i + 1]][0])
        cycle_distance += euclidian_distance(graph[valid_cycle[0]][0], graph[valid_cycle[len(valid_cycle) - 1]][0])
        if math.isclose(cycle_distance, minimal_distance):
            optimal_paths.append(valid_cycle)
        if cycle_distance < minimal_distance:
            minimal_distance = cycle_distance
            optimal_paths = [valid_cycle]
    return optimal_paths

def main():
    current_graph = graph_data.graph_data[4]
    permutations = permutation.SJT_algorithm(current_graph)
    print(check_hamiltonian_cycle(permutations, current_graph))

main()

