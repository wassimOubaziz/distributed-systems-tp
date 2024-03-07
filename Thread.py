from time import sleep
from threading import Thread

def task():
    sleep(1)
    print("execution d'un thred")

thread = Thread(target=task)

thread.start()
print("attendre le thread ...")
thread.join()


