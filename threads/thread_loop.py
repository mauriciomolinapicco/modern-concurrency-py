import time
import threading 
import concurrent.futures

def do_something(seconds):
    print(f"Sleeping {seconds} seconds")
    time.sleep(seconds)
    return f"Termine... {seconds} segundos"

with concurrent.futures.ThreadPoolExecutor() as executor:
    segundos = [5,4,3,2,1]
    results = [executor.submit(do_something, seg) for seg in segundos]
    
    #IMPORTANTE: esta forma es buenisima porque printea los results a medida que se van completando, no importa si el ultimo que se lanzo es el primero a ejecutarsse
    #con el segundo loop hasta que no termine el primer elemento no se printea nada aunque vayan terminando los otros porque es secuencial
    for f in concurrent.futures.as_completed(results):
        print(f.result())
    
    for f in results:
        print(f.result())

#loopeando con simple threads
# threads = []

# for i in range(10):
#     t = threading.Thread(target=do_something, args=(i,))
#     t.start()
#     threads.append(t)

# for t in threads:
#     t.join()