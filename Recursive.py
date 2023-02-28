#Floyd Warshall Algorithm recurisve version


# Number of vertices in the graph
V = 4

# Define infinity as the large enough value. This value will be
# used for vertices not connected to each other.
INF = 99999

# Recursive function to find the shortest distances
# between all pairs of vertices in the graph.
def floyd_warshall_recursive(graph, dist):
    # Base case: if there are no intermediate vertices,
    # the distance matrix is already the solution.
    if len(graph) == 0:
        return dist

    # Create a new distance matrix to store the updated
    # distances for this iteration.
    new_dist = [[0] * V for i in range(V)]

    # Iterate over all pairs of vertices.
    for i in range(V):
        for j in range(V):
            # Initialize the minimum distance to the current
            # distance between i and j.
            min_dist = dist[i][j]

            # Iterate over all possible intermediate vertices.
            for k in range(V):
                # If vertex k is on the shortest path from i to j,
                # update the minimum distance.
                if dist[i][k] + dist[k][j] < min_dist:
                    min_dist = dist[i][k] + dist[k][j]

            # Update the distance matrix with the minimum distance.
            new_dist[i][j] = min_dist

    # Recursively call the function with the new distance matrix.
    return floyd_warshall_recursive(graph[1:], new_dist)

# A utility function to print the solution.
def print_solution(dist):
    print("Following matrix shows the shortest distances "
          "between every pair of vertices:")
    for i in range(V):
        for j in range(V):
            if dist[i][j] == INF:
                print("%7s" % ("INF"), end=" ")
            else:
                print("%7d\t" % (dist[i][j]), end=' ')
            if j == V - 1:
                print()

# Driver's code
if __name__ == "__main__":
    """
                10
            (0)------->(3)
            |         /|\\
            5 |          |
            |         | 1
            \|/         |
            (1)------->(2)
                3
    """
    graph = [[0, 7, INF, 8],
             [INF, 0, 5, INF],
             [INF, INF, 0, 2],
             [INF, INF, INF, 0]
             ]

    # Initialize the distance matrix to the graph.
    dist = graph

    # Print the execution and the solution.

    print_solution(floyd_warshall_recursive(graph, dist))
