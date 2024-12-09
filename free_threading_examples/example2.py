from random import Random
from threading import Thread


def thread_main():
    r = Random()
    with open("/dev/null", "w") as sink:
        for _ in range(10000000):
            sink.write(f"{r.random()}")


def main():
    nthread = 4
    threads = [Thread(target=thread_main) for _ in range(nthread)]
    for t in threads:
        t.start()

    for t in threads:
        t.join()


if __name__ == "__main__":
    main()
