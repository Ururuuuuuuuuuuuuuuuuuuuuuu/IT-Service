from PyQt5.QtGui import QStandardItemModel
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QTableView

from DatabaseConnector import DatabaseTableThread

from UIWidgets.MasterDialog import Ui_Master


class MasterComponent(QtWidgets.QDialog):
    def __init__(self, user):
        super(MasterComponent, self).__init__()
        self.ui = Ui_Master()
        self.ui.setupUi(self)

        self.model = QStandardItemModel(self)
        self.model.setHorizontalHeaderLabels(["Заказ", "Техніка", "Опис", "Замовник", "Ім'я"])

        self.ui.orders_table.setModel(self.model)
        self.ui.orders_table.setSelectionBehavior(QTableView.SelectRows)

        self.db_thread = DatabaseTableThread()
        self.db_thread.data_received.connect(self.update_table)
        self.db_thread.start()

    def update_table(self, data):
        row_position = self.model.rowCount()
        self.model.insertRow(row_position)

        for column, value in enumerate(data):
            item = QtGui.QStandardItem(str(value))
            self.model.setItem(row_position, column, item)