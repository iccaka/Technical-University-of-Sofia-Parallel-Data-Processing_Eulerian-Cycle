from graph import Graph
from linked_list import LinkedList


class CycleFinder:
    @staticmethod
    def find_cycles(G):
        if not G.is_eulerian():
            print("An Eulerian Cycle for the given graph is not possible.")
            return

        verticesn = len(G.V)
        edgesn = len(G.E)
        path = LinkedList()


if __name__ == '__main__':
    # G = Graph([1, 2, 3, 4, 5], {(1, 2), (1, 3), (1, 4), (1, 5), (2, 4), (2, 3), (2, 5), (3, 4), (3, 5), (4, 5)})
    # G = Graph([1, 2, 3, 4], {(1, 2), (1, 3), (1, 4), (2, 3)})
    G = Graph([1, 2, 3, 4], {(1, 2), (1, 3), (2, 3)})
    print(list(G.neighbors(1)))
    print(list(G.neighbors(2)))
    G.add_edge(1, 4)
    G.add_edge(2, 5)
    print(list(G.neighbors(1)))
    print(list(G.neighbors(2)))
    print(len(G.V))

    # print(list(G.neighbors(1)))
    # print(list(G.V))
