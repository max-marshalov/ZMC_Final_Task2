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
        self.tableWidget.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        self.update_data()
        self.tableWidget.cellClicked.connect(self.student)

        self.student_status = 'Новый'

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

        for i in range(n):
            self.anketa = self.curs.execute(
                f"""Select Address, Paper, PersonalData, Education, agree_path, edu_form, branch, Exams, Achives, birthday, place_of_birth, phone_number, photo_path, campus, copy, agree_join_path from Anket where id='{i + 1}'""").fetchone()

            kol = 0

            if self.anketa:
                for j in self.anketa:
                    if j:
                        kol += 1

                if kol == len(self.anketa):
                    self.student_status = 'Полный комплект'
                elif ((kol == len(self.anketa) - 1) or (kol == len(self.anketa) - 1)) and (
                        (not self.anketa[-1]) or (not self.anketa[-2])):
                    self.student_status = 'Комплект без оригинала'
                elif kol > 0:
                    self.student_status = 'В работе'
                else:
                    self.student_status = 'Новый'
            else:
                self.student_status = 'Новый'

            self.tableWidget.setItem(i, 5, QTableWidgetItem())
            self.tableWidget.item(i, 5).setText(self.student_status)

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
