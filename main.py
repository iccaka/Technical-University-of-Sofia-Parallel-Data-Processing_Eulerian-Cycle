import datetime

from graph import Graph
import time
import threading


def do_something():
    print("hi")
    time.sleep(0.5)


if __name__ == '__main__':
    G = Graph([1, 2, 3, 4, 5, 6, 7], {(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7),
                                      (2, 3), (2, 4), (2, 5), (2, 6), (2, 7),
                                      (3, 4), (3, 5), (3, 6), (3, 7),
                                      (4, 5), (4, 6), (4, 7),
                                      (5, 6), (5, 7),
                                      (6, 7)})

    before = datetime.datetime.now().microsecond

    print("Nonparallel way:")

    for x in G.V:
        G.euler_tour(x)

    after = datetime.datetime.now().microsecond
    difference = after - before

    print(f"Time it took(nonparallel): {difference} microseconds")
    print(f"\n=====================================\n")
    print("Parallel way:")

    threads = []
    for x in G.V:
        t = threading.Thread(target=G.euler_tour, args=(x, ))
        threads.append(t)

    before = datetime.datetime.now().microsecond

    for x in threads:
        x.start()

    for x in threads:
        x.join()

    after = datetime.datetime.now().microsecond
    difference = after - before

    print(f"Time it took(parallel): {difference} microseconds")
