import unittest
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt

from UIComponents import LoginComponent
from User import User

app = QApplication([])


class TestLoginComponent(unittest.TestCase):
    def setUp(self):
        self.component = LoginComponent()

    def test_login_button_clicked(self):
        # Assuming UI components have email_line and password_line
        self.component.ui.email_line.setText("test@example.com")
        self.component.ui.password_line.setText("password")

        with unittest.mock.patch.object(self.component.collection, 'find_one', return_value={"email": "test@example.com", "name": "Test User", "user_root": "client"}):
            self.component.login_button_clicked()
            # Add assertions based on the expected behavior

    def test_redirect_to_master(self):
        # Mock the MasterComponent and check if it's created
        with unittest.mock.patch('YourModuleName.MasterComponent') as mock_master:
            user = User("test@example.com", "Test User", "admin")
            self.component.redirect_to_master(user)

        mock_master.assert_called_once_with(user)

# Similar tests can be written for MasterComponent and ClientComponent

if __name__ == '__main__':
    unittest.main()
