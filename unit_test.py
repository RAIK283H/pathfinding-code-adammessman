import math
import unittest
import graph_data
import pathing
import permutation
import main_no_pyglet


class TestPathFinding(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('test'.upper(), 'TEST')

    def test_isupper(self):
        self.assertTrue('TEST'.isupper())
        self.assertFalse('Test'.isupper())

    def test_floating_point_estimation(self):
        first_value = 0
        for x in range(1000):
            first_value += 1/100
        second_value = 10
        almost_pi = 3.1
        pi = math.pi
        self.assertNotEqual(first_value,second_value)
        self.assertAlmostEqual(first=first_value,second=second_value,delta=1e-9)
        self.assertNotEqual(almost_pi, pi)
        self.assertAlmostEqual(first=almost_pi, second=pi, delta=1e-1)

    def test_create_dfs_path_to_target_happy(self):
        current_graph  = graph_data.graph_data[3]
        start_index =  0
        target_index = 2
        expected = [0, 4, 8, 12, 13, 9, 5, 1, 2]
        actual = pathing.dfs_path_until_found(start_index, current_graph, target_index)
        self.assertEqual(expected, actual, 'Path for DFS is not accurate.')

    def test_create_dfs_path_to_target_back_track(self):
        current_graph  = graph_data.graph_data[7]
        start_index =  0
        target_index = 5
        expected = [0, 8, 9, 7, 9, 6, 9, 5]
        actual = pathing.dfs_path_until_found(start_index, current_graph, target_index)
        self.assertEqual(expected, actual, 'Path with DFS back tracking is not accurate.')

    def test_create_dfs_path_to_target_happy(self):
        current_graph  = graph_data.graph_data[3]
        start_index =  0
        target_index = 2
        expected = [1, 2]
        actual = pathing.bfs_path_until_found(start_index, current_graph, target_index)
        self.assertEqual(expected, actual, 'Path for BFS is not accurate.')

    def test_create_dfs_path_to_target_full_path(self):
        current_graph  = graph_data.graph_data[7]
        start_index =  0
        target_index = 5
        exit_index = len(current_graph) - 1
        expected = [5, 9]
        actual = pathing.bfs_path_until_found(start_index, current_graph, target_index) + pathing.bfs_path_until_found(target_index, current_graph, exit_index)
        self.assertEqual(expected, actual, 'Path with BFS back tracking is not accurate.')

    def test_find_largest_mobile_start(self):
        list = [-1, -2, -3, -4, -5]
        expected = 4
        actual = permutation.find_largest_mobile(list)
        self.assertEqual(expected, actual, 'The largest mobile element was not properly found.')

    def test_find_largest_mobile_w_highest(self):
        list = [-1, 5, 2, -3, 4]
        expected = 1
        actual = permutation.find_largest_mobile(list)
        self.assertEqual(expected, actual, 'The largest mobile element was not properly found.')

    def test_find_largest_mobile_w_highest_at_edge(self):
        list = [-4, -1, 2, -3, 5]
        expected = 3
        actual = permutation.find_largest_mobile(list)
        self.assertEqual(expected, actual, 'The largest mobile element was not properly found.')

    def test_find_largest_mobile_no_mobile(self):
        list = [-5, -4, -3, -2, -1]
        expected = -1
        actual = permutation.find_largest_mobile(list)
        self.assertEqual(expected, actual, 'The largest mobile element was not properly found.')

    def test_find_largest_w_correct_in_middle_second_last(self):
        list = [-1, -2, -5, -3, -4]
        expected = 2
        actual = permutation.find_largest_mobile(list)
        self.assertEqual(expected, actual, 'The largest mobile element was not properly found.')

    def test_permutation_of_three_nodes(self):
        graph = [[(0, 0), [1]], 
                 [(0, 1), [0, 2, 3]], 
                 [(0, 2), [1, 3]], 
                 [(2, 3), [1, 2, 4]], 
                 [(5, 0), [3]],
                 ]
        expected = [[1, 2, 3],
                [1, 3, 2],
                [3, 1, 2],
                [3, 2, 1], 
                [2, 3, 1], 
                [2, 1, 3], 
                ]
        actual = permutation.SJT_algorithm(graph)
        self.assertEqual(expected, actual, 'Permutations not found properly.')

    def test_valid_hamiltonian_cycle_all_valid(self):
        graph = [[(0, 0), [1]], 
                 [(0, 1), [0, 2, 3]], 
                 [(0, 2), [1, 3]], 
                 [(2, 3), [1, 2, 4]], 
                 [(5, 0), [3]],
                 ]
        expected = [[1, 2, 3],
                [1, 3, 2],
                [3, 1, 2],
                [3, 2, 1], 
                [2, 3, 1], 
                [2, 1, 3], 
                ]
        actual = main_no_pyglet.check_hamiltonian_cycle(permutation.SJT_algorithm(graph), graph)
        self.assertEqual(expected, actual, 'Hamiltonian cycles not found properly.')

    def test_valid_hamiltonian_cycle_none_valid(self):
        graph = [[(0, 0), [1]], 
                 [(0, 1), [0, 2]], 
                 [(0, 2), [1, 3]], 
                 [(2, 3), [2, 4]], 
                 [(5, 0), [3]],
                 ]
        expected = False
        actual = main_no_pyglet.check_hamiltonian_cycle(permutation.SJT_algorithm(graph), graph)
        self.assertEqual(expected, actual, 'Hamiltonian cycles not found properly.')

    def test_switch_direction_if_greater_happy(self):
        list = [1, 2, 3, 4, 5]
        threshold = 3
        expected = [1, 2, 3, -4, -5]
        actual = permutation.switch_directions_if_greater(list, threshold)
        self.assertEqual(expected, actual, 'Switch signs function if greater than threshold did not happen properly.')

    
    def test_switch_direction_if_greater_happy(self):
        list = [-1, 2, -3, -4, 5]
        threshold = -3
        expected = [-1, 2, -3, 4, -5]
        actual = permutation.switch_directions_if_greater(list, threshold)
        self.assertEqual(expected, actual, 'Switch signs function if greater than threshold did not happen properly.')

    def test_make_positive(self):
        list = [-1, 2, -3, -4, 5]
        expected = [1, 2, 3, 4, 5]
        actual = permutation.make_positive(list)
        self.assertEqual(expected, actual, 'Not all numbers were positive.')

    def test_opitmal_paths(self):
        graph = [[(0, 0), [1]], 
                 [(0, 1), [0, 2, 3]], 
                 [(0, 2), [1, 3]], 
                 [(2, 3), [1, 2, 4]], 
                 [(5, 0), [3]],
                 ]
        expected = [[1, 2, 3],
                [1, 3, 2],
                [3, 1, 2],
                [3, 2, 1], 
                [2, 3, 1], 
                [2, 1, 3], 
                ]
        valid_cycles = main_no_pyglet.check_hamiltonian_cycle(permutation.SJT_algorithm(graph), graph)
        print(valid_cycles)
        actual = main_no_pyglet.optimal_hamiltonian_cycle(valid_cycles, graph)
        self.assertEqual(expected, actual, 'Optimal paths not provided.')

        


if __name__ == '__main__':
    unittest.main()
