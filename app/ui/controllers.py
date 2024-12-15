# app/ui/controllers.py
from app.core.use_cases import TankUseCase

class TankController:
    def __init__(self, tank_use_case: TankUseCase):
        self.tank_use_case = tank_use_case

    def get_status(self):
        return self.tank_use_case.get_status()

    def activate_valve(self):
        self.tank_use_case.update_status(activate=True)

    def deactivate_valve(self):
        self.tank_use_case.update_status(activate=False)
