from multiprocessing import Process
from random import Random


def process_main():
    r = Random()
    with open("/dev/null", "w") as sink:
        for _ in range(10000000):
            sink.write(f"{r.random()}")


def main():
    nprocess = 4
    procs = [Process(target=process_main) for i in range(nprocess)]
    for t in procs:
        t.start()

    for t in procs:
        t.join()


if __name__ == "__main__":
    main()
