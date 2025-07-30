from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import random

def tarea(site_id):
    inicio = time.time()
    delay = random.uniform(0.5, 2.5)
    print(f"[{site_id}] Start (delay: {delay:.2f}s)")
    time.sleep(delay)
    fin = time.time()
    return f"[{site_id}] Done in {fin - inicio:.2f}s"

def main():
    sitios = [f"SITE_{i:02d}" for i in range(10)]

    print("Ejecutando tareas con ThreadPoolExecutor...")
    resultados = []

    with ThreadPoolExecutor(max_workers=4) as executor:
        futuros = [executor.submit(tarea, site) for site in sitios]

        for future in as_completed(futuros):
            resultado = future.result()
            resultados.append(resultado)
            print(resultado)

    print("\nResumen:")
    for r in resultados:
        print(r)

if __name__ == "__main__":
    main()
