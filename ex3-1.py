import sys
from PyQt5.QtWidgets import QApplication,QWidget

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My FirstApplication')
        self.move(300,300)
        self.resize(400,200)
        self.show()

if __name__=='__main__':
    print(__name__)
    app=QApplication(sys.argv)
    ex=MyApp()
    sys.exit(app.exec_())