from domain.project import Project
from domain.project_repository import ProjectRepository

class LocalProjectRepository(ProjectRepository):
    def __init__(self):
        self.__projects = []

    def save(self, project: Project) -> None:
        self.__projects.append(project)

    def exists(self, id: str) -> bool:
        return any(p.id == id for p in self.__projects)
