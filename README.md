# Qt Telemetry Dashboard (Python / PySide6)

A Python Qt 6 application demonstrating a Service + ViewModel architecture with QML frontend.

## Overview

The **Qt Telemetry Dashboard** is a small desktop application built with **PySide6 (Qt for Python)** and **QML**. It demonstrates:
- Service + ViewModel architecture (MVVM)
- Signal-driven UI updates
- Python-based Qt development workflow
- Unit testing of Qt signals and ViewModels
- Clean separation of concerns between UI and logic

The app simulates real-time telemetry by generating random sensor data (speed, temperature, battery) and displays it in a responsive QML dashboard.

## Features

- Real-time telemetry simulation
- Reactive updates via signals
- MVVM pattern: services provide data, ViewModels expose it to QML
- Unit-tested Python code, including:
    - Signal emission
    - ViewModel property updates
    - Data integrity
- QML UI displaying sensor data in a clean dashboard layout

## Project Structure

```bash
app/
├── main.py                   # Application entry point
├── services/
│   └── telemetry_service.py  # Generates sensor data and emits signals
├── viewmodels/
│   ├── dashboard_vm.py       # Connects service data to QML
│   └── sensor_vm.py          # Wraps individual sensor data
├── models/
│   └── sensor_data.py        # SensorData and SensorStatus definitions
└── ui/
    ├── Main.qml              # Dashboard UI
    └── components
        ├── SensorRow.qml
        └── StatusIndicator.qml
tests/
│   ├── test_telemetry_service.py
│   ├── test_dashboard_vm.py
│   └── test_sensor_vm.py
├── pyproject.toml
├── README.md
└── .gitignore
```

### Flow:

```bash
TelemetryService → DashboardViewModel → QML UI
```

- `TelemetryService` generates data and emits a signal.
- `DashboardViewModel` listens to the service signal and updates `SensorViewModel`s.
- QML binds to the ViewModels for dynamic UI updates.

## Requirements

- Python 3.10+  
- PySide6
- pytest (for unit tests)

Install dependencies:

```bash
pip install PySide6 pytest
```

## Running the App

**Run as a module (recommended for correct imports):**

```bash
python -m app.main
```

Running `python app/main.py` directly may break imports due to package structure.

## Running Tests

```bash
pytest -v
```

All tests include signal emission checks using `QSignalSpy` and validate ViewModel behavior.
