import asyncio
from utils.fake_io import fake_fetch

async def main():
    tasks = [fake_fetch(i) for i in range(5)]
    results = await asyncio.gather(*tasks)
    print("Resultados:", results)

asyncio.run(main())
