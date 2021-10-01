import Exceptions_Matrix
import Exceptions_Graph
import AdjacencyList


class Matrix():
    def __init__(self):
        self._nodes = []
        self._matrix = []

    @property
    def nodes(self):
        return self._nodes

    @property
    def matrix(self):
        return self._matrix

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
            for j in range(len(self._matrix[i])):
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
        for i in range(len(self._matrix[from_node.index])):
            for j in self._matrix[from_node.index][i]:
                self.connect_dir(node, self._nodes[i], j)
        for i in range(len(self._matrix)):
            for j in self._matrix[i][from_node.index]:
                self.connect_dir(self._nodes[i], node, j)

    def plus(self, first_matrix, second_matrix, links):
        for i in range(len(first_matrix.matrix)):
            for j in range(len(first_matrix.matrix[i])):
                for k in first_matrix.matrix[i][j]:
                    self.connect_dir(self._nodes[links[first_matrix.nodes[i]]],
                                     self._nodes[links[first_matrix.nodes[j]]], k)

        for i in range(len(second_matrix.matrix)):
            for j in range(len(second_matrix.matrix[i])):
                for k in second_matrix.matrix[i][j]:
                    self.connect_dir(self.nodes[links[second_matrix.nodes[i]]],
                                     self._nodes[links[second_matrix.nodes[j]]], k)

    def matrix_crossing(self, first_matrix, second_matrix, links):
        for i in range(len(self._matrix)):
            for j in range(len(self._matrix[i])):
                first_array = first_matrix.matrix[links[i].index][links[j].index]
                second_array = second_matrix.matrix[links[i].index][links[j].index]
                for k in first_array:
                    for g in second_array:
                        if k == g:
                            self.connect_dir(self._nodes[i], self._nodes[j], k)

    def annular_sum(self, first_matrix, second_matrix, links):
        for i in range(len(self._matrix)):
            for j in range(len(self._matrix[i])):
                first_array = first_matrix.matrix[links[i].index][links[j].index]
                second_array = second_matrix.matrix[links[i].index][links[j].index]
                for k in first_array:
                    if k not in [g for g in second_array]:
                        self.connect_dir(self._nodes[i], self._nodes[j], k)
                for k in second_array:
                    if k not in [g for g in first_array]:
                        self.connect_dir(self._nodes[i], self._nodes[j], k)

    def cartesian_product(self, first_matrix, second_matrix, links):
        for i in range(len(self._matrix)):
            for j in range(len(self._matrix[i])):
                if links[i][0] == links[j][0] and len(second_matrix.matrix[links[i][1].index][links[j][1].index]) > 0:
                    self._matrix[i][j] = (second_matrix.matrix[links[i][1].index][links[j][1].index])
                elif links[i][1] == links[j][1] and len(first_matrix.matrix[links[i][0].index][links[j][0].index]) > 0:
                    self._matrix[i][j] = (first_matrix.matrix[links[i][0].index][links[j][0].index])

    def dfs(self, node):
        return self._dfs_real(node)

    def _dfs_real(self, node):
        visits = []
        stack = [node.index]
        while len(stack) > 0:
            item = stack.pop()
            if item not in visits:
                visits.append(item)
                for i in range(len(self._matrix[item]) - 1, 0, -1):
                    if len(self._matrix[item][i]) > 0:
                        stack.append(i)
        return visits
