from concurrent.futures import ThreadPoolExecutor
import time

def worker(num1, num2):
    print(f"Proceso demorado para el numero {num1}")
    time.sleep(2)
    return num1 + num2

#estoy definiendo que puede tener como maximo dos threads
pool = ThreadPoolExecutor(2)
resultado1 = pool.submit(worker, 7, 2) # es como una promesa o un objeto asincrono
resultado2 = pool.submit(worker, 4, 2)
resultado3 = pool.submit(worker, 67, 2)
resultado4 = pool.submit(worker, 11, 2)
resultado5 = pool.submit(worker, 77, 2)

# print(f"resultado del 5: {resultado5.result()}") 
#hacer .result() es bloqueante por lo que la siguiente linea no se ejecuta hasta que se obtenga el resultado

"""Si queremos prevenir que se 'espere' a que termine un resultado podemos hacer"""
print(resultado4.done()) #booleano
if resultado4.done():
    print(f"Termino el resultado 4: {resultado4.result}")

time.sleep(5)
print(resultado4.done())
if resultado4.done():
    print(f"Termino el resultado 4: {resultado4.result()}")

print("hola mundo")


#terminar el pool para que no se puedan hacer mas submits
pool.shutdown(wait=True) #parametro wait opcional, espera a que todos terminen de ejecutarse
resultado6 = pool.submit(worker, 77, 2) #excepciondef multi_thread_handler(query_result, ruta_bucket_global, root_path):
