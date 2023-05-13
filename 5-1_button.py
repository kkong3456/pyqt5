import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QVBoxLayout,QHBoxLayout

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        btn1=QPushButton('&Button1',self)
        # btn1.setCheckable(False)
        btn1.toggle()
        
        btn2=QPushButton(self)
        btn2.setText('Bttuon&2')
        
        btn3=QPushButton('Button3',self)
        btn3.setEnabled(False)
        
        vbox=QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addStretch(1)
        
        hbox=QHBoxLayout()
        hbox.addStretch(1)
        hbox.addLayout(vbox)
        hbox.addStretch(1)
        
        
       
        
        self.setLayout(hbox)
        self.setWindowTitle('QPushButton')
        self.setGeometry(300,300,300,200)
        self.show()
        
if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=MyApp()
    sys.exit(app.exec_())
        