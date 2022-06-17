from PySide6.QtCore import Signal, QObject


class MySignal(QObject):
    setremain_num=Signal(str)
    setmake=Signal(str)
    setmodel=Signal(str)
    setdetal=Signal(str)
    setfilename=Signal(str)
    setProgressBar = Signal(int)


my_signal = MySignal()