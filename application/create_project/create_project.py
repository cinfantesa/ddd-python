from application.create_project.create_project_command import CreateProjectCommand
from domain.id_generator import IdGenerator
from domain.project import Project
from domain.project_already_exists_error import ProjectAlreadyExistsError
from domain.project_repository import ProjectRepository


class CreateProject:
    def __init__(self, project_repository: ProjectRepository, id_generator: IdGenerator):
        self._project_repository = project_repository
        self._id_generator = id_generator

    def create(self, command: CreateProjectCommand) -> None:
        id: str = self._id_generator.generate()
        if self._project_repository.exists(id):
            raise ProjectAlreadyExistsError()

        project = Project(id, command.name)
        self._project_repository.save(project)


