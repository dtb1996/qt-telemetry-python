from dataclasses import dataclass
from enum import Enum


class SensorStatus(Enum):
    OK = "OK"
    WARNING = "WARNING"
    ERROR = "ERROR"


@dataclass(frozen=True)
class SensorData:
    name: str
    value: float
    unit: str
    status: SensorStatus
