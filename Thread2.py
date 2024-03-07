from time import sleep
from threading import Thread

def task(sleep_time, message):
    sleep(sleep_time)
    print(message)

thread = Thread(target=task, args=(2, "un nouveau message d'un autre thread"))

thread.start()
print("attendre le thread ...")
thread.join()