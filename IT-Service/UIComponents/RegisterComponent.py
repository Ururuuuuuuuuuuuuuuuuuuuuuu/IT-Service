from PyQt5 import QtWidgets

from DatabaseConnector import DatabaseThread
from UIWidgets.RegisterDialog import Ui_Register

from UIComponents.LoginComponent import LoginComponent


class RegisterComponent(QtWidgets.QDialog):
    def __init__(self):
        super(RegisterComponent, self).__init__()
        self.collection = None
        self.ui = Ui_Register()
        self.ui.setupUi(self)
        self.register_model = {
            "email": "",
            "name": "",
            "password": "",
            "user_root": "client"
        }

        self.db_thread = DatabaseThread()
        self.db_thread.connection_signal.connect(self.setup_database_connection)
        self.db_thread.start()

        self.ui.register_button.clicked.connect(self.register_button_clicked)
        self.ui.login_redirect_button.clicked.connect(self.redirect_to_login)

    def setup_database_connection(self, client):
        database = client["IT-Service"]
        self.collection = database["users"]

    def register_button_clicked(self):
        self.register_model["email"] = self.ui.email_line.text()
        self.register_model["name"] = self.ui.name_line.text()
        self.register_model["password"] = self.ui.password_line.text()

        if not all(self.register_model.values()):
            print("Заполните все поля")
            return

        self.collection.insert_one(self.register_model)
        self.redirect_to_login()

    def redirect_to_login(self):
        self.close()
        component = LoginComponent()
        component.exec()

