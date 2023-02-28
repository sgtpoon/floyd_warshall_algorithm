#The Purpose is to test if Recursive function will fail or not.
import unittest
from Recursive import floyd_warshall_recursive
# test case will be implemented
class TestFloydWarshall(unittest.TestCase):

    def test_floyd_warshall_recursive(self):
        # Test case 1: Graph with 4 vertices
        graph = [[0, 5, INF, 10],
                 [INF, 0, 3, INF],
                 [INF, INF, 0, 1],
                 [INF, INF, INF, 0]]
        dist = graph
        expected = [[0, 5, 8, 9],
                    [INF, 0, 3, 4],
                    [INF, INF, 0, 1],
                    [INF, INF, INF, 0]]
        self.assertEqual(floyd_warshall_recursive(graph, dist), expected)

        # Test case 2: Graph with 3 vertices
        graph = [[0, 2, INF],
                 [INF, 0, 1],
                 [INF, INF, 0]]
        dist = graph
        expected = [[0, 2, 3],
                    [INF, 0, 1],
                    [INF, INF, 0]]
        self.assertEqual(floyd_warshall_recursive(graph, dist), expected)

        # Test case 3: Graph with 5 vertices
        graph = [[0, 1, INF, INF, INF],
                 [INF, 0, 2, INF, 4],
                 [INF, INF, 0, 3, INF],
                 [INF, INF, INF, 0, 5],
                 [INF, INF, INF, INF, 0]]
        dist = graph
        expected = [[0, 1, 3, 6, 10],
                    [INF, 0, 2, 5, 4],
                    [INF, INF, 0, 3, 7],
                    [INF, INF, INF, 0, 5],
                    [INF, INF, INF, INF, 0]]
        self.assertEqual(floyd_warshall_recursive(graph, dist), expected)

    if __name__ == '__main__':
        unittest.main(argv=['first-arg-is-ignored'], exit=False)
