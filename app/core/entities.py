from dataclasses import dataclass

@dataclass
class TankStatus:
    level: int
    activations: int
    deactivations: int
    usage: float
