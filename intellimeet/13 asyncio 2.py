import asyncio
import datetime
import time
loop = asyncio.get_event_loop()


#  co-routine
async def hello():
    print('Hello')
    await asyncio.sleep(3)
    print('World')
    return datetime.datetime.now().isoformat()


async def bye():
    print("bye!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


async def main():
    abc = await asyncio.gather(hello(), hello(), hello(), hello(), hello(), hello(),bye())
    print(abc)


if __name__ == "__main__":
    start = time.perf_counter()

    loop.run_until_complete(main())
    loop.run_in_executor()
    asyncio.new_event_loop()
    # print("I am done")
    print(time.perf_counter() - start)