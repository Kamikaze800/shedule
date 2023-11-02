import csv
import math

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
        teach_count_dc[klas][data_teach_klas[ind + 1][jnd + 1]] = int(data_subject_count[ind + 1][jnd + 1])

# self.day_table.currentText()
# self.num_klas_table.text()
class Parallel:
    def __init__(self, klass):
        self.klass = klass
        def create_klas_shedule(klass, mid):
            schedule = []
            for day in range(5):
                daily_schedule = []
                for klas in klass:
                    schedule_klas = []
                    ind_les = 0
                    les = 0
                    while les < len(klas.keys()) and len(schedule_klas) < mid and sum(klas.values())>0:
                        mx = len(schedule_klas)
                        ind_les_sp = [sched[ind_les] for sched in daily_schedule if len(sched) > mx]
                        teach = list(klas.keys())[les]
                        if klas[teach] > 0 and teach not in ind_les_sp and schedule_klas.count(teach) < 2:
                            schedule_klas.append(teach)
                            klas[teach] -= 1
                            ind_les += 1
                            les = 0
                        else:
                            les += 1
                    daily_schedule.append(schedule_klas)
                schedule.append(daily_schedule)
            return schedule

        res = create_klas_shedule(klass, max([sum(x.values()) for x in klass])/5)
        ost = create_klas_shedule(klass, max([sum(x.values()) for x in klass])/5)
        for ind in range(len(res)):
            for jnd in range(len(res[ind])):
                res[len(res[ind]) - ind - 1][jnd] += ost[ind][jnd]
        self.res = res

    def vyvod(self):
        return self.res

russian_alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
week_days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"]
klass = list(teach_count_dc.keys())

def create_klas_shedule(klas):
    teach_count_sp = [teach_count_dc[klas], teach_count_dc[klas].copy(), teach_count_dc[klas].copy(), teach_count_dc[klas].copy()]
    klas_1_shedule = Parallel(teach_count_sp)
    klas_1_shedule_row = klas_1_shedule.vyvod()
    for ind_day, day in enumerate(week_days):
        shedule_today = klas_1_shedule_row[ind_day]
        with open(f'static/csv/{klas}/{day}.csv', 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([*[russian_alphabet[i] for i in range(len(teach_count_sp))]])
            for ind_lesson in range(len(max(shedule_today, key=len))):
                sp = []
                for letter_of_klas in range(len(shedule_today)):
                    if ind_lesson < len(shedule_today[letter_of_klas]):
                        sp.append(shedule_today[letter_of_klas][ind_lesson])
                writer.writerow(sp)

for ind, val in enumerate(klass):
    create_klas_shedule(val)
b = 1