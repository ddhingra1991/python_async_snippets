from time import sleep
import time

def hello():
    print('Hello')
    sleep(3)
    print('World')


def main():
    hello()
    hello()
    hello()
    hello()
    hello()
    hello()

if __name__=='__main__':
    start = time.perf_counter()
    main()
    print(time.perf_counter() - start)