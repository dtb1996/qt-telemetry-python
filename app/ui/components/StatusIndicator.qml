import QtQuick

Rectangle {
    id: root
    width: 12
    height: 12
    radius: 6

    property string status

    color: status === "OK"      ? "#4caf50" :
           status === "WARNING" ? "#ff9800" :
           status === "ERROR"   ? "#f44336" : "#9e9e9e"
}
