from time import sleep, perf_counter
from threading import Thread
from random import random
from threading import Lock

def task(lock, identifier, value):
    with lock:
        print("thread", identifier, "a le verou, il dor pour", value)
        sleep(value)

lock = Lock()
for i in range(10):
    Thread(target=task, args=(lock, i, random())).start()