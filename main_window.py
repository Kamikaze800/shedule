import csv
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, \
    QPushButton, QDialog
from PyQt5 import uic
from create_dc_from_csv_file import create_dc_from_csv


# from tst import table_sub_count


class Shedule(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.initUI()
        uic.loadUi('main.ui', self)
        self.view_table_but.clicked.connect(self.view_table_def)
        self.table_save_changes.clicked.connect(self.table_save_changes_def)
        self.view_count_sub_table.clicked.connect(self.view_count_sub_table_def)
        self.view_teach_sub_table.clicked.connect(self.view_teach_sub_table_def)
        self.qwidget_count_sub_table = shablon_table_view('subject_count.csv')
        self.qwidget_teach_sub_table = shablon_table_view('teach_klas.csv')

    def view_count_sub_table_def(self):
        self.qwidget_count_sub_table.show()
        # self.qwidget_count_sub_table.exec_()

    def view_teach_sub_table_def(self):
        self.qwidget_teach_sub_table.show()
        # self.qdilog_teach_sub_table.exec_()

    def table_save_changes_def(self):
        pass

    def view_table_def(self):
        self.tableWidget.clearContents()
        with open(f'static/csv/{self.num_klas_table.text()} класс/{self.day_table.currentText()}.csv', 'r',
                  encoding='utf-8') as file:
            reader = csv.reader(file)
            data = list(reader)
        with open('teach_klas.csv', 'r',
                  encoding='utf-8') as file:
            reader = csv.reader(file)
            sub_teach = create_dc_from_csv('teach_klas.csv')[f'{self.num_klas_table.text()} класс']
        # Заполняем таблицу данными из файла
        for i, row in enumerate(data[1:]):
            for j, value in enumerate(row):
                subject = ''
                for key, teach in sub_teach.items():
                    if teach == value:
                        subject = key
                        break
                table_item = QTableWidgetItem(subject)
                self.tableWidget.setItem(i, j, table_item)

class shablon_table_view(QWidget):
    def __init__(self, file_name):
        super().__init__()
        table = QTableWidget()
        # main_widget = QWidget(window)
        layout = QVBoxLayout(self)

        # Открываем файл CSV и читаем данные
        with open(f'{file_name}', 'r', encoding='utf-8') as file:
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

        # button.setVisible(False)
        def item_changed():
            button.setVisible(True)

        # Connect the itemChanged signal to the item_changed slot
        table.itemChanged.connect(item_changed)

        def save_changes():
            button.setVisible(False)
            print("Changes saved.")

        layout.addWidget(table)
        layout.addWidget(button)
        self.setLayout(layout)
        self.resize(table.size())

def main():
    app = QApplication(sys.argv)
    window = Shedule()
    window.show()
    sys.exit(app.exec_())

main()