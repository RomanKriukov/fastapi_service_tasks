from typing import Annotated

from fastapi import APIRouter, Depends
from starlette import status

from repository import TaskRepository
from schemas import STaskAdd, STask, STaskId

router = APIRouter(
    prefix="/tasks",
    tags=["Таски"]
)


@router.post("", status_code=status.HTTP_201_CREATED, summary="Додавання завдань")
async def add_task(task: Annotated[STaskAdd, Depends()]) -> STaskId:
    task_id = await TaskRepository.add_one(data=task)
    return task_id


@router.get("", summary="Отримання списку всіх завдань")
async def get_tasks() -> list[STask]:
    return await TaskRepository.find_all()
