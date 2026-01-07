import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import "components"

ApplicationWindow {
    id: mainWindow
    width: 640
    height: 480
    visible: true
    title: qsTr("Telemetry Dashboard")

    // Item {
    //     anchors.fill: parent

    ColumnLayout {
        anchors.fill: parent
        spacing: 12
        anchors.margins: 16

        Label {
            text: qsTr("Live Telemetry")
            font.pixelSize: 22
            Layout.alignment: Qt.AlignHCenter
        }

        Rectangle {
            Layout.fillWidth: true
            Layout.fillHeight: true
            radius: 6
            color: "#1e1e1e"

            ListView {
                id: sensorList
                anchors.fill: parent
                anchors.margins: 12
                spacing: 8

                model: DashboardViewModel.sensors

                delegate: SensorRow {
                    sensorName: modelData.name
                    sensorValue: modelData.value
                    sensorUnit: modelData.unit
                    sensorStatus: modelData.status
                }
            }
        }
    }
    // }

    Shortcut {
        sequence: "Escape"
        onActivated: Qt.quit()
    }

    Shortcut {
        sequence: "Alt+Return"
        onActivated: mainWindow.visibility = mainWindow.visibility === Window.FullScreen ? Window.Windowed : Window.FullScreen
    }
}
