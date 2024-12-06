from random import Random


def main():
    r = Random()
    with open("/dev/null", "w") as sink:
        for _ in range(10000000):
            sink.write(f"{r.random()}")


if __name__ == "__main__":
    main()
