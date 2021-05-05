import sys

from PyQt5 import QtCore, QtWidgets

from main import Ui_MainWindow
from sql import *


# ----------------------Интерфейс-----------------------------
class Ui_Form(object):
    def setup_start(self, Form):
        Form.setObjectName("Form")
        Form.resize(283, 150)
        self.Layout_2 = QtWidgets.QVBoxLayout(Form)
        self.Layout_2.setObjectName("Layout_2")
        self.Layout = QtWidgets.QVBoxLayout()
        self.Layout.setObjectName("Layout")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.Layout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.Layout.addWidget(self.lineEdit_2)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.Layout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.Layout.addWidget(self.pushButton)
        self.Layout_2.addLayout(self.Layout)

        self.pushButton.setStyleSheet("border: 2px solid rgb(0, 207, 207); background: white;border-radius: 6px")
        self.pushButton_2.setStyleSheet("border: 2px solid rgb(0, 207, 207); background: white;border-radius: 6px")
        self.lineEdit.setStyleSheet("border: 2px solid black")
        self.lineEdit_2.setStyleSheet("border: 2px solid black")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Authorization"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Login.."))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Password.."))
        self.pushButton_2.setText(_translate("Form", "Авторизация"))
        self.pushButton.setText(_translate("Form", "Регистрация"))


# ----------------------Оснавной класс логина и пароля-----------------------------


class Interface(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setup_start(self)

        self.ui.pushButton.clicked.connect(self.reg)
        self.ui.pushButton_2.clicked.connect(self.auth)
        self.base_line_edit = [self.ui.lineEdit, self.ui.lineEdit_2]

        self.check_db = CheckThread()
        self.check_db.mysignal.connect(self.signal_handler)

    # ----------------------Проверка ввода-----------------
    def check_input(funct):
        def wrapper(self):
            for line_edit in self.base_line_edit:
                if len(line_edit.text()) == 0:
                    return
            funct(self)

        return wrapper

    # ----------------------Сигналы--------------------------
    def signal_handler(self, value):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value)
        if value == 'Успешная авторизация!':
            self.window = QtWidgets.QMainWindow()
            self.np = Ui_MainWindow()
            self.np.setupUi(self.window)
            self.window.show()

    def auth(self):
        name = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        self.check_db.thr_login(name, password)

    def reg(self):
        name = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        self.check_db.thr_register(name, password)


class CheckThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)

    def thr_login(self, name, password):
        login(name, password, self.mysignal)

    def thr_register(self, name, password):
        register(name, password, self.mysignal)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mywin = Interface()
    mywin.show()
    sys.exit(app.exec_())
