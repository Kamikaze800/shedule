from PyQt5 import QtCore, QtGui, QtWidgets
from db_handler import *


class CheckThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)

    def thr_login(self, name, passw):
        if login(name, passw, self.mysignal):
            return True


    def thr_register(self, name, passw):
        register(name, passw, self.mysignal)