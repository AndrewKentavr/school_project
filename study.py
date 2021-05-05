# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'study.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import sys

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(558, 314)
        self.line_read = QtWidgets.QLineEdit(Dialog)
        self.line_read.setGeometry(QtCore.QRect(110, 100, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.line_read.setFont(font)
        self.line_read.setReadOnly(True)
        self.line_read.setObjectName("line_read")
        self.line_write = QtWidgets.QLineEdit(Dialog)
        self.line_write.setGeometry(QtCore.QRect(110, 180, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.line_write.setFont(font)
        self.line_write.setReadOnly(False)
        self.line_write.setObjectName("line_write")
        self.hint_btn = QtWidgets.QPushButton(Dialog)
        self.hint_btn.setGeometry(QtCore.QRect(460, 270, 91, 31))
        self.hint_btn.setObjectName("hint_btn")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(20, 20, 251, 41))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.exit_btn = QtWidgets.QPushButton(self.widget)
        self.exit_btn.setObjectName("exit_btn")
        self.horizontalLayout.addWidget(self.exit_btn)
        self.pass_btn = QtWidgets.QPushButton(self.widget)
        self.pass_btn.setObjectName("pass_btn")
        self.horizontalLayout.addWidget(self.pass_btn)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.line_read.setText(_translate("Dialog", "Ты еблан"))
        self.line_write.setText(_translate("Dialog", "NO"))
        self.hint_btn.setText(_translate("Dialog", "Подсказка"))
        self.exit_btn.setText(_translate("Dialog", "Закончить"))
        self.pass_btn.setText(_translate("Dialog", "Пропустить"))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ex = Ui_Dialog()
    ex.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
