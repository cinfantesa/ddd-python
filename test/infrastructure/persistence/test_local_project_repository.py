import pytest

from domain.project import Project
from infrastructure.persistence.local_project_repository import LocalProjectRepository


@pytest.fixture
def subject():
    return LocalProjectRepository()


def describe_exists():
    def returns_false_when_project_does_not_exist(subject):
        assert subject.exists('id') == False

    def returns_true_when_project_exists(subject):
        subject.save(Project('id', 'name'))
        assert subject.exists('id') == True


def describe_save():
    def saves_the_project(subject):
        project = Project('id', 'name')
        subject.save(project)
        assert subject.exists('id') == True
