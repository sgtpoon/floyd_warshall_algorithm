# Number of vertices in the graph
V = 4

# Define infinity as the large
# enough value. This value will be
# used for vertices not connected to each other
INF = 99999

graph = [
    [0, 5, INF, 10],
    [INF, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
    ]
dist = list(map(lambda i: list(map(lambda j: j, i)), graph))

# Solves all pair shortest path
# via Floyd Warshall Algorithm
def floyd_warshall_imperative (graph,dist):
    for k in range(V):

        # pick all vertices as source one by one
        for i in range(V):

            # Pick all vertices as destination
            # for the above picked source
            for j in range(V):
                # If vertex k is on the shortest path from
                # i to j, then update the value of dist[i][j]
                dist[i][j] = min(dist[i][j],
                                 dist[i][k] + dist[k][j]
                                 )
    return dist

# A utility function to print the solution
def print_solution(dist):
    print("Following matrix shows the shortest distances\
between every pair of vertices")
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


    print_solution(floyd_warshall_imperative(graph, dist))

