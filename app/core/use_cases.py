# app/core/use_cases.py
from .repository_interface import RepositoryInterface
from .entities import TankStatus

class TankUseCase:
    def __init__(self, repository: RepositoryInterface):
        self.repository = repository

    def get_status(self) -> TankStatus:
        return self.repository.get_tank_status()

    def update_status(self, activate: bool):
        status = self.repository.get_tank_status()
        if activate:
            status.activations += 1
            status.level = max(0, status.level - 10)
        else:
            status.deactivations += 1
            status.level = min(100, status.level + 10)
        status.usage += 10
        self.repository.update_tank_status(status)
