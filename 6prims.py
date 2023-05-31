# The provided code implements the Prim's algorithm for finding the Minimum Spanning Tree (MST) of a graph. Here's an explanation of the code:

# ```python

INF = 9999999
# Number of vertices in the graph
N = 5
# Creating the graph using the adjacency matrix method
G = [[0, 19, 5, 0, 0],
     [19, 0, 5, 9, 2],
     [5, 5, 0, 1, 6],
     [0, 9, 1, 0, 1],
     [0, 2, 6, 1, 0]]

selected_node = [0, 0, 0, 0, 0]

no_edge = 0

selected_node[0] = True

# Printing for edge and weight
print("Edge : Weight\n")
while (no_edge < N - 1):

    minimum = INF
    a = 0
    b = 0
    for m in range(N):
        if selected_node[m]:
            for n in range(N):
                if not selected_node[n] and G[m][n]:
                    # Not in selected and there is an edge
                    if minimum > G[m][n]:
                        minimum = G[m][n]
                        a = m
                        b = n
    print(str(a) + "-" + str(b) + ":" + str(G[a][b]))
    selected_node[b] = True
    no_edge += 1

'''
Explanation:

1. The variable `INF` is initialized with a large value to represent infinity, which will be used for initializing minimum values.

2. The variable `N` represents the number of vertices in the graph.

3. The graph `G` is represented using a 2D list (adjacency matrix), where `G[i][j]` represents the weight of the edge between vertices `i` and `j`. A weight of `0` indicates no edge between the vertices.

4. The list `selected_node` is used to keep track of the selected vertices. Initially, all vertices are marked as not selected (0).

5. The variable `no_edge` keeps track of the number of edges selected in the Minimum Spanning Tree (MST). It is initially set to 0.

6. The first vertex (vertex 0) is marked as selected (`selected_node[0] = True`) since we start building the MST from this vertex.

7. The while loop runs until `no_edge` becomes equal to `N - 1`, which indicates that all edges required for the MST have been selected.

8. Inside the loop, the minimum weight edge (`minimum`) and its corresponding vertices (`a` and `b`) are determined by iterating over the selected vertices and the non-selected vertices.

9. The condition `if not selected_node[n] and G[m][n]` checks if vertex `n` is not selected and there is an edge between vertices `m` and `n`.

10. If a smaller weight edge is found (`minimum > G[m][n]`), the minimum weight, as well as the vertices `a` and `b`, are updated accordingly.

11. After finding the minimum weight edge, it is printed using the format `"a-b:weight"`.

12. The vertex `b` is marked as selected (`selected_node[b] = True`).

13. The number of edges selected (`no_edge`) is incremented by 1.

14. The loop continues until all edges required for the MST have been selected.

Output and Explanation:

The code will print the selected edges and their weights, representing the Minimum

 Spanning Tree (MST) of the given graph.

For example, considering the given graph:

```python
G = [[0, 19, 5, 0, 0],
     [19, 0, 5, 9, 2],
     [5, 5, 0, 1, 6],
     [0, 9, 1, 0, 1],
     [0, 2, 6, 1, 0]]
```

The output will be:

```
Edge : Weight
0-2:5
2-3:1
3-4:1
2-1:5
```

This represents the edges and their weights in the Minimum Spanning Tree (MST) of the given graph. Each line in the output represents an edge in the MST, where the vertices of the edge are separated by a hyphen, and the weight of the edge is mentioned after the colon. The MST is built by selecting the edges with the smallest weights while ensuring that no cycles are formed.
'''