from PyQt5.QtCore import QThread,pyqtSignal

class External(QThread):  # 这是个骗人型进度条
    """
    Runs a counter thread.
    """
    countChanged = pyqtSignal(int)
    def __del__(self):
        self.wait()
    def run(self):
        import time
        count = 0
        while count<100:
            count +=1
            self.countChanged.emit(count)