import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # self.setStyleSheet('background-color:white;')
        label=QLabel('금리환율')
        
        hor_line=QFrame()
        hor_line.setFrameShape(QFrame.HLine)
        hor_line.setFrameShadow(QFrame.Sunken)
        
        widget=QWidget()
        v_layout=QVBoxLayout(widget)
        
        self.tableWidget=QTableWidget()
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(5)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.setStyleSheet('gridline-color:red;border:1px solid;')
        
        self.tableWidget.setItem(0,0,QTableWidgetItem('국고채 3년'))
        
        item=QTableWidgetItem('3.18')
        # item.setForeground(QBrush(QColor(255,0,0)))
        self.tableWidget.setItem(0,1,item)
        
        
        self.tableWidget.setItem(1,0,QTableWidgetItem('회사채 3년'))
        item=QTableWidgetItem('4.17')
        # item.setForeground(QBrush(QColor(255,0,0)))
        self.tableWidget.setItem(1,1,item)
        
        #layout
        v_layout.addWidget(label)
        v_layout.addWidget(hor_line)
        v_layout.addWidget(self.tableWidget)
        self.setCentralWidget(widget)
        # self.layout(v_layout)
        
        
if __name__=='__main__':
    app=QApplication(sys.argv)
    mywindow=MyWindow()
    mywindow.show()
    app.exec_()
        
        
        
        