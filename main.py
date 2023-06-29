#imports
import sys
import os
#import GUI file
from Data_Cleaner_Tool.UI.data_tool import *

#Classe principale
class Data_Tool_Application(QMainWindow):
    def __init__(self,parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()


# Execute APP
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Data_Tool_Application()
    sys.exit(app.exec())