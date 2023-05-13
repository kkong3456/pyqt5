import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        btn=QPushButton(text="Quit",parent=self)
        btn.move(50,50)
        btn.resize(btn.sizeHint())
        print('=--------------')
        print(btn.resize(btn.minimumSizeHint()))
        print('=--==-----------')
        btn.clicked.connect(QCoreApplication.instance().quit)
        
        self.setWindowTitle('Quit Button')
        self.setGeometry(300,300,300,200)
        self.show()
        
if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=MyApp()
    sys.exit(app.exec_())

