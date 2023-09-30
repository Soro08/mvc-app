from tinydb import TinyDB, Query


class TaskManager:
    def __init__(self, db_path):
        self.db = TinyDB(db_path)
        self.tasks_table = self.db.table("tasks")

    def add_task(self, task):
        self.tasks_table.insert(task)

    def get_all_tasks(self):
        return self.tasks_table.all()

    def mark_task_as_completed(self, task_id):
        self.tasks_table.update({"completed": True}, doc_ids=[task_id])

    def delete_task(self, task_id):
        self.tasks_table.remove(doc_ids=[task_id])
