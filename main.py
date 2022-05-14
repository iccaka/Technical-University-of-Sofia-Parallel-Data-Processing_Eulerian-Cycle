from graph import Graph
import time
import threading


def create_graph(size):
    G = Graph([], {})
    for x in range(1, size + 1):
        G.add_vertex(x)
    for x in range(1, size + 1):
        for y in range(x + 1, size + 1):
            G.add_edge(x, y)
    return G


if __name__ == '__main__':
    G1 = create_graph(33)
    G2 = create_graph(77)
    G3 = create_graph(99)
    graphs = [G1, G2, G3]

    print("Nonparallel, single vertex:")
    before = time.perf_counter()
    for x in graphs:
        x.euler_tour(1)
    after = time.perf_counter()
    difference = after - before
    print(f"It took {difference} seconds")

    print("Parallel, single vertex:")
    threads = []
    before = time.perf_counter()
    for x in graphs:
        thread = threading.Thread(target=x.euler_tour, args=(1, ))
        threads.append(thread)
    for x in threads:
        x.start()
    for x in threads:
        x.join()
    after = time.perf_counter()
    difference = after - before
    print(f"Threads took {difference} seconds")

    print("Nonparallel, all vertices:")
    for x in graphs:
        before = time.perf_counter()
        for y in x.V:
            x.euler_tour(y)
        after = time.perf_counter()
        difference = after - before
        print(f"It took {difference} seconds")

    print("Parallel, all vertices:")
    for x in graphs:
        threads = []
        for y in x.V:
            thread = threading.Thread(target=x.euler_tour, args=(y, ))
            threads.append(thread)
        before = time.perf_counter()
        for z in threads:
            z.start()
        for z in threads:
            z.join()
        after = time.perf_counter()
        difference = after - before
        print(f"Threads took {difference} seconds")
