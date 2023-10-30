import sys
import csv
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem

# Создаем приложение и главное окно
app = QApplication(sys.argv)
main_window = QMainWindow()

# Создаем таблицу
table = QTableWidget()
main_window.setCentralWidget(table)

# Открываем CSV-файл и считываем данные
with open('static/csv/1 класс.csv',encoding='utf-8', newline='') as csvfile:
    reader = csv.reader(csvfile)
    data = list(reader)

# Определяем день, для которого вы хотите вывести расписание
day = "Понедельник"

# Находим индекс столбца, соответствующего выбранному дню
day_column = data[0].index("день")

# Фильтруем данные только для выбранного дня
filtered_data = [row for row in data if row[day_column] == day]

# Устанавливаем количество строк и столбцов в таблице
table.setRowCount(len(filtered_data))
table.setColumnCount(len(filtered_data[0]))

# Заполняем таблицу данными для выбранного дня
for row_num, row_data in enumerate(filtered_data):
    for col_num, cell_data in enumerate(row_data):
        item = QTableWidgetItem(cell_data)
        table.setItem(row_num, col_num, item)

# Устанавливаем заголовки столбцов
table.setHorizontalHeaderLabels(data[0])

# Устанавливаем название дня
main_window.setWindowTitle(day)

# Отображаем окно
main_window.show()

# Запускаем приложение
sys.exit(app.exec_())
