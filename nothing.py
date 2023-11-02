import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Главное окно')
        self.setGeometry(100, 100, 400, 200)

        button = QPushButton('Открыть новое окно', self)
        button.clicked.connect(self.openNewWindow)

    def openNewWindow(self):
        new_window = AdditionalWindow()
        new_window.show()

class AdditionalWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Дополнительное окно')
        self.setGeometry(200, 200, 300, 150)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
