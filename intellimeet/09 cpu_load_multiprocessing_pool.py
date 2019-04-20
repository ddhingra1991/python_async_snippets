import multiprocessing
import threading
import time


# def f(x1,y1,x2,y2):
def f(iter_x):
    x1,y1,x2,y2 = iter_x
    print(f"{multiprocessing.current_process().name} started..")

    for i in range(23):
        x1=x1*x1
        x2=x2*x2
        y1=y1*y1
        y2=y2*y2


def call_f():
    print(f'Starting {multiprocessing.current_process().name}')


if __name__=="__main__":
    args_list = [(2,3,2,4),(2,3,2,4),(2,3,4,2),(3,3,3,4)]
    pool_size = multiprocessing.cpu_count()*2
    # pool_size = 4
    pool = multiprocessing.Pool(
        processes=pool_size,
        initializer=call_f()
    )
    inputs = args_list
    start = time.perf_counter()
    # outputs = pool.map(f,inputs)

    # async block..#
    outputs = pool.map_async(f,inputs)
    try:
        outputs.get(5)
    except multiprocessing.context.TimeoutError as te:
        print("Timed out..")

    print(f"completed in {time.perf_counter() - start}")

    pool.close()
    pool.join()

