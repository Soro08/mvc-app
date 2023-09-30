from apps.views import TaskView
from apps.models import Task
from apps.manager import TaskManager


class TaskController:
    def __init__(self):
        self.task_views = TaskView()
        self.task_manager = TaskManager("task.db")

    def create(self):
        task_data = self.task_views.get_task_data()
        task = Task(*task_data)
        self.task_manager.add_task(task.serializer())

    def update(self):
        pass

    def display(self):
        pass

    def delete(self):
        pass
