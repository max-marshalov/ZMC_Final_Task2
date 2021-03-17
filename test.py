from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets, QtGui, QtCore
import sqlite3
from startwindow import Ui_MainWindow
from pht import Ui_Pht
from check import Ui_Check
from join import *
import sys


class CheckWindow(QMainWindow, Ui_Check):
    def __init__(self, path):
        self.path = path
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect(self.path)
        self.curs = self.con.cursor()
        self.data = \
            self.curs.execute("""SELECT photo_path, agree_path, agree_join_path from Anket WHERE id = 1""").fetchall()[
                0]

        self.personal_photo.clicked.connect(self.shw_pers_photo)
        # self.paper_photo.clicked.connect(self.shw_paper_photo)
        self.agree_photo.clicked.connect(self.shw_ag_photo)
        # self.tabel_photo.clicked.connect(self.shw_tb_photo)
        # self.achives_photo.clicked.connect(self.shw_ach_photo)
        self.join_agree_photo.clicked.connect(self.shw_join_photo)

    def shw_pers_photo(self):
        self.ex = Example(self.data[0])
        self.ex.show()

    def shw_ag_photo(self):
        self.ex = Example(self.data[1])
        self.ex.show()

    def shw_join_photo(self):
        self.ex = Example(self.data[2])
        self.ex.show()
    #def shw_paper_photo(self):
        #self.ex = Example(self.curs.execute("""Select photo_path from paper where id = 1""").fetchone())
        #self.ex.show()



class Example(QWidget):

    def __init__(self, path):
        self.path = path
        super().__init__()

        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)
        pixmap = QtGui.QPixmap(self.path)

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.move(300, 200)
        self.setWindowTitle('Photo')
        self.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = CheckWindow("DATABASE.db")
    mainWindow.show()
    sys.exit(app.exec())
