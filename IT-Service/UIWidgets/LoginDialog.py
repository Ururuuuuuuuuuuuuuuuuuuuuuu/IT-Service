# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UITemplates/login.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(442, 500)
        Login.setMinimumSize(QtCore.QSize(400, 500))
        Login.setStyleSheet("QDialog{\n"
"    background-color:white;\n"
"}\n"
"\n"
"QLabel{\n"
"    font-family: Arial;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: #ed5684;\n"
"    color: white;\n"
"    min-height:30px;\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"    border: 1px solid #d0d0d0;\n"
"    border-radius: 20px;\n"
"}")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Login)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.asdasdaa = QtWidgets.QFrame(Login)
        self.asdasdaa.setObjectName("asdasdaa")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.asdasdaa)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.asdasdaa)
        self.label_3.setMinimumSize(QtCore.QSize(0, 70))
        self.label_3.setStyleSheet("font-size:26px;\n"
"color: #ed5684;")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.asdasdaa)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.email_line = QtWidgets.QLineEdit(self.asdasdaa)
        self.email_line.setStyleSheet("min-height:30px;")
        self.email_line.setText("")
        self.email_line.setPlaceholderText("")
        self.email_line.setObjectName("email_line")
        self.verticalLayout_4.addWidget(self.email_line)
        self.verticalLayout_6.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(-1, -1, -1, 5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.asdasdaa)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.password_line = QtWidgets.QLineEdit(self.asdasdaa)
        self.password_line.setStyleSheet("min-height:30px;")
        self.password_line.setPlaceholderText("")
        self.password_line.setObjectName("password_line")
        self.verticalLayout_5.addWidget(self.password_line)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout.addLayout(self.verticalLayout_6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.redirect_button_register = QtWidgets.QPushButton(self.asdasdaa)
        self.redirect_button_register.setObjectName("redirect_button_register")
        self.horizontalLayout.addWidget(self.redirect_button_register)
        self.login_button = QtWidgets.QPushButton(self.asdasdaa)
        self.login_button.setObjectName("login_button")
        self.horizontalLayout.addWidget(self.login_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.asdasdaa, 0, QtCore.Qt.AlignVCenter)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Dialog"))
        self.label_3.setText(_translate("Login", "Вхід"))
        self.label.setText(_translate("Login", "Номер телефону"))
        self.label_2.setText(_translate("Login", "Пароль"))
        self.redirect_button_register.setText(_translate("Login", "Перейти до реєстрації"))
        self.login_button.setText(_translate("Login", "Увійти"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QDialog()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())
