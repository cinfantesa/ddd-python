import uuid
from uuid import UUID

import pytest

from domain.project import Project


def test_raise_error_when_id_is_missing():
    with pytest.raises(ValueError):
        Project(None, 'name')


def test_creates_project():
    id : str = str(uuid.uuid4())
    project: Project = Project(id, 'name')

    assert project.id == id
    assert project.name == 'name'
