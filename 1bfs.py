from collections import deque

# Define the graph using a dictionary
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def bfs(graph, start_node):
    visited = []  # List to store visited nodes
    queue = deque()  # Queue to store nodes to be visited

    visited.append(start_node)  # Mark the start node as visited
    queue.append(start_node)  # Add the start node to the queue

    while queue:
        node = queue.popleft()  # Remove and return the leftmost node from the queue
        print(node, end=" ")  # Print the current node

        neighbors = graph[node]  # Get the neighbors of the current node

        for neighbor in neighbors:
            if neighbor not in visited:
                visited.append(neighbor)  # Mark the neighbor as visited
                queue.append(neighbor)  # Add the neighbor to the queue

# Call the BFS function with the graph and the starting node
bfs(graph, 'B')


'''
Here's a breakdown of the code with comments:

Import the deque class from the collections module. It is used to create a queue efficiently.

Define the graph using a dictionary, where each key represents a node and the corresponding value is a list of its neighboring nodes.

Define the bfs function that takes the graph and start_node as parameters.

Initialize an empty visited list to keep track of visited nodes.

Create an empty queue using the deque class from collections to store the nodes to be visited.

Mark the start_node as visited by adding it to the visited list and enqueue it by adding it to the queue.

Enter a while loop that continues until the queue is empty.

Remove the leftmost node from the queue using the popleft() method and assign it to the variable node.

Print the current node to display the order of traversal.

Get the neighboring nodes of the current node from the graph dictionary and assign them to the neighbors variable.

Iterate over each neighbor in neighbors.

If the neighbor has not been visited, mark it as visited by adding it to the visited list and enqueue it by adding it to the queue.

After the BFS is complete and the queue is empty, the function will exit.

Call the bfs function with the graph and the starting node 'B'.

This code performs a breadth-first search traversal starting from the node 'B' in the given graph and prints the nodes in the order they are visited.
'''