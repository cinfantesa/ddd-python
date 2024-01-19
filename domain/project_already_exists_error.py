class ProjectAlreadyExistsError(Exception):
    def __init__(self):
        super().__init__('Project already exists')
