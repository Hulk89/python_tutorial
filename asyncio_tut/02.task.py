import asyncio
import time

async def sleep(sleep_time):
    await asyncio.sleep(sleep_time)
    now = time.time()
    return now

async def main():
    start_time = time.time()
    # create_task로 곧 실행되도록 예약을 건다.
    task2 = asyncio.create_task(sleep(2))
    task1 = asyncio.create_task(sleep(1))

    # "task" can now be used to cancel "sleep()", or
    # can simply be awaited to wait until it is complete:
    time_after_task2 = await task2
    time_after_task1 = await task1

    # task1, 2가 거의 동시에 시작했으므로, 시작시간으로부터 각각 1초, 2초가 지나야한다.
    print(start_time)
    print(time_after_task1)
    print(time_after_task2)

asyncio.run(main())
