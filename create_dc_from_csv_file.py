import csv

def create_dc_from_csv(file_name):
# Указываем имя файла CSV, из которого хотим прочитать данные

    # Создаем пустой список для хранения словарей
    data = []

    # Открываем файл CSV для чтения в режиме чтения ('r' - read)
    with open(file_name, mode='r', newline='', encoding='utf-8') as file:
        # Создаем объект для чтения CSV
        reader = csv.reader(file)

        # Читаем данные из файла и преобразуем их в словари
        for ind, row in enumerate(reader):
            if ind == 0:
                klasss = {x: {} for x in row[1:]}

            else:
                for jnd, klas in enumerate(klasss):
                    klasss[klas][row[0]] = row[jnd+1]
            data.append(row)
        res = klasss
        return res
