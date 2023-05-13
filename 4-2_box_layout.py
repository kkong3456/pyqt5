import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QHBoxLayout,QVBoxLayout

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        okButton=QPushButton('OK',self)
        cancelButton=QPushButton('Cancel')
        
        okButton2=QPushButton('OK2',self)
        cancelButton2=QPushButton('Cancel2')
        
        hbox=QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        hbox.addStretch(1)
        
        hbox2=QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(okButton2)
        hbox2.addWidget(cancelButton2)
        hbox2.addStretch(1)
        
        vbox=QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addLayout(hbox2)
        vbox.addStretch(1)
        
        self.setLayout(vbox)
        
        self.setWindowTitle('Box Layout')
        self.setGeometry(300,300,300,200)
        self.show()
        
if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=MyApp()
    sys.exit(app.exec_())