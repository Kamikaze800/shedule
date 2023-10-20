import csv

with open('shedule.csv', mode='r', newline='', encoding='utf-8') as file:
    # Создаем объект для чтения CSV
    reader = csv.reader(file)
    # print(reader)
    sp = []
    dc = {}

    teach_sub_count = {}
    for ind, row in enumerate(reader):
        if ind == 0:
            dc = {x: {} for x in row[1:]}
        else:
            for jnd, val in enumerate(dc):
                try:
                    day_shedule = row[jnd + 1]
                except Exception:
                    day_shedule = ""
                dc[val][row[0]] = day_shedule
        # dc[row[0]] = row[1]
        # sp.append(row)
shedule_dc = dc
print(shedule_dc)
