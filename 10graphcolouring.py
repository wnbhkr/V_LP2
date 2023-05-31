def printConfiguration(colorArray):
    print("The assigned colors are as follows:")
    for i in range(4):
        print("Vertex: ",
              i, " Color: ", colorArray[i])



def isSafe(v, graph, colorArray, j):
    for i in range(4):
        if graph[v][i] == 1 and j == colorArray[i]:
            return False
    return True



def graphColoringAlgorithm(graph, m, i, colorArray):
    if(i == 4):
        printConfiguration(colorArray)
        return True

    # Assigning color to the vertex and recursively calling the function.
    for j in range(1, m + 1):
        if isSafe(i, graph, colorArray, j):
            colorArray[i] = j
            if (graphColoringAlgorithm(graph, m, i + 1, colorArray)):
                return True
            colorArray[i] = 0
    return False



graph = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0],
]
m = 3

# Initially the color list is initialized with 0.
colorArray = [0 for i in range(4)]

if (graphColoringAlgorithm(graph, m, 0, colorArray)):
    print("Coloring is possible!")
else:
    print("Coloring is not possible!")

    '''
    The provided code implements a graph coloring algorithm using backtracking to assign colors to vertices of a graph. Here's the breakdown of the code:

```python
def printConfiguration(colorArray):
    print("The assigned colors are as follows:")
    for i in range(4):
        print("Vertex:", i, "Color:", colorArray[i])
```
The `printConfiguration` function is defined to print the assigned colors for each vertex. It takes `colorArray` as input, which represents the assigned colors for each vertex. It iterates through the vertices (4 in this case) and prints the vertex index along with its assigned color.

```python
def isSafe(v, graph, colorArray, j):
    for i in range(4):
        if graph[v][i] == 1 and j == colorArray[i]:
            return False
    return True
```
The `isSafe` function checks if it is safe to assign a color `j` to a vertex `v`. It takes the vertex index `v`, the adjacency matrix `graph`, the current `colorArray`, and the color `j` as input. It iterates through all vertices and checks if there is an edge between vertex `v` and vertex `i` (if `graph[v][i] == 1`). If an edge exists and the color of vertex `i` is the same as `j`, it means there would be a conflict in colors, and the function returns `False`. Otherwise, it returns `True`.

```python
def graphColoringAlgorithm(graph, m, i, colorArray):
    if i == 4:
        printConfiguration(colorArray)
        return True

    # Assigning color to the vertex and recursively calling the function.
    for j in range(1, m + 1):
        if isSafe(i, graph, colorArray, j):
            colorArray[i] = j
            if graphColoringAlgorithm(graph, m, i + 1, colorArray):
                return True
            colorArray[i] = 0
    return False
```
The `graphColoringAlgorithm` function is the main recursive function that performs the graph coloring algorithm. It takes the graph adjacency matrix `graph`, the number of colors `m`, the current vertex index `i`, and the `colorArray` as input. The base case is when `i` reaches the total number of vertices (4 in this case). At that point, it calls the `printConfiguration` function to display the assigned colors and returns `True`.

In the recursive part, it iterates through colors from 1 to `m`. For each color, it checks if it is safe to assign that color to the current vertex `i` using the `isSafe` function. If it is safe, the color is assigned to `colorArray[i]`, and the function is called recursively for the next vertex `i + 1`. If the recursive call returns `True`, it means a valid coloring solution is found, and the function returns `True`. If not, it resets the color of `colorArray[i]` back to 0 and continues to try other colors.

```python
graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0],
]
m = 3

# Initially, the color list is initialized with 0.
colorArray = [0 for i in range(4)]

if graphColoringAlgorithm(graph, m, 0, colorArray):
    print("Coloring is possible!")
else:
    print("Color

ing is not possible!")
```
In the main part of the code, an example graph is defined as an adjacency matrix `graph`. Each row and column represents a vertex, and a value of 1 in the matrix indicates an edge between the corresponding vertices. The number of colors `m` is set to 3.

A `colorArray` list is initialized with 0s, representing no colors assigned to any vertex yet.

The `graphColoringAlgorithm` function is called with the graph, number of colors, initial vertex index (`0`), and the colorArray. If a valid coloring solution is found, it prints "Coloring is possible!" Otherwise, it prints "Coloring is not possible!"

Now let's consider the output:

```
The assigned colors are as follows:
Vertex: 0 Color: 1
Vertex: 1 Color: 2
Vertex: 2 Color: 3
Vertex: 3 Color: 2
Coloring is possible!
```
The output shows the assigned colors for each vertex, and it indicates that a valid coloring solution is possible for the given graph. Each line represents a vertex, and the assigned color is displayed next to it.

I hope this explanation helps you understand the code and its output. If you have any further questions, feel free to ask!'''

'''
The provided code defines a graph using an adjacency matrix representation. Here's an explanation of the graph:

The variable `graph` represents a 4x4 matrix, where each row and column corresponds to a vertex in the graph. The value at position `[i][j]` in the matrix indicates whether there is an edge between vertex `i` and vertex `j`.

Let's break down the matrix:

```
graph = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0],
]
```

- Row 0: Vertex 0 is connected to vertices 1, 2, and 3. There are edges from vertex 0 to vertices 1, 2, and 3.
- Row 1: Vertex 1 is connected to vertices 0 and 2. There is an edge from vertex 1 to vertex 0 and from vertex 1 to vertex 2.
- Row 2: Vertex 2 is connected to vertices 0, 1, and 3. There are edges from vertex 2 to vertices 0, 1, and 3.
- Row 3: Vertex 3 is connected to vertices 0 and 2. There is an edge from vertex 3 to vertex 0 and from vertex 3 to vertex 2.

In summary, the graph can be visualized as follows:

```
0 -- 1
|  \/ |
|  /\ |
3 -- 2
```

Vertex 0 is connected to vertices 1, 2, and 3. Vertex 1 is connected to vertices 0 and 2. Vertex 2 is connected to vertices 0, 1, and 3. Vertex 3 is connected to vertices 0 and 2.

This graph represents a connected undirected graph with four vertices. The adjacency matrix indicates the presence or absence of edges between the vertices. In this case, the graph represents a symmetric graph since it is undirected. If an edge exists between vertex `i` and vertex `j`, there will be a corresponding edge between vertex `j` and vertex `i` in the adjacency matrix.'''