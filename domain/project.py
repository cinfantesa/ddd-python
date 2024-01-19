class Project:
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name

    @property
    def id(self) -> str:
        return self.__id

    @property
    def name(self):
        return self.__name

    @id.setter
    def id(self, id: str):
        if id is None:
            raise ValueError('Field id cannot be set to empty')
        self.__id = id

    @name.setter
    def name(self, name: str):
        if name is None:
            raise ValueError('Field name cannot be set to empty')
        self.__name = name

    def __eq__(self, other):
        if not isinstance(other, Project):
            return False
        return self.id == other.id and self.name == other.name
