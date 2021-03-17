from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets, QtGui, QtCore
import sqlite3
from startwindow import Ui_MainWindow
from check import Ui_Check
from join import *
from Results_Table import *
import sys


class Join(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Join()
        self.ui.setupUi(self)

        self.ui.label_error.hide()

        self.ui.btn_join.clicked.connect(self.go_join)

    def go_join(self):
        Login = None
        Password = None

        if len(self.ui.edit_login.text()) > 0:
            Login = self.ui.edit_login.text()
        else:
            self.ui.label_error.setText("Введите логин и пароль")
            self.ui.label_error.show()
            return

        if len(self.ui.edit_password.text()) > 0:
            Password = self.ui.edit_password.text()
        else:
            self.ui.label_error.setText("Введите логин и пароль")
            self.ui.label_error.show()
            return

        con = sqlite3.connect("DATABASE.db")
        curs = con.cursor()
        ex = curs.execute(
            """SELECT * FROM Teachers WHERE FIO = "{}" and password = "{}" """.format(Login, Password)).fetchall()
        con.commit()
        con.close()
        if not ex:
            self.ui.label_error.setText("Неверный логин или пароль")
            self.ui.label_error.show()
            return
        else:
            try:
                self.win = UI_Main("DATABASE.db")
                self.close()
                self.win.show()

            except Exception as er:
                print(er)


################################################################################################################
################################################################################################################
class CheckWindow(QMainWindow, Ui_Check):
    def __init__(self, path, user):
        self.user = user
        self.path = path
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect(self.path)
        self.curs = self.con.cursor()
        try:
            self.data = self.curs.execute(
                f"""SELECT photo_path, agree_path, agree_join_path from Anket WHERE id = {self.user}""").fetchall()[0]
        except Exception as ex:
            self.data = ('', '', '')
        print(self.data)
        self.personal_photo.clicked.connect(self.shw_pers_photo)
        self.paper_photo.clicked.connect(self.shw_paper_photo)
        self.agree_photo.clicked.connect(self.shw_ag_photo)
        self.tabel_photo.clicked.connect(self.shw_tb_photo)
        self.achives_photo.clicked.connect(self.shw_ach_photo)
        self.join_agree_photo.clicked.connect(self.shw_join_photo)

        self.radioButton_bad.clicked.connect(self.unblocking)
        self.radioButton_good.clicked.connect(self.unblocking)

        self.checkbox_base = [self.checkBox, self.checkBox_2, self.checkBox_3, self.checkBox_4, self.checkBox_5,
                              self.checkBox_6]

        self.btn_back.clicked.connect(self.go_to_main)
        self.btn_send.clicked.connect(self.sending)

        self.fio = self.curs.execute(
            f"""SELECT FIO from UserForm WHERE id = {self.user}""").fetchone()[0]
        self.label_FIO.setText(self.fio)

    def sending(self):
        self.wrongs = []
        if self.radioButton_bad.isChecked():
            for box in self.checkbox_base:
                if box.isChecked():
                    self.wrongs.append(box.text())
            self.curs.execute(
                f"""UPDATE UserForm set level = 'Отправлено на доработку' WHERE id = {self.user}"""
            )
            self.con.commit()
            # отправка письма с ошибками
        else:
            # отправка письма об участии
            self.curs.execute(
                f"""UPDATE UserForm set level = 'Принято' WHERE id = {self.user}"""
            )
            self.con.commit()

    def go_to_main(self):
        try:
            self.win = UI_Main("DATABASE.db")
            self.close()
            self.win.show()

        except Exception as er:
            print(er)

    def unblocking(self):
        if self.radioButton_bad.isChecked():
            for box in self.checkbox_base:
                box.setEnabled(1)
        else:
            for box in self.checkbox_base:
                box.setDisabled(1)

    def shw_pers_photo(self):
        if self.data[0]:
            self.ex = Example(self.data[0])
            self.ex.show()
        else:
            info = QMessageBox.information(self, "Message", "Пользователь не загрузил эти данные")

    def shw_ag_photo(self):
        if self.data[1]:
            self.ex = Example(self.data[1])
            self.ex.show()
        else:
            info = QMessageBox.information(self, "Message", "Пользователь не загрузил эти данные")

    def shw_join_photo(self):
        if self.data[2]:
            self.ex = Example(self.data[2])
            self.ex.show()
        else:
            info = QMessageBox.information(self, "Message", "Пользователь не загрузил эти данные")

    def shw_paper_photo(self):
        dt = self.curs.execute("""Select photo_path from paper where id = 1""").fetchall()[0][0]
        if dt:
            self.ex = Example(dt)
            self.ex.show()

        else:
            info = QMessageBox.information(self, "Message", "Пользователь не загрузил эти данные")

    def shw_tb_photo(self):
        try:
            dt = self.curs.execute("""Select photo_path from Education where id = 1""").fetchall()[0][0]
            if dt:
                self.ex = Example(dt)
                self.ex.show()
            else:
                info = QMessageBox.information(self, "Message", "Пользователь не загрузил эти данные")
        except Exception as er:
            print(er)

    def shw_ach_photo(self):
        try:
            dt = self.curs.execute("""Select photo_path from Achives where id = 1""").fetchall()[0][0]
            if dt:
                self.ex = Example(dt)
                self.ex.show()
            else:
                info = QMessageBox.information(self, "Message", "Пользователь не загрузил эти данные")

        except Exception as er:
            print(er)


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


#####################################################################################################################
##########################################################################################################################

class Results_Table(QMainWindow, Ui_Results_Table):
    def __init__(self, path):
        self.path = path
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect(self.path)
        self.cur = self.con.cursor()

        self.btn_go_to_main.clicked.connect(self.go_to_main)
        self.comboBox.activated.connect(self.get_data)
        # self.user_id = self.cur.execute("""Select PersonalData from Anket""").fetchall()[0]
        # self.exam = self.cur.execute("""Select Exams from Anket""").fetchall()[0]
        # self.ach = self.cur.execute("Select Achives from Anket").fetchall()[0]
        # self.cp = self.cur.execute("Select copy from Anket").fetchall()[0]

    def get_data(self):
        try:
            self.brch = self.cur.execute(
                """Select id from Branches where name = "{}"  """.format(self.comboBox.currentText())).fetchall()[0][0]
            self.need = self.cur.execute(
                """Select need from Branches where name = "{}" """.format(self.comboBox.currentText())).fetchall()[0][0]

            self.data = self.cur.execute(
                """Select PersonalData, Exams, Achives, copy from Anket WHERE Branch = {}""".format(
                    self.brch)).fetchall()
            self.items = []
            for i in self.data:
                self.FIO = \
                    self.cur.execute("""Select FIO from UserForm WHERE id = {}""".format(i[0])).fetchall()[0][0]
                self.ach = \
                    self.cur.execute("""Select price from Achives where id = {}""".format(i[2])).fetchall()[0][0]
                if i[3]:
                    self.cp = "Да"
                else:
                    self.cp = "Нет"
                self.ex = self.cur.execute(
                    """Select rus, math, "{}" from Exams where id = {} """.format(self.need, i[1])).fetchall()[0]
                self.summ = sum(self.ex)
                self.items.append((self.FIO, self.summ, self.ach, self.cp))
                self.tableWidget.setRowCount(0)
                n = len(self.items)
                self.tableWidget.setRowCount(n)
                for j in range(n):
                    self.tableWidget.setItem(j, 0, QTableWidgetItem())
                    self.tableWidget.setItem(j, 1, QTableWidgetItem())
                    self.tableWidget.setItem(j, 2, QTableWidgetItem())
                    self.tableWidget.setItem(j, 3, QTableWidgetItem())

                    self.tableWidget.item(j, 0).setText(self.items[j][0])
                    self.tableWidget.item(j, 1).setText(str(self.items[j][1]))
                    self.tableWidget.item(j, 2).setText(str(self.items[j][2]))
                    self.tableWidget.item(j, 3).setText(self.items[j][3])

        except Exception as er:
            print(er)

    def go_to_main(self):
        try:
            self.win = UI_Main("DATABASE.db")
            self.close()
            self.win.show()

        except Exception as er:
            print(er)



class UI_Main(QMainWindow, Ui_MainWindow):
    def __init__(self, path):
        self.path = path
        super().__init__()
        self.setupUi(self)

        self.conn = sqlite3.connect(self.path)
        self.curs = self.conn.cursor()
        # self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        # self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        # self.tableWidget.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        # self.tableWidget.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        # self.tableWidget.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        # self.tableWidget.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        self.update_data()
        self.tableWidget.cellClicked.connect(self.student)

        self.btn_go_to_tables.clicked.connect(self.go_to_tables)
        self.btn_go_to_zach.clicked.connect(self.go_to_zach)

        self.student_status = 'Новый'

    def go_to_tables(self):
        try:
            self.win = Results_Table("DATABASE.db")
            self.close()
            self.win.show()
        except Exception as er:
            print(er)

    def go_to_zach(self):
        pass

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
            self.level = self.curs.execute(
                f"""Select level from UserForm WHERE id = {i + 1}""").fetchone()[0]

            if self.level == None:
                self.level = 'Новый'

            if self.anketa:
                for j in self.anketa:
                    if j:
                        kol += 1

                if kol == len(self.anketa):
                    self.student_status = 'Полный комплект'
                    if self.level == 'Новый':
                        self.level = 'На рассмотрении'
                elif ((kol == len(self.anketa) - 1) or (kol == len(self.anketa) - 1)) and (
                        (not self.anketa[-1]) or (not self.anketa[-2])):
                    self.student_status = 'Комплект без оригинала'
                elif kol > 0:
                    self.student_status = 'В работе'
                else:
                    self.student_status = 'Новый'
            else:
                self.student_status = 'Новый'

            self.curs.execute(
                f"""UPDATE UserForm set level = '{self.level}' WHERE id = {i + 1}"""
            )
            self.conn.commit()

            self.tableWidget.setItem(i, 5, QTableWidgetItem())
            self.tableWidget.item(i, 5).setText(self.student_status)

            self.tableWidget.setItem(i, 6, QTableWidgetItem())
            self.tableWidget.item(i, 6).setText(self.level)

    def student(self):
        try:
            self.win = CheckWindow("DATABASE.db", int(self.tableWidget.item(self.tableWidget.currentRow(), 0).text()))
            self.close()
            self.win.show()
        except Exception as error:
            print(error)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = Join()
    mainWindow.show()
    sys.exit(app.exec())
