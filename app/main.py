# This Python file uses the following encoding: utf-8
import sys
from pathlib import Path

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

from app.services.telemetry_service import TelemetryService
from app.viewmodels.dashboard_vm import DashboardViewModel


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)

    telemetry_service = TelemetryService()
    dashboard_vm = DashboardViewModel(telemetry_service)

    engine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty("DashboardViewModel", dashboard_vm)

    qml_file = Path(__file__).resolve().parent / "ui/main.qml"
    engine.load(qml_file)
    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())
