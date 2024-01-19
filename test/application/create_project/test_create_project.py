from unittest.mock import MagicMock

import pytest

from application.create_project.create_project import CreateProject
from application.create_project.create_project_command import CreateProjectCommand
from domain.project import Project
from domain.project_already_exists_error import ProjectAlreadyExistsError


@pytest.fixture
def mocks(mocker):
    return {
        'idGenerator': mocker.patch('domain.id_generator'),
        'projectRepository': mocker.patch('domain.project_repository')
    }


@pytest.fixture
def subject(mocks):
    return CreateProject(mocks['projectRepository'], mocks['idGenerator'])


id: str = 'id'


def test_generates_id(mocks, subject):
    mocks['idGenerator'].generate = MagicMock()
    mocks['projectRepository'].exists = MagicMock(return_value=False)

    command: CreateProjectCommand = CreateProjectCommand('name')
    subject.create(command)

    mocks['idGenerator'].generate.assert_called_once()


def test_calls_repository_to_check_if_project_exists(mocks, subject):
    mocks['idGenerator'].generate = MagicMock(return_value=id)
    mocks['projectRepository'].exists = MagicMock(return_value=False)

    command: CreateProjectCommand = CreateProjectCommand('name')
    subject.create(command)

    mocks['projectRepository'].exists.assert_called_once()
    mocks['projectRepository'].exists.assert_called_once_with(id)


def test_raise_error_when_project_already_exists(mocks, subject):
    mocks['idGenerator'].generate = MagicMock()
    mocks['projectRepository'].exists = MagicMock(return_value=True)

    command: CreateProjectCommand = CreateProjectCommand('name')
    with pytest.raises(ProjectAlreadyExistsError) as exception:
        subject.create(command)

    assert str(exception.value) == 'Project already exists'


def test_saves_the_project(mocks, subject):
    mocks['idGenerator'].generate = MagicMock(return_value=id)
    mocks['projectRepository'].exists = MagicMock(return_value=False)
    mocks['projectRepository'].save = MagicMock()

    command: CreateProjectCommand = CreateProjectCommand('name')
    subject.create(command)

    expectedProject: Project = Project(id, 'name')
    mocks['projectRepository'].save.assert_called_once_with(expectedProject)
