from PySide6.QtCore import QObject, Property, Signal

from app.services.telemetry_service import TelemetryService
from app.viewmodels.sensor_vm import SensorViewModel
from app.models.sensor_data import SensorData


class DashboardViewModel(QObject):
    sensorsChanged = Signal()

    def __init__(self, telemetry_service: TelemetryService, parent=None):
        super().__init__(parent)

        self._telemetry_service = telemetry_service
        self._sensors: list[SensorViewModel] = []

        self._telemetry_service.telemetry_updated.connect(self._on_telemetry_updated)

    def _on_telemetry_updated(self, sensors: list[SensorData]) -> None:
        if not self._sensors:
            self._sensors = [
                SensorViewModel(sensor, self)
                for sensor in sensors
            ]
        else:
            for vm, sensor in zip(self._sensors, sensors):
                vm.update(sensor)

        self.sensorsChanged.emit()

    @Property(list, notify=sensorsChanged)
    def sensors(self) -> list[SensorViewModel]:
        return self._sensors
