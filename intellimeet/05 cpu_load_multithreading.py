import multiprocessing
import threading
import time


def f(x1,y1,x2,y2):
    print(f"{threading.currentThread().getName()} started..")

    for i in range(23):
        x1=x1*x1
        x2=x2*x2
        y1=y1*y1
        y2=y2*y2


if __name__=="__main__":
    args_list = [(2,3,2,4),(2,3,2,4),(2,3,4,2),(3,3,3,4)]
    threads = []
    start = time.perf_counter()
    for arg_ in args_list:
        t = threading.Thread(target=f,args=arg_)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print(f"completed in {time.perf_counter() - start}")