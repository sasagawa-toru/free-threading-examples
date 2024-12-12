from multiprocessing import Process
from random import Random


def process_main(filename):
    r = Random()
    with open(filename, "w") as f:
        for _ in range(10000000):
            f.write(f"{r.random()}")
            f.flush()


def main():
    nprocess = 4
    procs = [
        Process(target=process_main, args=(f"tmp/out{i}.txt",)) for i in range(nprocess)
    ]
    for t in procs:
        t.start()

    for t in procs:
        t.join()


if __name__ == "__main__":
    main()
