from graph import Graph

if __name__ == '__main__':
    G = Graph([1, 2, 3, 4, 5, 6, 7], {(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7),
                                      (2, 3), (2, 4), (2, 5), (2, 6), (2, 7),
                                      (3, 4), (3, 5), (3, 6), (3, 7),
                                      (4, 5), (4, 6), (4, 7),
                                      (5, 6), (5, 7),
                                      (6, 7)})
    G1 = Graph([1, 2, 3, 4, 5], {(1, 2), (1, 3), (1, 4), (1, 5),
                                 (2, 3), (2, 4), (2, 5),
                                 (3, 4), (3, 5),
                                 (4, 5)})
    G2 = Graph([1, 2, 3, 4, 5], {(1, 2), (1, 3), (1, 4), (1, 5),
                                 (2, 3), (4, 5)})
    print(G.euler_tour())
    print(G1.euler_tour())
    print(G2.euler_tour())

    G3 = Graph([1, 2, 3, 4], {(1, 2), (1, 3), (1, 4),
                              (2, 3)})
    print(G3.euler_tour())

    # G = Graph([1, 2, 3, 4], {(1, 2), (1, 3), (2, 3)})
    # assert(len(G.V) == 4 and len(G.E) == 3 and G.deg(1) == 2)
    #
    # G.add_vertex(5)
    # G.add_edge(1, 5)
    # assert(len(G.V) == 5 and len(G.E) == 4 and G.deg(1) == 3)
    #
    # G.remove_vertex(5)
    # assert(len(G.V) == 4 and len(G.E) == 3 and G.deg(1) == 2)
    #
    # G.remove_vertex(6)
    # assert(len(G.V) == 4 and len(G.E) == 3)
