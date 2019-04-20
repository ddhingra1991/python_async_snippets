import multiprocessing
import os
import signal
import threading
from time import sleep


def do_some_work(some_val):
    print("1. doing some work in process")

    sleep(5)
    print("2. work done..")



val = "text"

# below dunder method important for avoiding process creation race around
# condition.
if __name__=="__main__":
    t = multiprocessing.Process(target=do_some_work, args=(val,), daemon=False)
    t.start()
    os.kill(multiprocessing.current_process().pid,signal.SIGKILL)


    print("3. last instruction..")

    # t.join()



