from PyQt5 import QtWidgets
import sys

from UIComponents.RegisterComponent import RegisterComponent

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    component = RegisterComponent()
    component.exec()
    sys.exit(app.exec_())
