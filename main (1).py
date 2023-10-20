import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5 import uic
class Shedule(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.initUI()
        uic.loadUi('main.ui', self)

        class Parallel:
            def __init__(self, *classes):
                res = []
                mid_count = 4  # среднее кол-во уроков в день
                for i in range(5):
                    shedule_day = []  # расписание на день для всех
                    for klass in classes:
                        shedule_klass = []  # расписание для класса
                        ind = 0  # номер урока
                        big_les = [x for x in klass.keys() if klass[x] > 2]  # если уроков больше 2
                        points = 1  # кол-во предмета в день
                        for les in klass.keys():
                            if les in big_les:
                                points = 2
                            for j in range(points):
                                if klass[les] > 0 and len(
                                        shedule_klass) < mid_count:  # проеряем, что кол-во часов для предмета больше 0
                                    les_ind = []  # уроки классов по номеру.
                                    for x in shedule_day:
                                        # добавлем только те классы, чьё расписание больше или равно нынешнему номеру урока
                                        if len(x) > ind:
                                            les_ind.append(x[ind])
                                    # если нынешний урок не совпадает с уроками по этому же номеру в параллели - добавляем
                                    if les not in les_ind:
                                        shedule_klass.append(les)
                                        # Shedule.tableWidget.setItem(shedule_klass.index(les), classes.index(klass), QTableWidgetItem(les))
                                        klass[les] -= 1
                                        ind += 1
                            points = 1
                        shedule_day.append(shedule_klass)
                    res.append(shedule_day)
                self.res = res


        a = Parallel({'рус': 3, 'мат': 6, 'ист': 2, 'общ': 2, 'физ': 6},
                     {'рус': 6, 'мат': 3, 'ист': 5, 'общ': 4, 'физ': 1, 'право': 2})
        for i in range(len(a.res[0])): # перебираем расписание токо первого дня
            for j in range(len(a.res[0][i])):
                self.tableWidget.setItem(j, i, QTableWidgetItem(a.res[0][i][j]))


def main():
    app = QApplication(sys.argv)
    window = Shedule()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
