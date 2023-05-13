import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtCore import QDate,QTime,Qt,QDateTime

now=QDate.currentDate()
print(now.toString('yyyy-MM-dd'))

time=QTime.currentTime()
print(time.toString())
print(time.toString('hh:mm:ss:zzzzzzzz'))

datetime=QDateTime.currentDateTime()
print(datetime.toString('yyyy-MM-dd hh:mm:ss'))
print(datetime.toString(Qt.DefaultLocaleLongDate))
print(datetime.toString(Qt.DefaultLocaleShortDate))


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.date=QDate.currentDate()
        self.initUI()
        
    def initUI(self):
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))
        self.setWindowTitle('Date')
        self.setGeometry(300,300,400,200)
        self.show()
        
if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=MyApp()
    sys.exit(app.exec_())




