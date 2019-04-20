import multiprocessing


def do_work(data):
    return data**data


def start_processing():
    print(f'Starting {multiprocessing.current_process().name}')


if __name__=="__main__":
    pool_size = multiprocessing.cpu_count()*2
    pool = multiprocessing.Pool(
        processes=pool_size,
        initializer=start_processing
    )
    inputs = list(range(100))

    # outputs = pool.map(do_work,inputs)
    # print(f'Outputs : {outputs}')

    # # async block # #
    outputs = pool.map_async(do_work,inputs)
    print(f'Outputs : {outputs.get(10)}')

    pool.close()  # no more tasks
    pool.join()  # wait for the worker processes to exit
