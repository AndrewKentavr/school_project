# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Игра.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


import sys
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QButtonGroup, QRadioButton

file_txt = 'Список слов.txt'

class Ui_OtherWindow(object):
    def setup_study_window(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(688, 723)
        Dialog.setStyleSheet("background: white")

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 70, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("border: 2px solid black; background: white;border-radius: 9px")
        self.label.setObjectName("label")

        self.label_correct = QtWidgets.QLabel(Dialog)
        self.label_correct.setGeometry(QtCore.QRect(120, 160, 140, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_correct.setFont(font)
        self.label_correct.setObjectName("label")

        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(270, 70, 321, 41))
        self.lineEdit.setStyleSheet("border: 2px solid rgb(0, 207, 207); background: white;border-radius: 12px")
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit_2")

        self.radioButton_1 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_1.setGeometry(QtCore.QRect(480, 190, 95, 20))
        self.radioButton_1.setObjectName("radioButton_3")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(350, 150, 95, 20))
        self.radioButton_2.setObjectName("radioButton_4")
        self.radioButton_3 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_3.setGeometry(QtCore.QRect(350, 190, 95, 20))
        self.radioButton_3.setObjectName("radioButton_2")
        self.radioButton_4 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_4.setGeometry(QtCore.QRect(480, 150, 95, 20))
        self.radioButton_4.setObjectName("radioButton")

        self.button_group = QButtonGroup()
        self.button_group.addButton(self.radioButton_1)
        self.button_group.addButton(self.radioButton_2)
        self.button_group.addButton(self.radioButton_3)
        self.button_group.addButton(self.radioButton_4)

        self.button_group.buttonClicked.connect(self._on_radio_button_clicked)

        # ----------------------------------------------------------------------------
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 270, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border: 2px solid black; background: white;border-radius: 9px")
        self.label_2.setObjectName("label_2")

        self.label_correct_2 = QtWidgets.QLabel(Dialog)
        self.label_correct_2.setGeometry(QtCore.QRect(120, 360, 140, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_correct_2.setFont(font)
        self.label_correct_2.setObjectName("label")

        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(270, 270, 321, 41))
        self.lineEdit_2.setStyleSheet("border: 2px solid rgb(0, 207, 207); background: white;border-radius: 12px")
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_3")

        self.radioButton_5 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_5.setGeometry(QtCore.QRect(480, 350, 95, 20))
        self.radioButton_5.setObjectName("radioButton_7")
        self.radioButton_6 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_6.setGeometry(QtCore.QRect(480, 390, 95, 20))
        self.radioButton_6.setObjectName("radioButton_8")
        self.radioButton_7 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_7.setGeometry(QtCore.QRect(350, 350, 95, 20))
        self.radioButton_7.setObjectName("radioButton_5")
        self.radioButton_8 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_8.setGeometry(QtCore.QRect(350, 390, 95, 20))
        self.radioButton_8.setObjectName("radioButton_6")

        self.button_group_2 = QButtonGroup()
        self.button_group_2.addButton(self.radioButton_5)
        self.button_group_2.addButton(self.radioButton_6)
        self.button_group_2.addButton(self.radioButton_7)
        self.button_group_2.addButton(self.radioButton_8)

        self.button_group_2.buttonClicked.connect(self._on_radio_button_clicked_2)

        # ----------------------------------------------------------------------------
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 480, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border: 2px solid black; background: white;border-radius: 9px")
        self.label_3.setObjectName("label_3")

        self.label_correct_3 = QtWidgets.QLabel(Dialog)
        self.label_correct_3.setGeometry(QtCore.QRect(120, 570, 140, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_correct_3.setFont(font)
        self.label_correct_3.setObjectName("label")

        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(270, 480, 321, 41))
        self.lineEdit_3.setStyleSheet("border: 2px solid rgb(0, 207, 207); background: white;border-radius: 12px")
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_4")

        self.radioButton_9 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_9.setGeometry(QtCore.QRect(480, 600, 95, 20))
        self.radioButton_9.setObjectName("radioButton_9")
        self.radioButton_10 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_10.setGeometry(QtCore.QRect(350, 560, 95, 20))
        self.radioButton_10.setObjectName("radioButton_10")
        self.radioButton_11 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_11.setGeometry(QtCore.QRect(350, 600, 95, 20))
        self.radioButton_11.setObjectName("radioButton_11")
        self.radioButton_12 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_12.setGeometry(QtCore.QRect(480, 560, 95, 20))
        self.radioButton_12.setObjectName("radioButton_12")

        self.button_group_3 = QButtonGroup()
        self.button_group_3.addButton(self.radioButton_9)
        self.button_group_3.addButton(self.radioButton_10)
        self.button_group_3.addButton(self.radioButton_11)
        self.button_group_3.addButton(self.radioButton_12)

        self.button_group_3.buttonClicked.connect(self._on_radio_button_clicked_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # ----------------------------Тут хрень---------------------------
        # ----------------------------1 колонка-------------------------------


        import random

        db = "words.db"
        con = sqlite3.connect(db)
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM word
        WHERE category = 4""").fetchall()
        self.lines = []
        for elem in result:
            name = ''
            name += elem[1] + ', ' + elem[2]
            self.lines.append(name)
        con.close()

        random_number = random.randint(1, 4)

        random_list = []

        self.ran = random.choice(self.lines)
        self.lineEdit.setText(self.ran.split(', ')[0])

        if random_number == 1:
            random_list.append(self.ran.split(', ')[1])
            self.radioButton_1.setText(self.ran.split(', ')[1])
        else:
            r = random.choice(self.lines).split(', ')[1]
            random_list.append(r)
            self.radioButton_1.setText(r)
        if random_number == 2:
            random_list.append(self.ran.split(', ')[1])
            self.radioButton_2.setText(self.ran.split(', ')[1])
        else:
            r = random.choice(self.lines).split(', ')[1]
            while r in random_list:
                r = random.choice(self.lines).split(', ')[1]
            random_list.append(r)
            self.radioButton_2.setText(r)
        if random_number == 3:
            random_list.append(self.ran.split(', ')[1])
            self.radioButton_3.setText(self.ran.split(', ')[1])
        else:
            r = random.choice(self.lines).split(', ')[1]
            while r in random_list:
                r = random.choice(self.lines).split(', ')[1]
            random_list.append(r)
            self.radioButton_3.setText(r)
        if random_number == 4:
            random_list.append(self.ran.split(', ')[1])
            self.radioButton_4.setText(self.ran.split(', ')[1])
        else:
            r = random.choice(self.lines).split(', ')[1]
            while r in random_list:
                r = random.choice(self.lines).split(', ')[1]
            random_list.append(r)
            self.radioButton_4.setText(r)

        # ----------------------------2 колонка--------------------------------------

        random_number_2 = random.randint(1, 4)

        random_list_2 = []

        self.ran_2 = random.choice(self.lines)

        while self.lineEdit.text() == self.ran_2.split(', ')[0]:
            self.ran_2 = random.choice(self.lines)

        self.lineEdit_2.setText(self.ran_2.split(', ')[0])
        self.lineEdit.text()

        if random_number_2 == 1:
            random_list_2.append(self.ran_2.split(', ')[1])
            self.radioButton_5.setText(self.ran_2.split(', ')[1])
        else:
            r = random.choice(self.lines).split(', ')[1]
            random_list_2.append(r)
            self.radioButton_5.setText(r)
        if random_number_2 == 2:
            random_list_2.append(self.ran_2.split(', ')[1])
            self.radioButton_6.setText(self.ran_2.split(', ')[1])
        else:
            r = random.choice(self.lines).split(', ')[1]
            while r in random_list_2:
                r = random.choice(self.lines).split(', ')[1]
            random_list_2.append(r)
            self.radioButton_6.setText(r)
        if random_number_2 == 3:
            random_list_2.append(self.ran_2.split(', ')[1])
            self.radioButton_7.setText(self.ran_2.split(', ')[1])
        else:
            r = random.choice(self.lines).split(', ')[1]
            while r in random_list_2:
                r = random.choice(self.lines).split(', ')[1]
            random_list_2.append(r)
            self.radioButton_7.setText(r)
        if random_number_2 == 4:
            random_list_2.append(self.ran_2.split(', ')[1])
            self.radioButton_8.setText(self.ran_2.split(', ')[1])
        else:
            r = random.choice(self.lines).split(', ')[1]
            while r in random_list_2:
                r = random.choice(self.lines).split(', ')[1]
            random_list_2.append(r)
            self.radioButton_8.setText(r)
        # ----------------------------3 колонка--------------------------------------

        random_number_3 = random.randint(1, 4)

        random_list_3 = []

        self.ran_3 = random.choice(self.lines)

        while self.lineEdit.text() == self.ran_3.split(', ')[0] or self.lineEdit_2.text() == self.ran_3.split(', ')[0]:
            self.ran_3 = random.choice(self.lines)

        self.lineEdit_3.setText(self.ran_3.split(', ')[0])

        if random_number_3 == 1:
            random_list_3.append(self.ran_3.split(', ')[1])
            self.radioButton_9.setText(self.ran_3.split(', ')[1])
        else:
            r = random.choice(self.lines).split(', ')[1]
            random_list_3.append(r)
            self.radioButton_9.setText(r)
        if random_number_3 == 2:
            random_list_3.append(self.ran_3.split(', ')[1])
            self.radioButton_10.setText(self.ran_3.split(', ')[1])
        else:
            r = random.choice(self.lines).split(', ')[1]
            while r in random_list_3:
                r = random.choice(self.lines).split(', ')[1]
            random_list_3.append(r)
            self.radioButton_10.setText(r)
        if random_number_3 == 3:
            random_list_3.append(self.ran_3.split(', ')[1])
            self.radioButton_11.setText(self.ran_3.split(', ')[1])
        else:
            r = random.choice(self.lines).split(', ')[1]
            while r in random_list_3:
                r = random.choice(self.lines).split(', ')[1]
            random_list_3.append(r)
            self.radioButton_11.setText(r)
        if random_number_3 == 4:
            random_list_3.append(self.ran_3.split(', ')[1])
            self.radioButton_12.setText(self.ran_3.split(', ')[1])
        else:
            r = random.choice(self.lines).split(', ')[1]
            while r in random_list_3:
                r = random.choice(self.lines).split(', ')[1]
            random_list_3.append(r)
            self.radioButton_12.setText(r)

        # ----------------------------Функции--------------------------------------


    def _on_radio_button_clicked(self, button):
        if self.ran.split(', ')[1] == button.text():
            self.label_correct.setText('Правильный ответ')
            self.label_correct.setStyleSheet("border: 2px solid rgb(0, 255, 0); background: white;border-radius: 9px")
        else:
            self.label_correct.setText('Неверный ответ')
            self.label_correct.setStyleSheet("border: 2px solid red; background: white;border-radius: 9px")

    def _on_radio_button_clicked_2(self, button):
        if self.ran_2.split(', ')[1] == button.text():
            self.label_correct_2.setText('Правильный ответ')
            self.label_correct_2.setStyleSheet("border: 2px solid rgb(0, 255, 0); background: white;border-radius: 9px")

        else:
            self.label_correct_2.setText('Неверный ответ')
            self.label_correct_2.setStyleSheet("border: 2px solid red; background: white;border-radius: 9px")

    def _on_radio_button_clicked_3(self, button):
        if self.ran_3.split(', ')[1] == button.text():
            self.label_correct_3.setText('Правильный ответ')
            self.label_correct_3.setStyleSheet("border: 2px solid rgb(0, 255, 0); background: white;border-radius: 9px")

        else:
            self.label_correct_3.setText('Неверный ответ')
            self.label_correct_3.setStyleSheet("border: 2px solid red; background: white;border-radius: 9px")


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Ведите перевод:"))
        self.label_3.setText(_translate("Dialog", "Ведите перевод:"))
        self.label_2.setText(_translate("Dialog", "Ведите перевод:"))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    OtherWindow = QtWidgets.QMainWindow()
    ui = Ui_OtherWindow()
    ui.setup_study_window(OtherWindow)
    OtherWindow.show()
    sys.exit(app.exec_())
