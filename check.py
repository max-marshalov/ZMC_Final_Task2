# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'check.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Check(object):
    def setupUi(self, Ui_Check):
        Ui_Check.setObjectName("Ui_Check")
        Ui_Check.resize(910, 749)
        self.centralwidget = QtWidgets.QWidget(Ui_Check)
        self.centralwidget.setObjectName("centralwidget")
        self.personal_photo = QtWidgets.QPushButton(self.centralwidget)
        self.personal_photo.setGeometry(QtCore.QRect(30, 80, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.personal_photo.setFont(font)
        self.personal_photo.setObjectName("personal_photo")
        self.paper_photo = QtWidgets.QPushButton(self.centralwidget)
        self.paper_photo.setGeometry(QtCore.QRect(30, 150, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.paper_photo.setFont(font)
        self.paper_photo.setObjectName("paper_photo")
        self.agree_photo = QtWidgets.QPushButton(self.centralwidget)
        self.agree_photo.setGeometry(QtCore.QRect(30, 220, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.agree_photo.setFont(font)
        self.agree_photo.setObjectName("agree_photo")
        self.tabel_photo = QtWidgets.QPushButton(self.centralwidget)
        self.tabel_photo.setGeometry(QtCore.QRect(30, 290, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tabel_photo.setFont(font)
        self.tabel_photo.setObjectName("tabel_photo")
        self.achives_photo = QtWidgets.QPushButton(self.centralwidget)
        self.achives_photo.setGeometry(QtCore.QRect(30, 360, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.achives_photo.setFont(font)
        self.achives_photo.setObjectName("achives_photo")
        self.join_agree_photo = QtWidgets.QPushButton(self.centralwidget)
        self.join_agree_photo.setGeometry(QtCore.QRect(30, 430, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.join_agree_photo.setFont(font)
        self.join_agree_photo.setObjectName("join_agree_photo")
        self.label_FIO = QtWidgets.QLabel(self.centralwidget)
        self.label_FIO.setGeometry(QtCore.QRect(210, 0, 481, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_FIO.setFont(font)
        self.label_FIO.setAlignment(QtCore.Qt.AlignCenter)
        self.label_FIO.setObjectName("label_FIO")
        self.radioButton_good = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_good.setGeometry(QtCore.QRect(30, 540, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_good.setFont(font)
        self.radioButton_good.setStyleSheet("color: rgb(0, 170, 127)")
        self.radioButton_good.setObjectName("radioButton_good")
        self.radioButton_bad = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_bad.setGeometry(QtCore.QRect(210, 540, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_bad.setFont(font)
        self.radioButton_bad.setStyleSheet("color: rgb(143, 12, 30)")
        self.radioButton_bad.setObjectName("radioButton_bad")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setEnabled(False)
        self.checkBox.setGeometry(QtCore.QRect(210, 580, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setEnabled(False)
        self.checkBox_2.setGeometry(QtCore.QRect(420, 580, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setEnabled(False)
        self.checkBox_3.setGeometry(QtCore.QRect(420, 690, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setEnabled(False)
        self.checkBox_4.setGeometry(QtCore.QRect(210, 630, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setEnabled(False)
        self.checkBox_5.setGeometry(QtCore.QRect(420, 630, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_6.setEnabled(False)
        self.checkBox_6.setGeometry(QtCore.QRect(210, 690, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_6.setFont(font)
        self.checkBox_6.setObjectName("checkBox_6")
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(680, 700, 91, 31))
        self.btn_back.setObjectName("btn_back")
        self.btn_send = QtWidgets.QPushButton(self.centralwidget)
        self.btn_send.setGeometry(QtCore.QRect(790, 700, 91, 31))
        self.btn_send.setObjectName("btn_send")
        Ui_Check.setCentralWidget(self.centralwidget)

        self.retranslateUi(Ui_Check)
        QtCore.QMetaObject.connectSlotsByName(Ui_Check)

    def retranslateUi(self, Ui_Check):
        _translate = QtCore.QCoreApplication.translate
        Ui_Check.setWindowTitle(_translate("Ui_Check", "MainWindow"))
        self.personal_photo.setText(_translate("Ui_Check", "???????? ???? ???????????? ????????"))
        self.paper_photo.setText(_translate("Ui_Check", "??????????????"))
        self.agree_photo.setText(_translate("Ui_Check", "???????????????? ???? ??????"))
        self.tabel_photo.setText(_translate("Ui_Check", "????????????????"))
        self.achives_photo.setText(_translate("Ui_Check", "???????????????????????????? ????????????????????"))
        self.join_agree_photo.setText(_translate("Ui_Check", "???????????????? ???? ????????????????????"))
        self.label_FIO.setText(_translate("Ui_Check", "?????????????? ?????? ????????????????"))
        self.radioButton_good.setText(_translate("Ui_Check", "???????????? ??????????"))
        self.radioButton_bad.setText(_translate("Ui_Check", "???????????? ??????????????, ???????????? ??:"))
        self.checkBox.setText(_translate("Ui_Check", "???????? ???? ???????????? ????????"))
        self.checkBox_2.setText(_translate("Ui_Check", "??????????????"))
        self.checkBox_3.setText(_translate("Ui_Check", "???????????????? ???? ??????"))
        self.checkBox_4.setText(_translate("Ui_Check", "????????????????"))
        self.checkBox_5.setText(_translate("Ui_Check", "???????????????????????????? ????????????????????"))
        self.checkBox_6.setText(_translate("Ui_Check", "???????????????? ???? ????????????????????"))
        self.btn_back.setText(_translate("Ui_Check", "????????????"))
        self.btn_send.setText(_translate("Ui_Check", "??????????????????"))
