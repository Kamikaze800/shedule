import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5 import uic
from all_subject_count_dc import all_subject_count_dc
from shedule_dc import shedule_dc


class Shedule(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.initUI()
        uic.loadUi('main.ui', self)
        self.sub_teach_dc = {'Vova': 'мат'}
        self.add_sub_teach_but.clicked.connect(self.add_sub_teach_def)
        self.view_table_but.clicked.connect(self.view_table_def)

        # with open('csc', encoding='utf-8') as f:
        #     f

        # a = Parallel({'рус': 3, 'мат': 6, 'ист': 2, 'общ': 2, 'физ': 6},
        #              {'рус': 6, 'мат': 3, 'ист': 5, 'общ': 4, 'физ': 1, 'право': 2})

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
                for num_les, les in enumerate(dc_curent_day[klas].split(', ')):
                    int_row = num_les # строка
                    letter = klas[1]  # буква класса
                    int_column = column_header_items[letter] # колонка
                    self.tableWidget.setItem(int_row, int_column, QTableWidgetItem(les))


    def add_sub_teach_def(self):
        self.sub_teach_dc[self.teach_line.text()] = self.sub_line.text()
        print(self.sub_teach_dc)


def main():
    app = QApplication(sys.argv)
    window = Shedule()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
