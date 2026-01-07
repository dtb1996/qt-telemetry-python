from PySide6.QtTest import QSignalSpy

from app.services.telemetry_service import TelemetryService
from app.viewmodels.dashboard_vm import DashboardViewModel
from app.models.sensor_data import SensorData, SensorStatus


def test_dashboard_viewmodel_initial_population():
    service = TelemetryService(update_interval_ms=999999)
    vm = DashboardViewModel(service)

    spy = QSignalSpy(vm.sensorsChanged)

    sensors = [
        SensorData("A", 1.0, "u", SensorStatus.OK),
        SensorData("B", 2.0, "u", SensorStatus.WARNING),
    ]

    service.telemetry_updated.emit(sensors)

    assert spy.count() == 1
    assert len(vm.sensors) == 2
    assert vm.sensors[0].name == "A"


def test_dashboard_viewmodel_updates_existing_vms():
    service = TelemetryService(update_interval_ms=999999)
    vm = DashboardViewModel(service)

    initial = [
        SensorData("A", 1.0, "u", SensorStatus.OK),
    ]
    updated = [
        SensorData("A", 99.0, "u", SensorStatus.ERROR),
    ]

    service.telemetry_updated.emit(initial)
    service.telemetry_updated.emit(updated)

    assert len(vm.sensors) == 1
    assert vm.sensors[0].value == 99.0
    assert vm.sensors[0].status == "ERROR"
