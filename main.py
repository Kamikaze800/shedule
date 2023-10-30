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
        # self.qdilog_count_sub_table = qdilog_count_sub_class()
        # self.qdilog_teach_sub_table = qdilog_teach_sub_class()

    def view_count_sub_table_def(self):
        self.qdilog_count_sub_table.show()
        self.qdilog_count_sub_table.exec_()

    def view_teach_sub_table_def(self):
        self.qdilog_teach_sub_table.show()
        self.qdilog_teach_sub_table.exec_()

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


def main():
    app = QApplication(sys.argv)
    window = Shedule()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
