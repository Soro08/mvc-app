from tinydb import TinyDB, Query, where


class Task:
    def __init__(self, title, description, due_date, completed):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = completed

    def serializer(self):
        return {
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "completed": self.completed,
        }
