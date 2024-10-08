from src.dolphine_app import DolphineBackend
from src.api import api_v1
from fastapi import FastAPI
from src.database.worker import DBWorker

if __name__ == "__main__":
    dolphine_fst = DolphineBackend()
    app: FastAPI = dolphine_fst.back_app

    @app.on_event("startup")
    async def startup():
        await DBWorker.create_tables()

    # api_v1
    dolphine_fst.add_router(api_v1)

    dolphine_fst.start_project()
