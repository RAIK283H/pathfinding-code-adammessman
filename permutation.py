
# Finds the largest mobile number from the current list of nodes
def find_largest_mobile(nodes):
    largest_mobile_index = 0
    largest_mobile_number = 0
    
    # Loops through to check if others are higher mobile
    for i in range(1, len(nodes) - 1):
        # Case if negative number
        if(nodes[i] < 0):
            if (abs(nodes[i]) > abs(largest_mobile_number)) and (abs(nodes[i]) > abs(nodes[i - 1])):
                largest_mobile_index = i
                largest_mobile_number = nodes[i]
        # Case if positive number
        else:
            if (nodes[i] > abs(largest_mobile_number)) and (nodes[i] > abs(nodes[i + 1])):
                largest_mobile_index = i
                largest_mobile_number = nodes[i]
    
    # Checks to see if last in list points left and is greater than current largest mobile 
    if (nodes[len(nodes) - 1] < 0) and (abs(nodes[len(nodes) - 1]) > abs(nodes[len(nodes) - 2])) and (abs(nodes[len(nodes) - 1]) > abs(largest_mobile_number)):
        largest_mobile_index = len(nodes) - 1
        largest_mobile_number = nodes[len(nodes) - 1]
    
    # Sets the largest to -1 if the first index in list is wrong
    if (largest_mobile_number == 0) and ((nodes[0] < 0) or (abs(nodes[0]) < abs(nodes[1]))):
        largest_mobile_index = -1
    return largest_mobile_index

    # Notes:
    # move first check to last, and still 0 in last case
    # make copy, then wipe negatives

def swap(list, index_to, index_from):
    temp = list[index_from]
    list[index_from] = list[index_to]
    list[index_to] = temp

# Switches the direction of nodes if are greater than the threshold
def switch_directions_if_greater(list, threshold):
    for i in range(len(list)):
        if abs(list[i]) > abs(threshold):
            list[i] = list[i] * -1 
    return list

# Makes the list positive to represent nodes
def make_positive(list):
    for i in range(len(list)):
        if list[i] < 0:
            list[i] = list[i] * -1
    return list


# Creates all of the permutations using the SJT algorithm
def SJT_algorithm(graph):
    cycle_nodes = []
    for i in range(1, len(graph) - 1):
        # Negative numbers represent left pointing, positive represents righ pointing 
        # All nodes start as left pointing
        cycle_nodes.append(i * -1)

    permutations = []
    permutations.append(make_positive(cycle_nodes.copy()))

    largest_mobile_index = find_largest_mobile(cycle_nodes) 
    while (largest_mobile_index != -1):
        # case if swapping left
        if (cycle_nodes[largest_mobile_index] > 0):
            swap(cycle_nodes, largest_mobile_index, largest_mobile_index + 1)
            switch_directions_if_greater(cycle_nodes, cycle_nodes[largest_mobile_index + 1])
        # case if swapping right
        else:
            swap(cycle_nodes, largest_mobile_index, largest_mobile_index - 1)
            switch_directions_if_greater(cycle_nodes, cycle_nodes[largest_mobile_index - 1])
        # Adds permutation to the overall list
        permutation = cycle_nodes.copy()
        permutations.append(make_positive(permutation).copy())
        
        largest_mobile_index = find_largest_mobile(cycle_nodes)
        
    return permutations
            
    