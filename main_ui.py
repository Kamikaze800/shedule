# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(674, 377)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 40, 521, 241))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        self.num_klas_table = QtWidgets.QSpinBox(self.centralwidget)
        self.num_klas_table.setGeometry(QtCore.QRect(270, 10, 42, 22))
        self.num_klas_table.setMinimum(1)
        self.num_klas_table.setMaximum(11)
        self.num_klas_table.setObjectName("num_klas_table")
        self.day_table = QtWidgets.QComboBox(self.centralwidget)
        self.day_table.setGeometry(QtCore.QRect(160, 10, 91, 20))
        self.day_table.setObjectName("day_table")
        self.day_table.addItem("")
        self.day_table.addItem("")
        self.day_table.addItem("")
        self.day_table.addItem("")
        self.day_table.addItem("")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(320, 10, 47, 13))
        self.label_6.setObjectName("label_6")
        self.view_table_but = QtWidgets.QPushButton(self.centralwidget)
        self.view_table_but.setGeometry(QtCore.QRect(370, 10, 75, 23))
        self.view_table_but.setObjectName("view_table_but")
        self.view_count_sub_table = QtWidgets.QPushButton(self.centralwidget)
        self.view_count_sub_table.setGeometry(QtCore.QRect(580, 130, 75, 23))
        self.view_count_sub_table.setObjectName("view_count_sub_table")
        self.view_teach_sub_table = QtWidgets.QPushButton(self.centralwidget)
        self.view_teach_sub_table.setGeometry(QtCore.QRect(580, 190, 75, 23))
        self.view_teach_sub_table.setObjectName("view_teach_sub_table")
        self.generation_but = QtWidgets.QPushButton(self.centralwidget)
        self.generation_but.setGeometry(QtCore.QRect(580, 70, 75, 23))
        self.generation_but.setObjectName("generation_but")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(580, 110, 71, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(560, 170, 111, 20))
        self.label_2.setObjectName("label_2")
        self.save_table_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_table_btn.setGeometry(QtCore.QRect(240, 290, 93, 28))
        self.save_table_btn.setObjectName("save_table_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 674, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "А"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Б"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "В"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Г"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Д"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.day_table.setItemText(0, _translate("MainWindow", "Понедельник"))
        self.day_table.setItemText(1, _translate("MainWindow", "Вторник"))
        self.day_table.setItemText(2, _translate("MainWindow", "Среда"))
        self.day_table.setItemText(3, _translate("MainWindow", "Четверг"))
        self.day_table.setItemText(4, _translate("MainWindow", "Пятница"))
        self.label_6.setText(_translate("MainWindow", "класс"))
        self.view_table_but.setText(_translate("MainWindow", "показать"))
        self.view_count_sub_table.setText(_translate("MainWindow", "показать"))
        self.view_teach_sub_table.setText(_translate("MainWindow", "показать"))
        self.generation_but.setText(_translate("MainWindow", "генерация"))
        self.label.setText(_translate("MainWindow", "кол-во часов"))
        self.label_2.setText(_translate("MainWindow", "учителя и предметы"))
        self.save_table_btn.setText(_translate("MainWindow", "сохранить"))
