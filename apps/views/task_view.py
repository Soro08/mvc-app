class TaskView:
    def __init__(self):
        pass

    def menu(self):
        print(
            "1. Creer un tache \n2. Modifier une tache \n3. Afficher les taches \n4. Supprimer une tache"
        )
        choice = int(input("Entrer votre choix: "))
        return choice

    def get_task_data(self):
        title = input("Titre: ")
        description = input("Description: ")
        due_date = input("Date limite: ")
        completed = input("Status: ")
        return title, description, due_date, completed
