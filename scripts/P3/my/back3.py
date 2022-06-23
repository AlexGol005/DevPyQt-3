import time
from my3 import Ui_Form
from PySide2 import QtWidgets, QtGui, QtCore



class MyWindow(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        # self.ui = Ui_Form()
        # self.ui.setupUi(self)
        self.initThreads()
        self.initUi()

    def initUi(self):
        """
        Метод инициализации пользовательского интерфейса
        """

        # init QLineEdit
        self.lineEdit = QtWidgets.QLineEdit()
        self.lineEdit.setPlaceholderText("Введите количество секунд")

        # init QPushButton START
        self.pbStart = QtWidgets.QPushButton()
        self.pbStart.setText("Старт")

        # init QPushButton STOP
        self.pbStop = QtWidgets.QPushButton()
        self.pbStop.setText("Стоп")
        self.pbStop.setEnabled(False)

        # init main layout
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addWidget(self.lineEdit)
        main_layout.addWidget(self.pbStart)
        main_layout.addWidget(self.pbStop)

        # set main layout on main widget
        self.setLayout(main_layout)

        self.pbStart.clicked.connect(self.startTimerThread)

    def timerSignalEmit(self, emit_value):
        """
        Метод-слот для отработки сигнала timerSignal потока self.timerThread

        Будет срабатывать, когда в потоке у сигнала self.timerSignal, будет вызываться метод emit()
        П-р: self.timerSignal.emit(str(self.timerCount))
        """

        self.lineEdit.setText(emit_value)

    def initThreads(self):

        # create QThread instance
        self.timerThread = TimerThread()


    def startTimerThread(self):
        self.timerThread.start()
        self.timerThread.timerSignal.connect(self.timerSignalEmit)
    #
    #     # init signals
    #     self.timerThread.started.connect(self.timerThreadStarted)
    #     self.timerThread.finished.connect(self.timerThreadFinished)
    #
    #     self.timerThread.timerSignal.connect(self.timerSignalEmit)
    #
    # def onPBStartClicked(self):
    #
    #     try:
    #         self.timerThread.timerCount = int(
    #             self.lineEdit.text())  # установка числа относительно которого начнётся отсчёт
    #         self.timerThread.start()  # запуск потока
    #     except ValueError:  # обработка сценария, если пользователь введёт не число
    #         self.lineEdit.setText("")
    #         QtWidgets.QMessageBox.warning(self, "Ошибка", "Введено неправильное значение")
    #
    # def onPBStopClicked(self):
    #
    #     self.timerThread.status = False
    #
    # def timerThreadStarted(self):
    #
    #
    #     self.pbStart.setEnabled(False)
    #     self.pbStop.setEnabled(True)
    #     self.lineEdit.setEnabled(False)
    #
    # def timerThreadFinished(self):
    #     self.pbStart.setEnabled(True)
    #     self.pbStop.setEnabled(False)
    #     self.lineEdit.setEnabled(True)
    #
    #     self.lineEdit.setText("")
    #
    # def timerSignalEmit(self, emit_value):
    #
    #     self.lineEdit.setText(emit_value)


class TimerThread(QtCore.QThread):
    timerSignal = QtCore.Signal(str)  # создаём кастомный сигнал для потока

    # def __init__(self, parent=None):
    #     super(TimerThread, self).__init__(parent)
    #
    #     self.timerCount = None
    #     self.status = True

    def run(self):
        # self.status = True
        # while self.status:
        #     time.sleep(1)
        #     self.timerCount -= 1
        #     self.timerSignal.emit(str(self.timerCount))
        for i in range(10,0,-1):
            time.sleep(1)
            print(i)
            self.timerSignal.emit(str(i))



# class Site(QtCore.QThread):
#     pass
#
# class Sistem(QtCore.QThread):
#     pass



if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = MyWindow()
    win.show()

    app.exec_()