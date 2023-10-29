import csv

# Указываем имя файла CSV, из которого хотим прочитать данные
file_name = "teach_klas.csv"

# Создаем пустой список для хранения словарей
data = []

# Открываем файл CSV для чтения в режиме чтения ('r' - read)
with open(file_name, mode='r', newline='', encoding='utf-8') as file:
    # Создаем объект для чтения CSV
    reader = csv.reader(file)
    for row in reader:
        print(row)
    # klasss = {x: 0 for x in reader[0][1:]}
    # print(klasss)
    # # Читаем данные из файла и преобразуем их в словари
    # for ind, row in enumerate(reader):
    #     if ind == 0:
    #         klasss = {x: {} for x in row[1:]}
    #
    #     else:
    #         for jnd, klas in enumerate(klasss):
    #             klasss[klas][row[0]] = int(row[jnd+1])
    #     data.append(row)
    # all_subject_count_dc_res = klasss
    # b = 1
    # print(all_subject_count_dc_res)