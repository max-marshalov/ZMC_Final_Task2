# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Results_Table.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Results_Table(object):
    def setupUi(self, Results_Table):
        Results_Table.setObjectName("Results_Table")
        Results_Table.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Results_Table)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 60, 761, 441))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(140, 20, 331, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.btn_go_to_main = QtWidgets.QPushButton(self.centralwidget)
        self.btn_go_to_main.setGeometry(QtCore.QRect(20, 560, 241, 23))
        self.btn_go_to_main.setObjectName("btn_go_to_main")
        Results_Table.setCentralWidget(self.centralwidget)

        self.retranslateUi(Results_Table)
        QtCore.QMetaObject.connectSlotsByName(Results_Table)

    def retranslateUi(self, Results_Table):
        _translate = QtCore.QCoreApplication.translate
        Results_Table.setWindowTitle(_translate("Results_Table", "MainWindow"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Results_Table", "ФИО"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Results_Table", "Баллы ЕГЭ"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Results_Table", "Баллы ИД"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Results_Table", "Оригинал"))
        self.label.setText(_translate("Results_Table", "Таблица по:"))
        self.comboBox.setItemText(0, _translate("Results_Table", "Университет"))
        self.comboBox.setItemText(1, _translate("Results_Table", "Прикладная математика"))
        self.comboBox.setItemText(2, _translate("Results_Table", "Информатика и вычислительная техника"))
        self.comboBox.setItemText(3, _translate("Results_Table", "Автоматизация управления в технических системах"))
        self.comboBox.setItemText(4, _translate("Results_Table", "Инфокоммуникационные технологии"))
        self.comboBox.setItemText(5, _translate("Results_Table", "Защищенные сети и системы"))
        self.btn_go_to_main.setText(_translate("Results_Table", "Вернуться на главную"))
