# -*- coding: utf-8 -*-

import csv
import sqlite3
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTime
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QInputDialog
from PyQt5.QtWidgets import QMessageBox

from study_window import Ui_OtherWindow


class Ui_MainWindow(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_OtherWindow()
        self.ui.setup_study_window(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        self.db = "words.db"

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(620, 620)
        MainWindow.setStyleSheet("background: white; border: 2px solid black")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")

        # ------------------------Окно ошибки------------------------------------

        self.error_dialog = QtWidgets.QErrorMessage()
        self.error_dialog.setGeometry(700, 400, 150, 150)

        # ------------------------Часы----------------------------------------

        self.clock = QtWidgets.QLCDNumber(self.centralwidget)
        self.clock.setGeometry(QtCore.QRect(150, 30, 361, 101))
        self.clock.setStyleSheet("border: 2px solid rgb(0, 207, 207); background: white;border-radius: 12px")
        self.clock.setObjectName("clock")
        self.showTime()

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(75, 150, 510, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setStyleSheet("border: 0px solid black")
        self.label.setText('УЖЕ ВОТ СТОЛЬКО ВРЕМЕНИ, А ТЫ ЕЩЁ НЕ ИЗУЧАЛ СЛОВА?!')

        # ------------------------Основаная кнопка-----------------------------

        self.button_main = QtWidgets.QPushButton(self.centralwidget)
        self.button_main.setGeometry(QtCore.QRect(150, 440, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.button_main.setFont(font)
        self.button_main.setStyleSheet("border: 2px solid rgb(0, 207, 207); background: white;border-radius: 10px")
        self.button_main.setObjectName("button_main")
        MainWindow.setCentralWidget(self.centralwidget)
        self.button_main.clicked.connect(self.openWindow)

        # ------------------------Меню-бар-----------------------------

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(10)
        self.menubar.setFont(font)
        self.menubar.setStyleSheet("background: rgb(0, 207, 207)")
        self.menubar.setObjectName("menubar")

        self.menu_words = QtWidgets.QMenu(self.menubar)
        self.menu_words.setStyleSheet("background: rgb(0, 207, 207)")
        self.menu_words.setObjectName("menu_words")

        self.menu_add = QtWidgets.QMenu(self.menu_words)
        self.menu_add.setStyleSheet("")
        self.menu_add.setObjectName("menu_add")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStyleSheet("background: black")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.delet_words = QtWidgets.QAction(MainWindow)
        self.delet_words.setObjectName("delet_words")
        self.delet_words.triggered.connect(self.delet_word_func)
        self.delet_words.setShortcut('Ctrl+D')

        self.add_1_word = QtWidgets.QAction(MainWindow)
        self.add_1_word.setObjectName("add_1_word")
        self.add_1_word.triggered.connect(self.append_word)
        self.add_1_word.setShortcut('Ctrl+Q')

        self.add_file_txt = QtWidgets.QAction(MainWindow)
        self.add_file_txt.setObjectName("add_file_txt")
        self.add_file_txt.triggered.connect(self.append_file_txt)
        self.add_file_txt.setShortcut('Ctrl+Z')

        self.menu_add.addAction(self.add_1_word)
        self.menu_add.addAction(self.add_file_txt)
        self.menu_words.addAction(self.menu_add.menuAction())
        self.menu_words.addAction(self.delet_words)
        self.menubar.addAction(self.menu_words.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.error_dialog = QtWidgets.QErrorMessage()
        self.error_dialog.setGeometry(700, 400, 150, 150)

        # ------------------------Функции-----------------------------

    def showTime(self):
        time = QTime.currentTime()
        text = time.toString('hh:mm')
        if (time.second() % 2) == 0:
            text = text[:2] + ' ' + text[3:5]
        self.clock.display(text)

    def append_word(self):

        dlg = QInputDialog
        name, ok_pressed = dlg.getText(self.centralwidget, "Добавьте слово", "Добавьте слово")
        if name == '' or name == ' ' or name == '  ' or name == '   ':
            self.error_dialog.showMessage('Вы не ввели слово')
            return 0

        rus_word = name

        name, ok_pressed = dlg.getText(self.centralwidget, "Добавьте перевод", "Добавьте перевод этого слова")
        if name == '' or name == ' ' or name == '  ' or name == '   ':
            self.error_dialog.showMessage('Вы не ввели слово')
            return 0

        eng_word = name

        con = sqlite3.connect(self.db)
        cur = con.cursor()
        max_id = cur.execute("""select max(id) from word""").fetchall()
        max_id = int(max_id[0][0])
        cur.execute("""INSERT INTO word VALUES (?, ?, ?, 4);
        """, ((int(max_id) + 1), rus_word, eng_word)).fetchall()
        con.commit()
        con.close()

    def delet_word_func(self):

        dlg = QInputDialog
        name, ok_pressed = dlg.getText(self.centralwidget, "Удалите слово", "Удалите слово")

        con = sqlite3.connect(self.db)
        cur = con.cursor()
        cur.execute("""DELETE FROM word where rus_word = ? or eng_word = ?""",
                    (name, name)).fetchall()
        con.commit()
        con.close()

    def append_file_txt(self):
        rus_words = []
        eng_words = []
        file_name, _ = QFileDialog.getOpenFileName(None, 'Open File', r"<Default dir>",
                                                   "csv, txt file (*.txt *.csv)")

        if file_name.endswith('.txt'):

            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText(
                "Вы выбрали txt файл. Сначало введите пропуски между вашими словосоченатиями, а потом между словами")
            msgBox.setWindowTitle("Info")
            msgBox.exec()

            dlg = QInputDialog
            name, ok_pressed = dlg.getText(self.centralwidget, "Введите пропуск", "Введите пропуск между словами")
            if name == '' or name == ' ' or name == '  ' or name == '   ':
                self.error_dialog.showMessage('Вы ничего не ввели')
                return 0

            pass_1 = name

            dlg = QInputDialog
            name, ok_pressed = dlg.getText(self.centralwidget, "Введите пропуск", "Введите пропуск между словами")
            if name == '' or name == ' ' or name == '  ' or name == '   ':
                self.error_dialog.showMessage('Вы ничего не ввели')
                return 0

            pass_2 = name

            f = open(file_name, 'r', encoding="utf8")
            separation = f.read().split(pass_1)
            for i in separation:
                rus_words.append(i.split(pass_2)[0])
                eng_words.append(i.split(pass_2)[1])
        else:
            with open(file_name, encoding="utf8") as csvfile:
                reader = csv.reader(csvfile, delimiter=';', quotechar='"')
                for i in reader:
                    rus_words.append(i[0])
                    eng_words.append(i[1])


        con = sqlite3.connect(self.db)
        cur = con.cursor()
        max_id = cur.execute("""select max(id) from word""").fetchall()
        max_id = int(max_id[0][0])
        count = 1
        for i in range(len(rus_words)):

            cur.execute("""INSERT INTO word VALUES (?, ?, ?, 4);
            """, ((int(max_id) + count), rus_words[i], rus_words[i])).fetchall()
            count += 1
        con.commit()
        con.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_main.setText(_translate("MainWindow", "Начать изучение"))
        self.menu_words.setTitle(_translate("MainWindow", "Слова"))
        self.menu_add.setTitle(_translate("MainWindow", "Добавить"))
        self.add_file_txt.setText(_translate("MainWindow", "Добавить файл"))
        self.delet_words.setText(_translate("MainWindow", "Удалить"))
        self.add_1_word.setText(_translate("MainWindow", "Добавить слово"))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ex = Ui_MainWindow()
    ex.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
