import Exceptions_Node


class Node():
    def __init__(self, name=None, data=None, index=None):
        self._name = name
        self._data = data
        self._index = index

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_data):
        self._data = new_data

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, new_index):
        self._index = new_index

    def __eq__(self, other):
        if isinstance(other, Node):
            return self._equal(other.data)
        else:
            return self._equal(other)

    def _equal(self, other):
        try:
            if self.data == other:
                return True
            else:
                return False
        except TypeError:
            return False

    def __hash__(self):
        return hash(self.name)


