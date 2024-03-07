from time import sleep, perf_counter
from threading import Thread
from random import random
from threading import Lock

inc = 0

# def task(lock, identifier, value):
#     global inc
#     with lock:
#         print(inc)
#         inc = inc + 1

# lock = Lock()
# for i in range(10):
#     Thread(target=task, args=(lock, i, inc)).start()


def task():
    sleep(0.2)
    global inc
    inc = inc + 1
    print(inc)

for i in range(10):
    thread = Thread(target=task)
    thread.start()
