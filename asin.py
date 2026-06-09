import asyncio
 
async def print_1():
    print(10)

async def print_2():
    await asyncio.sleep(5)
    print(20)

async def print_3():
    print(30)

async def main():
    await asyncio.gather(print_1(), print_2(), print_3())

asyncio.run(main())