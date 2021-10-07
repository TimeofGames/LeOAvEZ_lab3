from random import randint
from Graph import Graph

graph = Graph(name="v")

for i in range(5):
    graph.add_node(i)

graph.connect(0,1)

graph.connect(2,1)
graph.connect(3,1)
graph.connect(4,0)

graph.print()
print(graph.bfs(graph.nodes[0]))