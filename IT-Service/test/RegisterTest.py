import unittest
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
from unittest.mock import patch

from UIComponents.RegisterComponent import RegisterComponent
from UIComponents.LoginComponent import LoginComponent
from UIComponents.MasterComponent import MasterComponent
from UIComponents.ClientComponent import ClientComponent
from User import User

app = QApplication([])

class TestRegisterComponent(unittest.TestCase):
    def setUp(self):
        self.component = RegisterComponent()

    def test_register_button_clicked(self):
        # Мокаем атрибут collection
        with patch.object(self.component, 'collection') as mock_collection:
            # Продолжаем с вашим тестовым кодом
            self.component.ui.email_line.setText("test@example.com")
            self.component.ui.name_line.setText("Test User")
            self.component.ui.password_line.setText("password")
            self.component.register_button_clicked()
            # Добавьте утверждения в соответствии с ожидаемым поведением

    def test_redirect_to_login(self):
        # Мокаем LoginComponent и проверяем, что он создан
        with patch('UIComponents.LoginComponent.LoginComponent') as mock_login:
            self.component.redirect_to_login()
            app.exit()  # Останавливаем выполнение теста

        mock_login.assert_called_once()

class TestLoginComponent(unittest.TestCase):
    def setUp(self):
        self.component = LoginComponent()

    def test_login_button_clicked(self):
        # Мокаем атрибут collection
        with patch.object(self.component, 'collection') as mock_collection:
            mock_collection.find_one.return_value = {"email": "test@example.com", "name": "Test User", "user_root": "client"}

            # Продолжаем с вашим тестовым кодом
            self.component.ui.email_line.setText("test@example.com")
            self.component.ui.password_line.setText("password")
            self.component.login_button_clicked()
            # Добавьте утверждения в соответствии с ожидаемым поведением

    def test_redirect_to_master(self):
        # Мокаем MasterComponent и проверяем, что он создан
        with patch('UIComponents.MasterComponent.MasterComponent') as mock_master:
            user = User("test@example.com", "Test User", "admin")
            self.component.redirect_to_master(user)
            app.exit()  # Останавливаем выполнение теста

        mock_master.assert_called_once_with(user)

# Похожие тесты можно написать для MasterComponent и ClientComponent

if __name__ == '__main__':
    unittest.main()
