import multiprocessing
import threading
import time
from concurrent.futures import ProcessPoolExecutor


def f(x1,y1,x2,y2):
    print(f"{multiprocessing.current_process().name} started..")

    for i in range(23):
        x1=x1*x1
        x2=x2*x2
        y1=y1*y1
        x1=x1*x1
    return 1


if __name__=="__main__":
    args_list = [(2,3,2,4),(2,3,2,4),(2,3,4,2),(3,3,3,1)]
    processes = []
    start = time.perf_counter()

    with ProcessPoolExecutor(max_workers=4) as executor:
        for arg_ in args_list:
            processes.append(executor.submit(f, *arg_)) # non-blocking call

    for p in processes:
        try:
            #  try except added to the code which calls result method &
            #  not on the submit method
            print(p.result()) # blocking call.
        except Exception as e:
            print(f"Exception occured : {e}")

    print(f"completed in {time.perf_counter() - start}")