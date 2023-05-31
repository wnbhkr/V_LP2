# The provided code implements Dijkstra's algorithm to find the shortest path from a given starting node to all other nodes in a graph. Here's the code with comments explaining each line:

# ```python
from numpy import Inf

def Dijkstra(graph, start):
    l = len(graph)

    # initialize all node distances as infinite
    dist = [Inf for i in range(l)]

    # set the distance of starting node as 0
    dist[start] = 0

    # create a list that indicates if a node is visited or not
    vis = [False for i in range(l)]

    # iterate over all the nodes
    for i in range(l):

        # set u=-1 to indicate a current starting node
        u = -1

        # iterate over all the nodes to check the status of the visit
        for x in range(l):
            # now if the 'x' node is not visited yet or the distance we have currently for it is less than the distance to the start node then update the current node as the 'x'
            if not vis[x] and (u == -1 or dist[x] < dist[u]):
                u = x

        # check if we have visited all the nodes or we haven't reached the node
        if dist[u] == Inf:
            break

        # set the currently running node as visited
        vis[u] = True

        # now if the distance of the current node + the distance to the node we're visiting is less than the prior distance of the node we're visiting then update that distance.
        for v, d in graph[u]:
            if dist[u] + d < dist[v]:
                dist[v] = dist[u] + d

    # now at last return the list which contains the shortest path to each node from that given node
    return dist

# Define the graph as a dictionary
graph = {
    0: [(1, 1)],
    1: [(0, 1), (2, 2), (3, 3)],
    2: [(1, 2), (3, 1), (4, 5)],
    3: [(1, 3), (2, 1), (4, 1)],
    4: [(2, 5), (3, 1)]
}

# Call the Dijkstra's algorithm function with the graph and starting node
distances = Dijkstra(graph, 0)

# Print the shortest path distances to each node from the starting node
print(distances)

'''

The code defines a function `Dijkstra` that takes a graph represented as a dictionary and a starting node as input. It initializes the distance list with infinite values, sets the distance of the starting node to 0, and creates a list to track visited nodes.

The algorithm then iterates over all nodes to find the node with the minimum distance that has not been visited yet. It updates the current node as the one with the smallest distance and marks it as visited. It then updates the distances of its neighboring nodes if a shorter path is found.

Finally, the function returns the list of distances, representing the shortest path from the starting node to all other nodes.

I can describe the graph to you or provide you with a textual representation of it. Here's the textual representation of the graph you provided:

```
0: [(1, 1)]
1: [(0, 1), (2, 2), (3, 3)]
2: [(1, 2), (3, 1), (4, 5)]
3: [(1, 3), (2, 1), (4, 1)]
4: [(2, 5), (3, 1)]
```

Each number represents a node in the graph, and the tuples inside the brackets represent the edges connecting the nodes. The first value in each tuple represents the node being connected to, and the second value represents the weight of the edge.

If you would like, I can provide more information about the graph or assist you with any specific questions you have about it.
For the provided example, the output will be:

```
[0, 1, 3, 4, 5]
```

This means that the shortest path distances from node 0 to all other nodes are as follows:
- Distance from node 0 to node 0: 0
- Distance from node 0 to node 1: 1
- Distance from node 0 to node 2: 3
- Distance from node 0 to node 3: 4


- Distance from node 0 to node 4: 5
'''


'''
#swayam code
import sys


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight

    def dijkstra(self, src):
        distance = [sys.maxsize] * self.vertices
        distance[src] = 0
        visited = [False] * self.vertices

        for _ in range(self.vertices):
            min_dist = sys.maxsize
            min_index = -1

            for v in range(self.vertices):
                if not visited[v] and distance[v] < min_dist:
                    min_dist = distance[v]
                    min_index = v

            visited[min_index] = True

            for v in range(self.vertices):
                if (
                    not visited[v]
                    and self.graph[min_index][v] != 0
                    and distance[min_index] + self.graph[min_index][v] < distance[v]
                ):
                    distance[v] = distance[min_index] + self.graph[min_index][v]

        self.print_solution(distance)

    def print_solution(self, distance):
        print("Vertex \tDistance from Source")
        for v in range(self.vertices):
            print(f"{v} \t\t{distance[v]}")


# Example usage
if __name__ == "__main__":
    graph = Graph(5)

    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 2, 8)
    graph.add_edge(1, 2, 8)
    graph.add_edge(1, 3, 11)
    graph.add_edge(2, 3, 7)
    graph.add_edge(2, 4, 2)
    graph.add_edge(3, 4, 4)
 
    graph.dijkstra(0)
'''
'''
This code implements Dijkstra's algorithm for finding the shortest path in a graph. Here's a breakdown of the code:

1. The code defines a class named `Graph`, which has an `__init__` method to initialize the graph with the given number of vertices. It also has methods to add an edge between two vertices and to perform Dijkstra's algorithm.

2. The `add_edge` method takes three arguments: `u`, `v`, and `weight`, which represent the vertices and weight of the edge between them. It updates the adjacency matrix of the graph with the given edge information.

3. The `dijkstra` method performs Dijkstra's algorithm to find the shortest path from a given source vertex to all other vertices in the graph. It initializes the distance array with a large value for all vertices except the source, which is set to 0. It also maintains a visited array to keep track of visited vertices.

4. The algorithm iterates `self.vertices` number of times to process all vertices. In each iteration, it selects the vertex with the minimum distance that has not been visited yet. It updates the visited array and explores its adjacent vertices.

5. For each unvisited adjacent vertex, if the distance to reach that vertex through the current vertex is shorter than its current distance, it updates the distance. This process continues until all vertices have been visited.

6. The `print_solution` method is used to print the resulting distances from the source vertex to all other vertices.

7. In the example usage section, an instance of the `Graph` class is created with 5 vertices. Edges are added between vertices using the `add_edge` method. Finally, Dijkstra's algorithm is applied with a source vertex of 0 using the `dijkstra` method.

8. The output of the program will be the vertex numbers and their corresponding distances from the source vertex.

Example output:
```
Vertex   Distance from Source
0        0
1        4
2        8
3        19
4        10
```

In this example, the graph has 5 vertices and the distances from the source vertex (0) to all other vertices are calculated using Dijkstra's algorithm. The shortest distances are printed as output.
'''