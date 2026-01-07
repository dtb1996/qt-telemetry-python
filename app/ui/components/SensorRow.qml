import QtQuick
import QtQuick.Layouts
import QtQuick.Controls

Rectangle {
    id: root
    width: parent.width
    height: 48
    radius: 4
    color: "#2b2b2b"

    property string sensorName
    property real sensorValue
    property string sensorUnit
    property string sensorStatus

    RowLayout {
        anchors.fill: parent
        anchors.margins: 8
        spacing: 12

        StatusIndicator {
            status: sensorStatus
        }

        Label {
            text: sensorName
            color: "#ffffff"
            Layout.fillWidth: true
        }

        Label {
            text: sensorValue.toFixed(1) + " " + sensorUnit
            color: "#ffffff"
            horizontalAlignment: Text.AlignRight
        }
    }
}
