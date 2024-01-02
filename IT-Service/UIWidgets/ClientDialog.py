# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UITemplates/client.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Client(object):
    def setupUi(self, Client):
        Client.setObjectName("Client")
        Client.resize(400, 600)
        Client.setMinimumSize(QtCore.QSize(400, 600))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Client)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.order_line = QtWidgets.QLineEdit(Client)
        self.order_line.setStyleSheet("min-height:30px;")
        self.order_line.setText("")
        self.order_line.setObjectName("order_line")
        self.verticalLayout.addWidget(self.order_line)
        self.equipment_line = QtWidgets.QLineEdit(Client)
        self.equipment_line.setStyleSheet("min-height:30px;")
        self.equipment_line.setObjectName("equipment_line")
        self.verticalLayout.addWidget(self.equipment_line)
        self.descriprion_area = QtWidgets.QTextBrowser(Client)
        self.descriprion_area.setMinimumSize(QtCore.QSize(0, 100))
        self.descriprion_area.setMaximumSize(QtCore.QSize(16777215, 250))
        self.descriprion_area.setReadOnly(False)
        self.descriprion_area.setObjectName("descriprion_area")
        self.verticalLayout.addWidget(self.descriprion_area)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.order_button = QtWidgets.QPushButton(Client)
        self.order_button.setObjectName("order_button")
        self.horizontalLayout.addWidget(self.order_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Client)
        QtCore.QMetaObject.connectSlotsByName(Client)

    def retranslateUi(self, Client):
        _translate = QtCore.QCoreApplication.translate
        Client.setWindowTitle(_translate("Client", " "))
        self.order_line.setPlaceholderText(_translate("Client", "Техніка"))
        self.equipment_line.setPlaceholderText(_translate("Client", "Модель"))
        self.descriprion_area.setPlaceholderText(_translate("Client", "Опишіть вашу проблему"))
        self.order_button.setText(_translate("Client", "Зробити замовлення"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Client = QtWidgets.QDialog()
    ui = Ui_Client()
    ui.setupUi(Client)
    Client.show()
    sys.exit(app.exec_())