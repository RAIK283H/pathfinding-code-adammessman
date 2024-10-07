# Pathfinding Starter Code

I interpreted the random path the mean that the player should be able to visit a node it has visited before in order to avoid the player getting stuck in an infinite loop. I also interpreted this to mean that the player should be able to go back to the start node and back and forth between nodes to maintain a higher degree of randomness. The player should be able to visit the exit node, even without visiting the target node. 

The statisic that I added was the multiple of the optimal/direct distance. This statistic is updated as the other statistics are updated. If the player goes 2560 units and the distance of the direct distance is 1000 units, the multiple will be 2.560.  