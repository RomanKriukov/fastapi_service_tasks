
from fastapi import FastAPI
from contextlib import asynccontextmanager

from database import create_tables, drop_tables
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await drop_tables()
    print("База очищена")
    await create_tables()
    print("База готова до роботи")
    yield
    print("Вимкнення")

app = FastAPI(lifespan=lifespan)
app.include_router(router=tasks_router)


tasks = []




