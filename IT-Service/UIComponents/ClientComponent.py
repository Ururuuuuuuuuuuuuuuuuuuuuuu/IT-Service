from PyQt5 import QtWidgets

from DatabaseConnector import DatabaseThread
from UIWidgets.ClientDialog import Ui_Client


class ClientComponent(QtWidgets.QDialog):
    def __init__(self, user):
        super(ClientComponent, self).__init__()
        self.ui = Ui_Client()
        self.ui.setupUi(self)

        self.db_thread = DatabaseThread()
        self.db_thread.connection_signal.connect(self.setup_database_connection)
        self.db_thread.start()

        self.user = user

        self.ui.order_button.clicked.connect(self.order_button_clicked)
        self.ui.redirect_button_login.clicked.connect(self.redirect_to_login)

    def setup_database_connection(self, client):
        client = client
        database = client["IT-Service"]
        self.collection = database["orders"]

    def order_button_clicked(self):
        order = self.ui.order_line.text()
        equipment = self.ui.equipment_line.text()
        description = self.ui.descriprion_area.toPlainText()

        if not all([order, equipment, description]):
            print("Заполните все поля")
            return

        try:
            print({"nameorder": order, "equipment": equipment, "description": description, "customer": self.user.name, "email": self.user.email})
            self.collection.insert_one({"nameorder": order, "equipment": equipment, "description": description, "customer": self.user.name, "email": self.user.email})
            print("Заказ успешно добавлен")
        except Exception as e:
            print(e)

    def redirect_to_login(self):
        from UIComponents.LoginComponent import LoginComponent
        try:
            self.close()
            component = LoginComponent()
            component.exec()
        except Exception as e:
            print(e)
