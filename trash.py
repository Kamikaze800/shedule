# res = {'класс 1': {'рус': 3, 'мат': 6, 'ист': 2, 'общ': 2, 'физ': 6}, 'класс 2': {'рус': 6, 'мат': 3, 'ист': 5, 'общ': 4, 'физ': 1, 'право': 2}}
# from all_subject_count_dc import all_subject_count_dc_res
import csv


with open('teach_klas.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    data_teach_klas = list(reader)

with open('subject_count.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    data_subject_count = list(reader)
# cоздание словаря типа класс: {учитель: часы}
teach_count_dc = {x: {} for x in data_teach_klas[0][1:]}  # классы
for ind in range(len(data_subject_count[1:])):
    for jnd, klas in enumerate(teach_count_dc):
        if ind != 0:
            teach_count_dc[klas][data_teach_klas[ind + 1][jnd + 1]] = int(data_subject_count[ind + 1][jnd + 1])

week_days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]


# self.day_table.currentText()
# self.num_klas_table.text()
class Parallel:
    def __init__(self, classes, mid_count):  # кол-во часов предметов для каждой буквы в одной параллели
        self.classes = classes
        self.mid_count = mid_count

    def create_shedule(self, classes):
        res = []  # расписание на неделю для параллели
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
                                shedule_klass) < self.mid_count:  # проеряем, что кол-во часов для предмета больше 0
                            les_ind = []  # уроки классов по номеру.
                            for x in shedule_day:
                                # добавлем только те классы, чьё расписание больше или равно нынешнему номеру урока
                                if len(x) > ind:
                                    les_ind.append(x[ind])
                            # если нынешний урок не совпадает с уроками по этому же номеру в параллели - добавляем
                            if les not in les_ind:
                                shedule_klass.append(les)
                                klass[les] -= 1
                                ind += 1
                    points = 1
                shedule_day.append(shedule_klass)
            res.append(shedule_day)
        return res

    def vyvod(self):
        rs = self.create_shedule(self.classes)
        rs_ost = self.create_shedule(self.classes)
        for i in range(len(rs_ost)):
            for j in range(len(rs_ost[i])):
                rs[i][j] += rs_ost[i][j]
        # for i in rs:
        #     print(i)
        return rs

russian_alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
klass = list(teach_count_dc.keys())
def create_klas_shedule(klas):
    teach_count_sp = [teach_count_dc[klas], teach_count_dc[klas].copy(), teach_count_dc[klas].copy(), teach_count_dc[klas].copy()]
    mid_count = max([sum(x.values()) for x in teach_count_sp])/5
    klas_1_shedule = Parallel(teach_count_sp, mid_count)
    klas_1_shedule_row = klas_1_shedule.vyvod()
    with open(f'static/csv/{klas}.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['день', *[russian_alphabet[i] for i in range(len(teach_count_sp))]])
        for i in range(5):
            writer.writerow([week_days[i], *[', '.join(x) for x in klas_1_shedule_row[i]]])

for ind, val in enumerate(klass):
    create_klas_shedule(val)