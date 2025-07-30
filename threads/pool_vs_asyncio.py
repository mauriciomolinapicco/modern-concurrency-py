from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import asyncio
import random

""" pool executor """
def llamada_http(site_id):
    delay = random.uniform(1, 3)
    print(f"[{site_id}] Iniciando (delay={delay:.2f}s)")
    time.sleep(delay)  # Simula una llamada bloqueante
    print(f"[{site_id}] Finalizada")
    return site_id

def main_pool():
    sitios = [f"SITE_{i:02d}" for i in range(10)]

    start = time.time()
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(llamada_http, s) for s in sitios]

        for f in as_completed(futures):
            f.result()
    end = time.time()

    print(f"\nTotal tiempo: {end - start:.2f} segundos")

"""
    asyncio
"""
async def llamada_http(site_id):
    delay = random.uniform(1, 3)
    print(f"[{site_id}] Iniciando (delay={delay:.2f}s)")
    await asyncio.sleep(delay)  # No bloquea
    print(f"[{site_id}] Finalizada")
    return site_id

async def main_async():
    sitios = [f"SITE_{i:02d}" for i in range(10)]

    start = asyncio.get_event_loop().time()
    tareas = [llamada_http(s) for s in sitios]
    await asyncio.gather(*tareas)
    end = asyncio.get_event_loop().time()

    print(f"\nTotal tiempo: {end - start:.2f} segundos")


if __name__ == "__main__":
    op = int(input("Ingrese 1 para ejecucion de pool o 2 para ejecucion de asyncio: "))
    if op == 1:
        main_pool()
    else:
        asyncio.run(main())


