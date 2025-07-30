import threading
import time

def tarea_larga(nombre):
    print(f"[{nombre}] Inicia tarea.")
    time.sleep(2)
    print(f"[{nombre}] Termina tarea.")

def main():
    print("Lanzando threads de ejemplo...")

    hilo1 = threading.Thread(target=tarea_larga, args=("Hilo-1",))
    hilo2 = threading.Thread(target=tarea_larga, args=("Hilo-2",))

    hilo1.start()
    hilo2.start()

    print("Esperando que terminen los hilos...")

    hilo1.join()
    hilo2.join()

    print("Todos los hilos completados.")

if __name__ == "__main__":
    main()
