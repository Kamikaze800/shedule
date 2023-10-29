import csv
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, \
    QPushButton, QDialog
from PyQt5 import uic
from all_subject_count_dc import all_subject_count_dc_res
from shedule_dc import shedule_dc
# from tst import table_sub_count


class Shedule(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.initUI()
        uic.loadUi('main.ui', self)
        self.sub_teach_dc = {'И.Р.Худ': 'Русский язык', 'С.А.Науман': 'Физика', 'Н.Н.Священко': 'Иностранный язык', 'Ч.Е.Нонова': 'Математика'}
        self.view_table_but.clicked.connect(self.view_table_def)
        self.table_save_changes.clicked.connect(self.table_save_changes_def)
        self.view_count_sub_table.clicked.connect(self.view_count_sub_table_def)
        self.view_teach_sub_table.clicked.connect(self.view_teach_sub_table_def)
        self.qdilog_count_sub_table = qdilog_count_sub_class()
        self.qdilog_teach_sub_table = qdilog_teach_sub_class()
        # with open('csc', encoding='utf-8') as f:
        #     f

        # a = Parallel({'рус': 3, 'мат': 6, 'ист': 2, 'общ': 2, 'физ': 6},
        #              {'рус': 6, 'мат': 3, 'ист': 5, 'общ': 4, 'физ': 1, 'право': 2})

    def view_count_sub_table_def(self):
        self.qdilog_count_sub_table.show()
        self.qdilog_count_sub_table.exec_()

    def view_teach_sub_table_def(self):
        self.qdilog_teach_sub_table.show()
        self.qdilog_teach_sub_table.exec_()
    def table_save_changes_def(self):
        pass
    def view_table_def(self):

        # очищаем содержимое ячеек
        self.tableWidget.clearContents()

        # словарь горизонтальных заголовков таблицы со значением номера столбца
        # {'А': 0, 'Б': 1, 'В': 2, 'Г': 3, 'Д': 4}
        column_header_items = {self.tableWidget.horizontalHeaderItem(i).text(): i for i in
                               range(self.tableWidget.columnCount())}

        # словарь расписаний всех классов в выбранный день
        # {'1Г': 'обц, рус, мат, ист', '2A': 'рус, мат, ист, обц'}
        dc_curent_day = shedule_dc[self.day_table.currentText()]

        # список классов выбранной параллели
        # ['1A', '1Б', '1В', '1Г']
        current_klasses = [x for x in dc_curent_day.keys() if
                           self.num_klas_table.text() in x]

        for ind, klas in enumerate(dc_curent_day):
            if klas in current_klasses:
                for num_les, teach in enumerate(dc_curent_day[klas].split(', ')):
                    int_row = num_les # строка
                    letter = klas[1] # буква класса
                    int_column = column_header_items[letter] # колонка
                    item = self.sub_teach_dc[teach]
                    self.tableWidget.setItem(int_row, int_column, QTableWidgetItem(item))

class qdilog_count_sub_class(QDialog):
    def __init__(self):
        super().__init__()
        table = QTableWidget()
        # main_widget = QWidget(window)
        layout = QVBoxLayout(self)

        # Открываем файл CSV и читаем данные
        with open('subject_count.csv', 'r', encoding='utf-8') as file:
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

class qdilog_teach_sub_class(QDialog):
    def __init__(self):
        super().__init__()
        table = QTableWidget()
        # main_widget = QWidget(window)
        layout = QVBoxLayout(self)

        # Открываем файл CSV и читаем данные
        with open('teach_klas.csv', 'r', encoding='utf-8') as file:
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


if __name__ == '__main__':
    main()