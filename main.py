from random import randint
from Graph import Graph

graph1 = Graph(name='V')

for i in range(10):
    graph1.add_node(i)

for _ in range(10):
    graph1.connect(randint(0, 5), randint(0, 5))

graph1.print()
print(graph1.dfs(0))
