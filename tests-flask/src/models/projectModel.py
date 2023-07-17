from .db import db
from .abstractModel import AbstractModel


class ProjectModel(AbstractModel):
    _collection = db["projects"]

    def __init__(self, json_deadline):
        super().__init__(json_deadline)

    @classmethod
    def separate_projects(cls):
        tasks = [task.to_dict() for task in cls.find()]
        projects = {}
        for task in tasks:
            project_id = task["id_project"]
            if project_id not in projects:
                projects[project_id] = []
            projects[project_id].append(task)
        return [project for project in projects.values()]

    def to_dict(self):
        return {
            '_id': str(self.deadline['_id']),
            'id_project': self.deadline['idProject'],
            'name': self.deadline['name'],
            'task': self.deadline['task'],
            'status': self.deadline['status'],
            'percentage_de_conclusao': self.deadline['completionPercentage'],
            'description_task': self.deadline['descriptionTask'],
            'deadline': self.deadline['deadline'],
            'responsible': self.deadline['responsible']
        }
