import csv
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget

# Создаем приложение
app = QApplication([])
window = QMainWindow()
table = QTableWidget()
# main_widget = QWidget(window)
layout = QVBoxLayout(window)

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

button = QPushButton("Save Changes", window)
# button.setVisible(False)
def item_changed():
    button.setVisible(True)

# Connect the itemChanged signal to the item_changed slot
table.itemChanged.connect(item_changed)

def save_changes():
    button.setVisible(False)
    print("Changes saved.")

# layout.addWidget(table)
layout.addWidget(button)
# table_sub_count = table
# Добавляем таблицу в окно приложения
window.setLayout(layout)
window.resize(table.size())
window.setCentralWidget(table)
window.show()

# Запускаем приложение
app.exec_()


