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

    def setup_database_connection(self, client):
        self.client = client
        self.database = self.client["IT-Service"]
        self.collection = self.database["orders"]

    def order_button_clicked(self):
        order = self.ui.order_line.text()
        equipment = self.ui.equipment_line.text()
        description = self.ui.descriprion_area.toPlainText()

        if not all([order, equipment, description]):
            print("Заполните все поля")
            return

        try:
            self.collection.insert_one({"nameorder": order, "equipment": equipment, "description": description, "customer": self.user.name, "email": self.user.email})
            print("Заказ успешно добавлен")
        except Exception as e:
            print(e)