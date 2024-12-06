from random import Random
from threading import Thread


def thread_main(filename):
    r = Random()
    with open(filename, "w") as f:
        for _ in range(10000000):
            f.write(f"{r.random()}")


def main():
    nthread = 4
    threads = [
        Thread(target=thread_main, args=(f"tmp/out{i}.txt",)) for i in range(nthread)
    ]
    for t in threads:
        t.start()

    for t in threads:
        t.join()


if __name__ == "__main__":
    main()
