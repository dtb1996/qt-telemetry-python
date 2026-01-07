from PySide6.QtTest import QSignalSpy

from app.models.sensor_data import SensorData, SensorStatus
from app.viewmodels.sensor_vm import SensorViewModel


def test_sensor_viewmodel_properties():
    data = SensorData(
        name="Speed",
        value=42.5,
        unit="km/h",
        status=SensorStatus.OK,
    )

    vm = SensorViewModel(data)

    assert vm.name == "Speed"
    assert vm.value == 42.5
    assert vm.unit == "km/h"
    assert vm.status == "OK"


def test_sensor_viewmodel_emits_on_update():
    data1 = SensorData("Temp", 20.0, "°C", SensorStatus.OK)
    data2 = SensorData("Temp", 95.0, "°C", SensorStatus.ERROR)

    vm = SensorViewModel(data1)
    spy = QSignalSpy(vm.dataChanged)

    vm.update(data2)

    assert spy.count() == 1
    assert vm.value == 95.0
    assert vm.status == "ERROR"
