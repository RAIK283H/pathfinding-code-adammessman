import math
import unittest
import graph_data
import pathing


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

    # TODO: UNIT TEST BFS


if __name__ == '__main__':
    unittest.main()
