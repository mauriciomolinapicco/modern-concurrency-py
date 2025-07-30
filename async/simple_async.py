import asyncio
import random

# 👇 Esta es una función "async", es decir, una corrutina.
async def saludar(nombre):
    print(f"👋 Hola {nombre}")
    await asyncio.sleep(random.uniform(0.5, 2))  # simula espera no bloqueante
    print(f"✅ Chau {nombre}")

# 👇 Otra corrutina más simple
async def cuenta_regresiva(n):
    while n > 0:
        print(f"⏳ Contando: {n}")
        await asyncio.sleep(1)
        n -= 1
    print("🚀 ¡Despegue!")

# 👇 Corrutina que espera otra
async def main():
    print("🏁 Inicio del programa")

    # Lanzamos varias tareas concurrentes
    tarea1 = asyncio.create_task(saludar("Alice"))
    tarea2 = asyncio.create_task(saludar("Bob"))
    tarea3 = asyncio.create_task(cuenta_regresiva(3))

    # Esperamos a que todas terminen
    await tarea1
    await tarea2
    await tarea3

    print("🏁 Fin del programa")

# Este es el entry point
if __name__ == "__main__":
    asyncio.run(main())
