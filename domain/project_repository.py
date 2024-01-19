from abc import ABC, abstractmethod

from domain.project import Project


class ProjectRepository(ABC):
    @abstractmethod
    def save(self, project: Project) -> None: raise NotImplementedError

    @abstractmethod
    def exists(self, id: str) -> bool: raise NotImplementedError
