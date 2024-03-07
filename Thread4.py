from time import sleep
from threading import Thread



thread1 = Thread()
thread2 = Thread(daemon=True)
thread3 = Thread()
thread3.daemon = True

print(thread1.daemon)
print(thread2.daemon)
print(thread3.daemon)