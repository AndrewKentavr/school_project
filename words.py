# -*- coding: utf-8 -*-

import sqlite3

from PyQt5.QtWidgets import QInputDialog

from shit import Ui_MainWindow


class Words_func(Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db = "words.db"

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

        self.log.show()

    def delet_word_func(self):

        dlg = QInputDialog
        name, ok_pressed = dlg.getText(self.centralwidget, "Удалите слово", "Удалите слово")

        con = sqlite3.connect(self.db)
        cur = con.cursor()
        cur.execute("""DELETE FROM word where rus_word = ? or eng_word = ?""",
                    (name, name)).fetchall()
        con.commit()
        con.close()
