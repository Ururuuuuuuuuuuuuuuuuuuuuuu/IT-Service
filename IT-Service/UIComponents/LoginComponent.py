from PyQt5 import QtWidgets, QtCore

import Redirector
from DatabaseConnector import DatabaseThread
from UIComponents.ClientComponent import ClientComponent
from UIComponents.MasterComponent import MasterComponent


from UIWidgets.LoginDialog import Ui_Login
from User import User


class LoginComponent(QtWidgets.QDialog):
    def __init__(self):
        super(LoginComponent, self).__init__()
        self.collection = None
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.login_model = {
            "email": None,
            "password": None
        }

        self.db_thread = DatabaseThread()
        self.db_thread.connection_signal.connect(self.setup_database_connection)
        self.db_thread.start()

        self.user = None

        self.ui.login_button.clicked.connect(self.login_button_clicked)
        self.ui.redirect_button_register.clicked.connect(self.redirect_to_register)

    def setup_database_connection(self, client):
        database = client["IT-Service"]
        self.collection = database["users"]

    def login_button_clicked(self):
        self.login_model["email"] = self.ui.email_line.text()
        self.login_model["password"] = self.ui.password_line.text()

        if not all(self.login_model.values()):
            print("Заполните все поля")
            return

        try:
            data = self.collection.find_one(self.login_model)
        except Exception as e:
            print(e)

        if data:
            print("Вы успешно вошли")
            self.user = User(data["email"], data["name"], data["user_root"])

            print(data)

            if self.user.user_root == "admin":
                self.redirect_to_master(self.user)
            elif self.user.user_root == "client":
                self.redirect_to_client(self.user)
        else:
            print("Неверный логин или пароль")



    def redirect_to_master(self, user):
        self.close()
        component = MasterComponent(user)
        component.exec()

    def redirect_to_client(self, user):
        self.close()
        component = ClientComponent(user)
        component.exec()

    def redirect_to_register(self):
        from UIComponents.RegisterComponent import RegisterComponent
        self.close()
        component = RegisterComponent()
        component.exec()