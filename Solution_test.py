#Solution test is to test the values inside the matrix, shortest distances between every pair of vertices:
import unittest
from Recursive import print_solution

def test_print_solution(self):
        # Test case 1: 3x3 matrix with INF values
        dist = [[0, INF, INF],
                [INF, 0, INF],
                [INF, INF, 0]]
        expected = """Following matrix shows the shortest distances between every pair of vertices:
      0	    INF	    INF	
    INF	      0	    INF	
    INF	    INF	      0	
"""
        self.assertEqual(print_solution(dist), expected)

        # Test case 2: 3x3 matrix with non-INF values
        dist = [[0, 2, 3],
                [INF, 0, 1],
                [INF, INF, 0]]
        expected = """Following matrix shows the shortest distances between every pair of vertices:
      0	      2	      3	
    INF	      0	      1	
    INF	    INF	      0	
"""
        self.assertEqual(print_solution(dist), expected)

        # Test case 3: 4x4 matrix with non-INF values
        dist = [[0, 5, 8, 9],
                [INF, 0, 3, 4],
                [INF, INF, 0, 1],
                [INF, INF, INF, 0]]
        expected = """Following matrix shows the shortest distances between every pair of vertices:
      0	      5	      8	      9	
    INF	      0	      3	      4	
    INF	    INF	      0	      1	
    INF	    INF	    INF	      0	
"""
        self.assertEqual(print_solution(dist), expected)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
