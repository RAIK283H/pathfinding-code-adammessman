# Pathfinding Starter Code

I interpreted the random path the mean that the player should be able to visit a node it has visited before in order to avoid the player getting stuck in an infinite loop. I also interpreted this to mean that the player should be able to go back to the start node and back and forth between nodes to maintain a higher degree of randomness. The player should be able to visit the exit node, even without visiting the target node. 

The statisic that I added was the multiple of the optimal/direct distance. This statistic is updated as the other statistics are updated. If the player goes 2560 units and the distance of the direct distance is 1000 units, the multiple will be 2.560. 

EXTRA CREDIT A* HEURISTIC: I added the euclidian distance from the current node to the target node as the heuristic for A*. 

HOMEWORK 7 EXTRA CREDIT: I switched out the Dijkstra player and make it a Floyd-Warshall. I did so by changing two classes: pathing.py and config_data.py. In the config_data.py, I simply changed the player_data to reflect the name of the Floyd-Warshall player. In the pathing.py file, I changed the set_current_graph_paths function to append a custom function for the F-W Algorithm instead of Dijkstra's. I added this custom function, using the f_w.py functions, to the bottom of the pathing.py file.  