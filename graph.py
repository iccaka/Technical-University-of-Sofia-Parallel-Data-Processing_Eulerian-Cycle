from ds2.deque import DoublyLinkedList as Deque


class Graph:
    # V - Vertex
    # E - Edge
    def __init__(self, V, E):
        self.V = set(V)
        self.E = set(frozenset(E))
        self._neighbors = {}
        for v in self.V:
            self._neighbors[v] = set()
        for u, v in self.E:
            self._neighbors[u].add(v)
            self._neighbors[v].add(u)

    # Returns the degree of the specified vertex
    def deg(self, v):
        return len(self._neighbors[v])

    # Returns an iterator object with all the neighbors
    def neighbors(self, v):
        return iter(self._neighbors[v])

    def remove_vertex(self, u):
        todelete = list(self.neighbors(u))
        for v in todelete:
            self.remove_edge(u, v)
        del self._neighbors[u]

    def add_vertex(self, v):
        if v not in self._neighbors:
            self._neighbors[v] = set()

    # Removes an edge connecting two vertices
    def remove_edge(self, u, v):
        e = frozenset([u, v])
        # Checks to see if such an edge exists
        if e in self.E:
            self.E.remove(e)
            self._neighbors[u].remove(v)
            self._neighbors[v].remove(u)

    # Adds an edge connecting two vertices
    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        self.E.add(frozenset([u, v]))
        self._neighbors[u].add(v)
        self._neighbors[v].add(u)

    def breadth_first_search(self, v):
        tree = {}
        tovisit = [(None, v)]
        while tovisit:
            a, b = tovisit.pop()
            if b not in tree:
                tree[b] = a
                for c in self.neighbors(b):
                    tovisit.insert(0, (b, c))
        return tree

    def depth_first_search(self, v):
        tree = {}
        tovisit = [(None, v)]
        while tovisit:
            a, b = tovisit.pop()
            if b not in tree:
                tree[b] = a
                for c in self.neighbors(b):
                    tovisit.append((b, c))
        return tree

    def path(self, u, v):
        tree = self.breadth_first_search(v)
        if u in tree:
            path = []
            while u is not None:
                path.append(u)
                u = tree[u]
            return path

    def deque_to_tour(self, deque):
        path = []
        while deque:
            path.append(deque.removefirst())

    def euler_tour(self):
        if self.is_eulerian():
            path = Deque()
            H = Graph(self.V, self.E)
            current_vertex = H.get_any_vertex()
            while len(H.E) > 0:
                if H.deg(current_vertex) > 0:
                    next_vertex = next(H.neighbors(current_vertex))
                    path.addlast(next_vertex)
                    H.remove_edge(current_vertex, next_vertex)
                    current_vertex = next_vertex
                else:
                    current_vertex = path.removefirst()
                    path.addlast(current_vertex)
            return self.deque_to_tour(path)

    def get_any_vertex(self):
        return next(iter(self._neighbors))

    # Checks if the degree of every edge is greater than 0
    def is_connected(self):
        v = self.get_any_vertex()
        return len(self.depth_first_search(v)) == len(self.E)

    # Checks if two edges are connected to each other
    def are_connected(self, u, v):
        return v in self.depth_first_search(u)

    # Check if the graph is eulerian
    def is_eulerian(self):
        return self.is_connected() and all(self.deg(v) % 2 == 0 for v in self.V)
