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

        #Eventi
        self.ui.closeBtn.clicked.connect(self.close)
        self.ui.minimizeBtn.clicked.connect(self.showMinimized)
        self.ui.restoreBtn.clicked.connect(self.toggleFullscreen)
        # TODO: rendere reponsive i tasti con qualche effetto o box-shadow
        # Mostra la finestra
        self.show()

    def toggleFullscreen(self):
        if self.isFullScreen():
            self.showNormal()  # Ripristina la finestra al suo stato precedente
        else:
            self.showFullScreen()


# Execute APP
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Data_Tool_Application()
    sys.exit(app.exec())
    print('commit tested')