import graph_data 
import permutation

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
    return valid_cycles
    

def main():
    current_graph = graph_data.graph_data[4]
    permutations = permutation.SJT_algorithm(current_graph)
    print(check_hamiltonian_cycle(permutations, current_graph))

main()

