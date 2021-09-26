from Graph import Graph

graph = Graph(name='V')

for i in range(5):
    graph.add_node(i)

graph.connect(2, 3)
graph.connect(1, 2)
graph.connect(3, 4)
graph.print()

graph.node_duplication(2)

graph.print()
