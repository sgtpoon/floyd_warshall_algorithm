# Floyd Warshall Algorithm - Recursive Version

This is a Python implementation of the Floyd Warshall Algorithm using recursion. The algorithm finds the shortest distances between every pair of vertices in a weighted graph.

## Usage

To use this algorithm, simply define the graph as a 2D array where each element represents the weight of the edge between two vertices. The `V` variable should be set to the number of vertices in the graph.

```python
# Number of vertices in the graph
V = 4

# Define infinity as the large enough value. This value will be
# used for vertices not connected to each other.
INF = 99999

# Define the graph as a 2D array
graph = [[0, 7, INF, 8],
         [INF, 0, 5, INF],
         [INF, INF, 0, 2],
         [INF, INF, INF, 0]
         ]
```

To find the shortest distances between every pair of vertices, call the `floyd_warshall_recursive` function with the graph and an initial distance matrix as arguments:

```python
# Initialize the distance matrix to the graph.
dist = graph

# Print the solution
print_solution(floyd_warshall_recursive(graph, dist))
```

The `print_solution` function will output the shortest distances between every pair of vertices:

```
Following matrix shows the shortest distances between every pair of vertices:
  0      7      12      8
  INF    0      5       10
  INF    INF    0       2
  INF    INF    INF     0
```

## Algorithm Details

The Floyd Warshall Algorithm is used to find the shortest distances between every pair of vertices in a weighted graph. It works by iteratively updating a distance matrix with the shortest distances between pairs of vertices.

The algorithm uses a dynamic programming approach to find the shortest paths. It considers all possible intermediate vertices in the paths and selects the shortest path between each pair of vertices.

The algorithm has a time complexity of O(V^3), where V is the number of vertices in the graph. Since the algorithm considers all possible pairs of vertices and intermediate vertices, it is not suitable for large graphs with many vertices.
![image](https://user-images.githubusercontent.com/125120849/221698680-150d3c53-3778-46fe-b68d-9fb8eb4c0e2f.png)
