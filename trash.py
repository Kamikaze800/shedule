# res = {'класс 1': {'рус': 3, 'мат': 6, 'ист': 2, 'общ': 2, 'физ': 6}, 'класс 2': {'рус': 6, 'мат': 3, 'ист': 5, 'общ': 4, 'физ': 1, 'право': 2}}
week_days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
        # self.day_table.currentText()
        # self.num_klas_table.text()
        class Parallel:
            def __init__(self, classes): # кол-во часов предметов для каждой буквы в одной параллели
                res = [] # расписание на неделю для параллели
                mid_count = 3  # среднее кол-во уроков в день
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
                # for klas in all_subject_count_dc:
                #     odna_paral([klas]*3)

        sp_paral = []
        for i in range(3):
            sp_paral.append(all_subject_count_dc[f'{self.num_klas_table.text()} класс'])
        a = Parallel(sp_paral)
        day = week_days.index(self.day_table.currentText())
        for i in range(len(a.res[day])):  # перебираем расписание токо выбранного дня
            for j in range(len(a.res[day][i])):
                self.tableWidget.setItem(j, i, QTableWidgetItem(a.res[day][i][j]))