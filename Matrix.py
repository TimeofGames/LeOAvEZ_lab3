import Exceptions_Matrix
import Exceptions_Graph
import AdjacencyList


class Matrix():
    def __init__(self):
        self._row = 0
        self._col = 0
        self._nodes = []
        self._matrix = []

    def add_node(self, node):
        self._nodes.append(node)
        self._matrix_update(1)

    def _matrix_update(self, add_nodes):
        for i in self._matrix:
            for _ in range(add_nodes):
                i.append([])
        for i in range(add_nodes):
            self._matrix.append([[] for _ in range(len(self._nodes))])

    def del_node(self, node):
        self._nodes.pop(node.index)
        self._matrix.pop(node.index)
        for i in self._matrix:
            i.pop(node.index)

    def print(self):
        for node in self._nodes:
            print("   " + node.name, end="")
        print()
        for i in range(len(self._matrix)):
            print(str(self._nodes[i].name) + " " + str(self._matrix[i])[1:-1])

    def connect_dir(self, from_node, to_node, weight=1):
        self._matrix[from_node.index][to_node.index].append(weight)

    def disconnect_dir(self, from_node, to_node, weight=1):
        self._matrix[from_node.index][to_node.index].remove(weight)

    def convert_to_adj_list(self):
        adj_list = AdjacencyList.AdjacencyList()
        for i in self._nodes:
            adj_list.add_node(i)
        for i in range(len(self._matrix)):
            for j in range(i, len(self._matrix[i])):
                for k in self._matrix[i][j]:
                    adj_list.connect_dir(self._nodes[i], self._nodes[j], k)

        for i in range(len(self._matrix)):
            for j in range(0, i):
                for k in self._matrix[i][j]:
                    adj_list.connect_dir(self._nodes[i], self._nodes[j], k)
        return adj_list

    def node_association(self, from_node, to_node):
        for i in range(len(self._matrix)):
            for k in self._matrix[i][from_node.index]:
                self.connect_dir(to_node, self._nodes[i], k)
                self.disconnect_dir(self._nodes[i], from_node, k)

        for j in range(len(self._matrix[from_node.index])):
            for k in self._matrix[from_node.index][j]:
                self.connect_dir(self._nodes[j], to_node, k)
                self.disconnect_dir(from_node, self._nodes[j], k)

    def rib_retraction(self, from_node, to_node, weight):
        if len(self._matrix[from_node.index][to_node.index]) > 0:
            self.node_association(from_node, to_node)
            self.disconnect_dir(to_node, to_node, weight)
        else:
            raise Exceptions_Graph.RibNotIncludedError

    def node_duplication(self, from_node, node):
        self.add_node(node)
        for i in range(len(self._matrix[from_node.index])):
            for j in self._matrix[from_node.index][i]:
                self.connect_dir(node, self._nodes[i], j)
        for i in range(len(self._matrix)):
            for j in self._matrix[i][from_node.index]:
                self.connect_dir(node, self._nodes[i], j)
