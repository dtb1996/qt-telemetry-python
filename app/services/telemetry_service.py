import random
from PySide6.QtCore import QObject, Signal, QTimer

from app.models.sensor_data import SensorData, SensorStatus


class TelemetryService(QObject):
    """
    Simluates a telemetry data source.
    Emits updated sensor data at a fixed interval
    """

    telemetry_updated = Signal(list) # List[SensorData]

    def __init__(self, update_interval_ms: int = 1000, parent=None):
        super().__init__(parent)

        self._timer = QTimer(self)
        self._timer.timeout.connect(self._generate_telemetry)
        self._timer.start(update_interval_ms)

    def _generate_telemetry(self) -> None:
        sensors = [
            self._make_sensor("Speed", "km/h", 0, 120),
            self._make_sensor("Temperature", "°C", -20, 120),
            self._make_sensor("Battery", "%", 0, 100),
        ]

        self.telemetry_updated.emit(sensors)

    def _make_sensor(self, name: str, unit: str, min_val: float, max_val: float) -> SensorData:
        value = random.uniform(min_val, max_val)

        if value < min_val * 0.1 or value > max_val * 0.9:
            status = SensorStatus.ERROR
        elif value < min_val * 0.2 or value > max_val * 0.8:
            status = SensorStatus.WARNING
        else:
            status = SensorStatus.OK

        return SensorData(
            name=name,
            value=round(value, 2),
            unit=unit,
            status=status
        )
