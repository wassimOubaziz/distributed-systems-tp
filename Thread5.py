from time import sleep
from threading import Thread

def task():
    sleep(1)

thread = Thread(target=task)
print(thread.is_alive())
thread.start()
print(thread.is_alive())
thread.join()
print(thread.is_alive())
