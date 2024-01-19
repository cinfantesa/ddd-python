from logging import Logger

from application.create_project.create_project import CreateProject
from container import obj_graph
from infrastructure.logging.json_logger import JsonLogger

if __name__ == '__main__':
    logger:Logger = obj_graph.provide(JsonLogger)
    logger.info("Started..")
    create_project = obj_graph.provide(CreateProject)
    create_project.create('name')
