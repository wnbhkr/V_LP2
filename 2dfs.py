graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=' ')  # Print the current node
        visited.add(node)  # Mark the current node as visited

        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)  # Recursively call dfs for unvisited neighboring nodes

dfs(visited, graph, 'B')  # Start DFS from node 'B'


'''
Here's a breakdown of the code with comments:

Define the graph using a dictionary, where each key represents a node and the corresponding value is a list of its neighboring nodes.

Create an empty set called visited to keep track of visited nodes.

Define the dfs function that takes the visited set, graph, and node as parameters.

Check if the node is not in the visited set. If it is not visited:

Print the current node to display the order of traversal.
Add the current node to the visited set to mark it as visited.
Iterate over each neighbour in the list of neighbors of the current node.

For each unvisited neighbour, recursively call the dfs function with the visited set, graph, and the neighbour as parameters. This allows traversal to continue to the unvisited neighboring nodes in a depth-first manner.

Call the dfs function with the visited set, graph, and the starting node 'B'.

This code performs a depth-first search (DFS) traversal starting from the node 'B' in the given graph and prints the nodes in the order they are visited.
'''