from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets, QtGui, QtCore
import sqlite3
from startwindow import Ui_MainWindow
import sys


class UI_Main(QMainWindow, Ui_MainWindow):
    def __init__(self, path):
        self.path = path
        super().__init__()
        self.setupUi(self)

        self.conn = sqlite3.connect(self.path)
        self.curs = self.conn.cursor()
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        #self.tableWidget.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        self.update_data()
        self.tableWidget.cellClicked.connect(self.student)

    def update_data(self):
        self.data = self.curs.execute(
            """Select id, FIO, sex, email, phone_number from UserForm""").fetchall()
        self.update_table()

    def update_table(self):
        self.tableWidget.setRowCount(0)

        n = len(self.data)
        self.tableWidget.setRowCount(n)
        for i in range(n):
            self.tableWidget.setItem(i, 0, QTableWidgetItem())
            self.tableWidget.setItem(i, 1, QTableWidgetItem())
            self.tableWidget.setItem(i, 2, QTableWidgetItem())
            self.tableWidget.setItem(i, 3, QTableWidgetItem())
            self.tableWidget.setItem(i, 4, QTableWidgetItem())

            self.tableWidget.item(i, 0).setText(str(self.data[i][0]))
            self.tableWidget.item(i, 1).setText(self.data[i][1])
            self.tableWidget.item(i, 2).setText(str(self.data[i][2]))
            self.tableWidget.item(i, 3).setText(self.data[i][3])
            self.tableWidget.item(i, 4).setText(str(self.data[i][4]))

    def student(self):
        try:
            x = []
            a = self.tableWidget.currentRow()
            for i in range(self.tableWidget.columnCount()):
                x.append(self.tableWidget.item(a, i).text())
            print(x)
        except Exception as er:
            print(er)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = UI_Main("DATABASE.db")
    mainWindow.show()
    sys.exit(app.exec())
