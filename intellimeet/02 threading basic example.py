import threading
from time import sleep


def do_some_work(some_val):
    print(f"{threading.currentThread().getName()}1. doing some work in thread for {some_val}")
    sleep(5)
    print(f"{threading.currentThread().getName()}2. work done..")


val = "text 1"

t = threading.Thread(target=do_some_work, args=(val,))
t.start()
print(f"{threading.currentThread().getName()}3. last instruction..")
t.join()


