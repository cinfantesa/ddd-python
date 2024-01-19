import pinject

# from application.create_project.create_project import CreateProject
# from infrastructure.logging.json_logger import JsonLogger
# from infrastructure.persistence.local_project_repository import LocalProjectRepository
# from infrastructure.uuid_id_generator import UUIDIdGenerator
#

# class ApplicationServices(pinject.BindingSpec):
#     def configure(self, bind):
#         bind('create_project', to_class=CreateProject)
#
#
# class DomainServices(pinject.BindingSpec):
#     def configure(self, bind):
#         bind('id_generator', to_class=UUIDIdGenerator)
#         bind('project_repository', to_class=LocalProjectRepository)
#
#
# class InfrastructureServices(pinject.BindingSpec):
#     def configure(self, bind):
#         bind('logger', to_class=JsonLogger)


# obj_graph = pinject.new_object_graph(modules=None, binding_specs=[
#     ApplicationServices(),
#     DomainServices(),
#     InfrastructureServices()
# ])

obj_graph = pinject.new_object_graph()
