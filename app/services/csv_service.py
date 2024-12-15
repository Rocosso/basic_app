import csv
import os
from app.core.entities import TankStatus

class CSVService:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.ensure_file_exists()

    def ensure_file_exists(self):
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["level", "activations", "deactivations", "usage"])
                writer.writeheader()
                writer.writerow({"level": 50, "activations": 0, "deactivations": 0, "usage": 0.0})

    def read_tank_status(self):
        with open(self.file_path, "r") as file:
            reader = csv.DictReader(file)
            last_row = list(reader)[-1]
            return TankStatus(
                level=int(last_row["level"]),
                activations=int(last_row["activations"]),
                deactivations=int(last_row["deactivations"]),
                usage=float(last_row["usage"])
            )

    def write_tank_status(self, tank_status: TankStatus):
        with open(self.file_path, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["level", "activations", "deactivations", "usage"])
            writer.writeheader()
            writer.writerow({
                "level": tank_status.level,
                "activations": tank_status.activations,
                "deactivations": tank_status.deactivations,
                "usage": tank_status.usage
            })
