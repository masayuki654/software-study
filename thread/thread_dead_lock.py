import threading
import time

data = 0
lock1 = threading.Lock()
lock2 = threading.Lock()


def generator1(start, end):
    global data
    for i in range(start, end, 1):
        lock1.acquire()
        lock2.acquire()
        print(i)
        time.sleep(0.1)
        lock2.release()
        lock1.release()


def generator2(start, end):
    global data
    for i in range(start, end, 1):
        lock2.acquire()
        lock1.acquire()
        print(i)
        time.sleep(0.1)
        lock1.release()
        lock2.release()


t1 = threading.Thread(target=generator1, args=(1, 10))
t2 = threading.Thread(target=generator2, args=(1, 10))
t1.start()
t2.start()
t1.join()
t2.join()
print(data)
