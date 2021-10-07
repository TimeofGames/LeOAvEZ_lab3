class Queue():
    def __init__(self):
        self._first = None
        self._last = None
        self._len = 0

    def add(self, data):
        node = QueueNode(data)
        if self._first is None:
            self._first = node
            self._last = node
        else:
            self._last.next = node
            self._last = node
        self._len += 1

    def pop(self):
        to_ret = self._first
        self._first = self._first.next
        self._len -= 1
        return to_ret.data

    def __len__(self):
        return self._len


class QueueNode():
    def __init__(self, data):
        self._data = data
        self._next = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new):
        self._data = new

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, new):
        self._next = new
