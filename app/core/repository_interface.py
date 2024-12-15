# app/core/repository_interface.py
from abc import ABC, abstractmethod
from .entities import TankStatus

class RepositoryInterface(ABC):
    @abstractmethod
    def get_tank_status(self) -> TankStatus:
        pass

    @abstractmethod
    def update_tank_status(self, tank_status: TankStatus):
        pass
