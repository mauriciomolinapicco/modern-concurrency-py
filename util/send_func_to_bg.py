from uuid import uuid4
import time
from flask_restx import Api, Resource
from threading import Thread
import flask

m_app = flask.Blueprint("m_app", __name__)

api = Api(
    m_app,
    title="Services API",
    description="Services to be consumed by FPS Fintech BI Users",
)


TASKS = {}  # task_id -> {"thread": Thread, "status": "queued|running|completed|failed", "error": None}

def start_background_thread(target, *args, **kwargs):
    """
    considerar cambio a multiprocessing para que sea realmente independiente del proceso principal
    """
    task_id = str(uuid4())
    TASKS[task_id] = {"thread": None, "status": "queued", "error": None}

    def wrapper():
        TASKS[task_id]["status"] = "running"
        try:
            target(*args, **kwargs)
            TASKS[task_id]["status"] = "completed"
        except Exception as e:
            TASKS[task_id]["status"] = "failed"
            TASKS[task_id]["error"] = str(e)

    t = Thread(target=wrapper, daemon=False)
    TASKS[task_id]["thread"] = t
    t.start()
    return task_id

#endpoint start process
class ProcessInput(Resource):
    """
    Ejecutada por job automatico. Inicia el flujo de Verdi por cada archivo no procesado
    """
    def post(self):
        task_id = start_background_thread(procesar_archivos, "param1", "param2")
        return {"task_id": task_id}, 202


def procesar_archivos(a,b):
    time.sleep(5)
    return f"Func ejemplo: recibidos {a} y {b} y procesados en bg"

#endpoint check health of task
class TaskStatus(Resource):
    """ consultar estado de tarea """
    def get(self, task_id):
        task = TASKS.get(task_id)
        if not task:
            return {"error": "Task not found"}, 404
        return {
            "id": task_id,
            "status": getattr(task, "status", None),
            "message": getattr(task, "message", None)
        }, 200


api.add_resource(ProcessInput, '/input') 
api.add_resource(TaskStatus, '/tasks/<task_id>')
