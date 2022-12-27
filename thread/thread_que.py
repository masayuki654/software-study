import threading
import queue
import time


# queue is FIFO type data structure
work = queue.Queue()


def generator(start, end):
    for i in range(start, end, 1):
        work.put(i)


def display():
    while work.empty() is False:
        data = work.get()
        print("data is " + str(data))
        time.sleep(1)
        # synchronize queue
        work.task_done()


threading.Thread(target=generator, args=(1, 10)).start()
threading.Thread(target=display).start()
# done when queue is finished
work.join()
