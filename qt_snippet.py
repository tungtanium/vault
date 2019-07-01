import sys
from Qt import QtWidgets, QtCore


class BaseWindow(QtWidgets.QWidget):
    def __init__(self):
        super(BaseWindow, self).__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Base Window')
        self.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    w = BaseWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
