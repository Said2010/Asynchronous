import random

import asyncio

async def check(city):
    print(f"Проверка товаров в городе {city}")
    prod = random.randint(100, 1001)
    await asyncio.sleep(5)
    print(f"Товаров {prod}")

async def main():
    async with asyncio.TaskGroup() as tg:
        citys = ["A","B","C","D"]
        for city in citys:
            tg.create_task(check(city))
    
asyncio.run(main())
