"""
explicacion de gpt
aiohttp es una librería asíncrona para hacer solicitudes HTTP. 
Se usa con asyncio para poder hacer varias peticiones web al 
mismo tiempo,  sin bloquear el programa mientras espera la respuesta.
"""
import asyncio
import time
from concurrent.futures import ThreadPoolExecutor
from utils.fake_io import fake_fetch

# Async version
async def run_async():
    tasks = [fake_fetch(i) for i in range(5)]
    await asyncio.gather(*tasks)

# Threaded version
def run_threads():
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(asyncio.run, fake_fetch(i)) for i in range(5)]
        for f in futures:
            f.result()

if __name__ == "__main__":
    start = time.time()
    asyncio.run(run_async())
    print("Asyncio took:", time.time() - start)

    start = time.time()
    run_threads()
    print("Threads took:", time.time() - start)
