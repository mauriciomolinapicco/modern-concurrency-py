import threading
import time
import random

def procesar_datos(site, delay):
    print(f"[{site}] Procesando con delay de {delay:.2f}s...")
    time.sleep(delay)
    resultado = f"{site}-OK"
    print(f"[{site}] Resultado: {resultado}")
    return resultado

def worker(site):
    delay = random.uniform(1, 3)
    procesar_datos(site, delay)

def main():
    sitios = ["RIPIO", "BITSO", "BINANCE", "LEMONT"]
    threads = []

    for site in sitios:
        t = threading.Thread(target=worker, args=(site,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Fin de ejecución concurrente con parámetros.")

if __name__ == "__main__":
    main()
