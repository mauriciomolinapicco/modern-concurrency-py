# Modern Python Concurrency 

Este repositorio explora patrones y técnicas modernas de concurrencia en Python, incluyendo:

- **Threading y multiprocessing**
- **Async/await y asyncio**
- **Casos reales de uso (I/O bound, web, DB)**
- **Comparativas de rendimiento**
- **Patrones de diseño concurrente**

## 🧱 Estructura

- `01_threads_basics/`: Fundamentos de `threading.Thread`, `Lock`, y `ThreadPoolExecutor`.
- `02_asyncio_basics/`: Uso de `async def`, `await`, `gather`, y el event loop.
- `03_real_use_cases/`: Scripts aplicados a scraping, file uploads y consultas DB.
- `04_perf_and_benchmarks/`: Medición de rendimiento entre modelos.
- `05_design_patterns/`: Patrones como producer-consumer, fan-out/fan-in, etc.
- `utils/`: Herramientas auxiliares como fake APIs o temporizadores.

## 🧪 Requisitos

Python 3.11+ recomendado.

```bash
pip install -r requirements.txt
