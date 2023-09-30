from .task_controller import TaskController
from apps.views import TaskView


class MainController:
    def __init__(self):
        self.task_controller = TaskController()
        self.task_views = TaskView()

    def start(self):
        self.menu()

    def menu(self):
        choice = self.task_views.menu()
        if choice == 1:
            self.task_controller.create()
        elif choice == 2:
            self.task_controller.update()
        elif choice == 3:
            self.task_controller.display()
        elif choice == 4:
            self.task_controller.delete()
        else:
            print("Invalid choice")
