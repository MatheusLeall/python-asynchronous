import time
from queue import Queue
from threading import Thread

import colorama


def data_generator(queue: Queue) -> None:
    for index in range(1, 11):
        print(colorama.Fore.WHITE + f"Data {index} generated.", flush=True)
        time.sleep(2)
        queue.put(index)


def consumer(queue: Queue) -> None:
    while queue.qsize() > 0:
        value = queue.get()
        print(colorama.Fore.GREEN + f"Data {value * 2} processed.", flush=True)
        time.sleep(1)
        queue.task_done()


if __name__ == "__main__":
    print(colorama.Fore.BLUE + "System started...", flush=True)
    queue: Queue = Queue()
    th1 = Thread(target=data_generator, args=(queue,))
    th2 = Thread(target=consumer, args=(queue,))

    th1.start()
    th1.join()

    th2.start()
    th2.join()
