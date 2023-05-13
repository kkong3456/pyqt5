import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QAction,qApp
from PyQt5.QtGui import QIcon

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        exitAction=QAction(QIcon('exit.png'),'Exit',self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit appliction')
        exitAction.triggered.connect(qApp.quit)
        
        self.statusBar()
        self.statusBar().showMessage('Ready')
        
        menubar=self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu=menubar.addMenu('&File')
        filemenu.addAction(exitAction)
        closeMenu=menubar.addMenu('&Close')
        closeMenu.addAction(exitAction)
        
        self.setWindowTitle('MenuBar')
        self.setGeometry(300,300,300,200)
        self.show()
        
if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=MyApp()
    sys.exit(app.exec_())