import asyncio

async def nested():
    return 42

async def main():
    print(nested())  # <coroutine object nested at 0x109e5ccc0>
    print(await nested())  # will print "42".

asyncio.run(main())
