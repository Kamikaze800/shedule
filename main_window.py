import csv

import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, \
    QPushButton, QDialog, QMessageBox
from PyQt5 import uic
from create_dc_from_csv_file import create_dc_from_csv
from main_ui import *
from trash import *

class Shedule(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.ui = Ui_MainWindow()
        # self.ui.setupUi(self)
        self.setWindowIcon(QIcon('static/img/table.png'))
        self.ui.view_table_but.clicked.connect(self.view_table_def)
        self.ui.view_count_sub_table.clicked.connect(self.view_count_sub_table_def)
        self.ui.view_teach_sub_table.clicked.connect(self.view_teach_sub_table_def)
        self.ui.qwidget_count_sub_table = shablon_table_view('subject_count.csv')
        self.ui.qwidget_teach_sub_table = shablon_table_view('teach_klas.csv')
        self.ui.generation_but.clicked.connect(self.generation_def)
        self.setWindowTitle("Генерация расписаний")
        self.ui.save_table_btn.clicked.connect(self.save_table_def)

    def save_table_def(self):
        with open(f'static/csv/{self.ui.num_klas_table.text()} класс/{self.ui.day_table.currentText()}.csv', 'w',
                  encoding='utf-8', newline='') as csv_file:
            # input()
            dig = 0
            csv_writer = csv.writer(csv_file)
            sp = []
            for row in range(self.ui.tableWidget.rowCount()):
                row_data = []
                for column in range(self.ui.tableWidget.columnCount()):
                    item = self.ui.tableWidget.item(row, column)
                    if item is not None:
                        row_data.append(item.text())
                sp.append(row_data)
            russian_alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
            csv_writer.writerow(russian_alphabet[0:len(max(sp, key=len))])
            for row_data in sp:
                csv_writer.writerow(row_data)
    def generation_def(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        msg.setText("Вы точно хотите выполнить генерацию?")
        msg.setWindowTitle("Подтверждение")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        result = msg.exec_()
        if result == QMessageBox.Yes:
            # Действия при нажатии кнопки "Да"
            trash_def()

    def view_count_sub_table_def(self):
        self.ui.qwidget_count_sub_table.show()


    def view_teach_sub_table_def(self):
        self.ui.qwidget_teach_sub_table.show()


    def table_save_changes_def(self):
        pass

    def view_table_def(self):
        self.ui.tableWidget.clearContents()
        with open(f'static/csv/{self.ui.num_klas_table.text()} класс/{self.ui.day_table.currentText()}.csv', 'r',
                  encoding='utf-8') as file:
            reader = csv.reader(file)
            data = list(reader)
        with open(f'static/csv/teach_klas.csv', 'r',
                  encoding='utf-8') as file:
            reader = csv.reader(file)
            sub_teach = create_dc_from_csv('static/csv/teach_klas.csv')[f'{self.ui.num_klas_table.text()} класс']
        # Заполняем таблицу данными из файла
        for i, row in enumerate(data[1:]):
            for j, value in enumerate(row):
                subject = ''
                for key, teach in sub_teach.items():
                    if teach == value:
                        subject = key
                        break
                table_item = QTableWidgetItem(subject)
                self.ui.tableWidget.setItem(i, j, table_item)

class shablon_table_view(QWidget):
    def __init__(self, file_name):
        super().__init__()
        table = QTableWidget()
        table = QTableWidget()

        # main_widget = QWidget(window)
        layout = QVBoxLayout(self)
        self.file_name = file_name

        # Открываем файл CSV и читаем данные
        with open(f'static/csv/{file_name}', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = list(reader)

        # Устанавливаем количество строк и столбцов в таблице
        num_rows = len(data)
        num_cols = len(data[0])
        table.setRowCount(num_rows)
        table.setColumnCount(num_cols)

        # Заполняем таблицу данными из файла
        for i, row in enumerate(data):
            for j, value in enumerate(row):
                table_item = QTableWidgetItem(value)
                table.setItem(i, j, table_item)

        # Убираем нумерацию строк и столбцов
        table.verticalHeader().setVisible(False)
        table.horizontalHeader().setVisible(False)

        # Масштабируем таблицу под контент
        table.resizeColumnsToContents()
        table.resizeRowsToContents()

        # кнопка появляется при изменении поля

        button = QPushButton("Save Changes", self)
        button.clicked.connect(self.saveToCSV)

        layout.addWidget(table)
        layout.addWidget(button)
        self.setLayout(layout)
        self.resize(table.size())
        self.table = table

    def saveToCSV(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        msg.setText("Вы точно хотите сохранить изменения?")
        msg.setWindowTitle("Подтверждение")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        result = msg.exec_()
        if result == QMessageBox.Yes:
            with open(f'static/csv/{self.file_name}', 'w', encoding='utf-8', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                for row in range(self.table.rowCount()):
                    row_data = []
                    for column in range(self.table.columnCount()):
                        item = self.table.item(row, column)
                        if item is not None:
                            row_data.append(item.text())
                        else:
                            row_data.append('')
                    csv_writer.writerow(row_data)



def main_window_def():
    app = QApplication(sys.argv)
    window = Shedule()
    window.show()
    sys.exit(app.exec_())

main_window_def()