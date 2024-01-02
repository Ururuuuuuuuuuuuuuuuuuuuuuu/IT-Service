from PyQt5 import QtWidgets, QtGui, QtCore
from pymongo import MongoClient

mongo_url = "mongodb+srv://Vova:Pl,mKoIjN@it-service.frz52dr.mongodb.net/"


class DatabaseThread(QtCore.QThread):
    connection_signal = QtCore.pyqtSignal(MongoClient)

    def run(self):
        client = MongoClient(mongo_url)
        self.connection_signal.emit(client)


class DatabaseTableThread(QtCore.QThread):
    data_received = QtCore.pyqtSignal(list)

    def run(self):
        client = MongoClient(mongo_url)
        database = client["IT-Service"]
        collection = database["orders"]

        for document in collection.find():
            data = [document["nameorder"], document["equipment"], document["description"], document["customer"], document["email"]]
            self.data_received.emit(data)
