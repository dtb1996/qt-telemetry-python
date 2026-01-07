from PySide6.QtCore import QObject, Property, Signal

from app.models.sensor_data import SensorData


class SensorViewModel(QObject):
    dataChanged = Signal()

    def __init__(self, sensor: SensorData, parent=None):
        super().__init__(parent)
        self._sensor = sensor

    def update(self, sensor: SensorData) -> None:
        self._sensor = sensor
        self.dataChanged.emit()

    @Property(str, notify=dataChanged)
    def name(self) -> str:
        return self._sensor.name

    @Property(float, notify=dataChanged)
    def value(self) -> float:
        return self._sensor.value

    @Property(str, notify=dataChanged)
    def unit(self) -> str:
        return self._sensor.unit

    @Property(str, notify=dataChanged)
    def status(self) -> str:
        return self._sensor.status.value
