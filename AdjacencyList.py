import Exceptions_list
import Exceptions_Graph
import Matrix


class AdjacencyList():
    def __init__(self):
        self._adj_list = dict()

    def add_node(self, node):
        self._adj_list[node] = list()

    def del_node(self, node):
        self._adj_list.pop(node)
        for i in self._adj_list.keys():
            count = 0
            for j in self._adj_list[i]:
                if j == node:
                    count += 1
            for _ in range(count):
                self._adj_list[i].pop(node)

    def print(self):
        for i in self._adj_list.keys():
            print(str(i.name) + ":", end="")
            for j in self._adj_list[i]:
                print(str(j[0].name + "[" + str(j[1]) + "]") + ", ", end="")
            print()

    def connect_dir(self, from_node, to_node, weight=1):
        self._adj_list[from_node].append([to_node, weight])

    def disconnect_dir(self, from_node, to_node, weight=1):
        self._adj_list[from_node].remove([to_node, weight])

    def convert_to_matrix(self):
        matrix = Matrix.Matrix()
        for i in self._adj_list.keys():
            matrix.add_node(i)
        for i in self._adj_list.keys():
            for j in self._adj_list[i]:
                matrix.connect_dir(i, j[0], j[1])
        return matrix

    def node_association(self, from_node, to_node):
        for i in self._adj_list.keys():
            local_copy = self._adj_list[i][:]
            for j in local_copy:
                if j[0] == from_node:
                    self.connect_dir(i, to_node, j[1])
                    self.disconnect_dir(i, from_node, j[1])
        local_copy = self._adj_list[from_node][:]
        for i in local_copy:
            self.connect_dir(to_node, i[0], i[1])
            self.disconnect_dir(from_node, i[0], i[1])

    def rib_retraction(self, from_node, to_node, weight):
        if from_node in [i[0] for i in self._adj_list[to_node]] or to_node in [i[0] for i in self._adj_list[from_node]]:
            self.node_association(from_node, to_node)
            self.disconnect_dir(to_node, to_node, weight)
        else:
            raise Exceptions_Graph.RibNotIncludedError

    def node_duplication(self, from_node, node):
        self.add_node(node)
        for i in self._adj_list.keys():
            for j in self._adj_list[i]:
                if j[0] == from_node:
                    self.connect_dir(j[0], node, j[1])

        for i in self._adj_list[from_node]:
            self.connect_dir(node, i[0], i[1])
