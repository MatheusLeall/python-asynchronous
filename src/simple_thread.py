import time
from threading import Thread
from typing import Any


def main():
    th = Thread(target=count, args=("cat", 10))

    th.start()

    print("We can do other things while a thread execute...")
    print("I want to know what is the sum of 10 plus 10: ", 10 + 10)

    th.join()

    print("Ready!")


def count(value: Any, number: int) -> None:
    for n in range(1, number + 1):
        print(f"{n} {value}'s")
        time.sleep(1)


if __name__ == "__main__":
    main()
