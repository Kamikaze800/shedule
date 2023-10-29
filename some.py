from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Главное окно")
        widget = QWidget()
        self.setCentralWidget(widget)
        button = QPushButton("Кнопка", self)
        widget.layout().addWidget(button)

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Виджет")
        button = QPushButton("Кнопка", self)
        self.layout().addWidget(button)

if __name__ == '__main__':
    app = QApplication([])
    main_window = MyMainWindow()
    main_window.show()

    widget = MyWidget()
    widget.show()

    app.exec_()
