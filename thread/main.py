import threading


# normal
def example_normal():
    for i in range(1, 10, 1):
        print(i)


example_normal()
example_normal()


# thread
def example():
    for i in range(1, 10, 1):
        print(i)


threading.Thread(target=example).start()
threading.Thread(target=example).start()
