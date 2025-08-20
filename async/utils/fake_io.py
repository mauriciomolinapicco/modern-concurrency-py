import asyncio
import random

async def fake_fetch(i):
    delay = random.uniform(0.5, 2.0)
    await asyncio.sleep(delay)
    return f"resultado {i} despues de {delay:.2f}s"
