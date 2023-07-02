#imports
import sys
import os
#import GUI file
from Data_Cleaner_Tool.UI.ui_data_tool import *

#Classe principale
class Data_Tool_Application(QMainWindow):
    def __init__(self,parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Eventi close/minimize/fullScreen
        self.ui.closeBtn.clicked.connect(self.close)
        self.ui.minimizeBtn.clicked.connect(self.showMinimized)
        self.ui.restoreBtn.clicked.connect(self.toggleFullscreen)
        #Eventi hover icone di sistema
        self.ui.systemBtns.enterEvent = lambda event: self.hover_system_icons()
        self.ui.systemBtns.leaveEvent = lambda event: self.reset_system_icons()

        # Mostra la finestra
        self.show()

    def toggleFullscreen(self):
        if self.isFullScreen():
            self.showNormal()  # Ripristina la finestra al suo stato precedente
        else:
            self.showFullScreen()
    def hover_system_icons(self):
        print('enter')
        self.ui.closeBtn.setIcon(QIcon(u":/icons/icons/hover-closeIconMacOS.svg"))
        self.ui.minimizeBtn.setIcon(QIcon(u":/icons/icons/hover-minimizeIconMacOS.svg"))
        self.ui.restoreBtn.setIcon(QIcon(u":/icons/icons/hover-fullscreenIconMacOS.svg"))
    def reset_system_icons(self):
        print('reset')
        self.ui.closeBtn.setIcon(QIcon(u":/icons/icons/closeIconMacOS.svg"))
        self.ui.minimizeBtn.setIcon(QIcon(u":/icons/icons/minimizeIconMacOS.svg"))
        self.ui.restoreBtn.setIcon(QIcon(u":/icons/icons/fullscreenIconMacOS.svg"))


# Execute APP
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Data_Tool_Application()
    sys.exit(app.exec())