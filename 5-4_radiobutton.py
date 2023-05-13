import sys 
from PyQt5.QtWidgets import QApplication,QWidget,QRadioButton 

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        rbtn1=QRadioButton('Frist Button',self)
        rbtn1.move(50,50)
        rbtn1.setChecked(True)
        rbtn1.toggled.connect(self.selectedOrNot)
        
        rbtn2=QRadioButton('Seond Button',self)
        rbtn2.move(50,70)
        rbtn2.setText('SecondButton')
        
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('QRadioButton')
        self.show()
        
    def selectedOrNot(self):
        print('xxx')
        
if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=MyApp()
    sys.exit(app.exec_())