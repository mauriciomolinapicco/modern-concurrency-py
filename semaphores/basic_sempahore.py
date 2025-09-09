import threading
import time
from contextlib import contextmanager

class SemaphoreManager:
    """
    Helper para manejar concurrencia con semáforos.
    Permite limitar la cantidad de hilos que ejecutan un recurso crítico.
    """

    def __init__(self, max_concurrent: int = 5):
        self._semaphore = threading.Semaphore(max_concurrent)

    @contextmanager
    def acquire(self, timeout: float = None):
        """
        Context manager para adquirir el semáforo de forma segura.
        :param timeout: Tiempo máximo de espera para adquirir el recurso.
        """
        acquired = self._semaphore.acquire(timeout=timeout)
        try:
            if not acquired:
                raise TimeoutError("No se pudo adquirir el semáforo a tiempo")
            yield
        finally:
            if acquired:
                self._semaphore.release()

    def run_with_semaphore(self, func, *args, **kwargs):
        """
        Ejecuta una función asegurando el control del semáforo.
        """
        with self.acquire():
            return func(*args, **kwargs)


if __name__ == "__main__":
    sem_manager = SemaphoreManager(max_concurrent=3)

    def tarea(n):
        with sem_manager.acquire():
            print(f"Ejecutando tarea {n}")
            time.sleep(2)
            print(f"Tarea {n} finalizada")

    threads = [threading.Thread(target=tarea, args=(i,)) for i in range(6)]

    for t in threads: t.start()
    for t in threads: t.join()
