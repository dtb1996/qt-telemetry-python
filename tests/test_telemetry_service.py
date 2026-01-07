from PySide6.QtTest import QSignalSpy

from app.services.telemetry_service import TelemetryService
from app.models.sensor_data import SensorData


def test_telemetry_service_emits_data():
    service = TelemetryService(update_interval_ms=10)

    spy = QSignalSpy(service.telemetry_updated)

    # Wait up to 100ms for signal
    assert spy.wait(100)

    assert spy.count() == 1

    args = spy.at(0)
    sensors = args[0]

    assert isinstance(sensors, list)
    assert len(sensors) > 0

    for sensor in sensors:
        assert isinstance(sensor, SensorData)
