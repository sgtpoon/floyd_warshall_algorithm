import timeit
from Recursive import floyd_warshall_recursive
from website import floyd_warshall_imperative
# Number of vertices in the graph
V = 4

# Define infinity as the large enough value. This value will be
# used for vertices not connected to each other.
INF = 99999

# Define the test graph.
graph = [[0, 7, INF, 8],
         [INF, 0, 5, INF],
         [INF, INF, 0, 2],
         [INF, INF, INF, 0]]

# Initialize the distance matrix to the graph.
dist = graph

# Define the number of iterations for the timeit function.
num_iterations = 1000

# Time the execution of the function.
recursive_execution_time = timeit.timeit(lambda: floyd_warshall_recursive(graph, dist),
                               number = num_iterations)
imperative_execution_time = timeit.timeit(lambda: floyd_warshall_imperative(graph, dist),
                               number = num_iterations)

# If conditions needs to execute to explain which value is great.



# Print the execution time and the solution.
print(f"Recursive Execution time: {recursive_execution_time:.6f} seconds "
      f"for {num_iterations} iterations.")

print(f"Imperative Execution time: {imperative_execution_time:.6f} seconds "
      f"for {num_iterations} iterations.")

if imperative_execution_time > recursive_execution_time:
    print ("This Performance test suggest Imperative is faster")

elif imperative_execution_time == recursive_execution_time:
    print ("This Performance test suggest Imperative are the same")

else:
    print ("This Performance test suggest Imperative Execution is faster")