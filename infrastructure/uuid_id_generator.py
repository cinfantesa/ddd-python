import uuid

from domain.id_generator import IdGenerator


class UUIDIdGenerator(IdGenerator):
    def generate(self) -> str:
        return str(uuid.uuid4())
