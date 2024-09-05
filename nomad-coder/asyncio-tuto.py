import asyncio
# import time

# async def main():
#     print('Hello')
#     await asyncio.sleep(1)
#     print('World')


# asyncio.run(main())

# def say_hello():
#     time.sleep(2)
#     print("Hello, Async World? (not yet)")

# say_hello()

# async def say_hello_async():
#     await asyncio.sleep(2)
#     print("Hello, Async World!")

# asyncio.run(say_hello_async())

async def say_hello_async():
    print("Start say_hello!")
    await asyncio.sleep(2)
    print("Hello, Async World!")

async def do_something_else():
    print("Starting another task...")
    await asyncio.sleep(1)
    print("Finished another task!")

async def main():
    await asyncio.gather(
        say_hello_async(),
        do_something_else(),
    )

asyncio.run(main())