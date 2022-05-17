from graph import Graph
from multiprocessing import Process
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
    G1 = create_graph(51)
    G2 = create_graph(111)
    G3 = create_graph(151)
    G4 = create_graph(211)
    graphs = [G1, G2, G3, G4]

    print("Nonparallel, single vertex:")
    before = time.perf_counter()
    for x in graphs:
        x.euler_tour(x.get_any_vertex())
    after = time.perf_counter()
    difference = after - before
    print(f"\tIt took {difference} seconds")
    #
    print("Multithreading, single vertex:")
    threads = []
    for x in graphs:
        thread = threading.Thread(target=x.euler_tour, args=(x.get_any_vertex(), ))
        threads.append(thread)
    before = time.perf_counter()
    for x in threads:
        x.start()
    for x in threads:
        x.join()
    after = time.perf_counter()
    difference = after - before
    print(f"\tThreads took {difference} seconds")

    print("Multiprocessing, single vertex:")
    processes = []
    for x in graphs:
        process = Process(target=x.euler_tour, args=(x.get_any_vertex(), ))
        processes.append(process)
    before = time.perf_counter()
    for x in processes:
        x.start()
    for x in processes:
        x.join()
    after = time.perf_counter()
    difference = after - before
    print(f"\tProcesses took {difference} seconds")

    print("Nonparallel, all vertices:")
    for x in graphs:
        before = time.perf_counter()
        for y in x.V:
            x.euler_tour(y)
        after = time.perf_counter()
        difference = after - before
        print(f"\tIt took {difference} seconds")

    print("Multithreading, all vertices:")
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
        print(f"\tThreads took {difference} seconds")

    print("Multiprocessing, all vertices:")
    for x in graphs:
        processes = []
        for y in x.V:
            process = Process(target=x.euler_tour, args=(y, ))
            processes.append(process)
        before = time.perf_counter()
        for z in processes:
            z.start()
        for z in processes:
            z.join()
        after = time.perf_counter()
        difference = after - before
        print(f"\tProcesses took {difference} seconds")
