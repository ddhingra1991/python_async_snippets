import multiprocessing
import time


def f(x1,y1,x2,y2):
    for i in range(23):
        x1=x1*x1
        x2=x2*x2
        y1=y1*y1
        y2=y2*y2
        print("loading..")


if __name__=="__main__":
    start = time.perf_counter()
    f(2,3,2,4)
    f(3,2,2,4)
    f(2,3,4,2)
    f(3,3,3,4)
    print("completed in {}".format(time.perf_counter() - start))