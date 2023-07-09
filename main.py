#imports
import sys
import os
from pathlib import PurePath
#import GUI file
from PySide6.QtGui import QDragEnterEvent, QDropEvent
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

        #Eventi hover per cambiare icone di sistema
        self.ui.systemBtns.enterEvent = lambda event: self.hover_system_icons()
        self.ui.systemBtns.leaveEvent = lambda event: self.reset_system_icons()

        #Evento drag&Drop
        self.ui.dropBoxFrame.dragEnterEvent = lambda event: self.dragEnterEvent(event)
        self.ui.dropBoxFrame.dropEvent = lambda event: self.dropEvent(event)

        # Frameless
        self.setWindowFlags(Qt.FramelessWindowHint)

        #Val iniziale posizione cursore
        self.oldPos = None

        # Mostra la finestra
        self.show()

    #Fuzioni spostamento della finestra
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton and self.ui.headerContainer.geometry().contains(event.position().toPoint()):
            self.oldPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if self.oldPos is not None:
            delta = event.globalPosition().toPoint() - self.oldPos
            self.move(self.pos() + delta)
            self.oldPos = event.globalPosition().toPoint()

    def mouseReleaseEvent(self, event):
        self.oldPos = None


    #Funzioni tasti di sistema
    def toggleFullscreen(self):
        if self.isFullScreen():
            self.showNormal()  # Ripristina la finestra al suo stato precedente
        else:
            self.showFullScreen()
    def hover_system_icons(self):
        #print('enter')
        self.ui.closeBtn.setIcon(QIcon(u":/icons/icons/hover-closeIconMacOS.svg"))
        self.ui.minimizeBtn.setIcon(QIcon(u":/icons/icons/hover-minimizeIconMacOS.svg"))
        self.ui.restoreBtn.setIcon(QIcon(u":/icons/icons/hover-fullscreenIconMacOS.svg"))
    def reset_system_icons(self):
        #print('reset')
        self.ui.closeBtn.setIcon(QIcon(u":/icons/icons/closeIconMacOS.svg"))
        self.ui.minimizeBtn.setIcon(QIcon(u":/icons/icons/minimizeIconMacOS.svg"))
        self.ui.restoreBtn.setIcon(QIcon(u":/icons/icons/fullscreenIconMacOS.svg"))

    #Funzioni drag&drop file input
    def dragEnterEvent(self, event: QDragEnterEvent):
        #print('drag event')
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
    def dropEvent(self, event: QDropEvent):
        urls = event.mimeData().urls()

        if urls:
            file_path = urls[0].toLocalFile()
            print(file_path, len(file_path))
            self.dropUptLabels(file_path)
            self.updateStatus(file_path)

    # Aggiornamento barra di stato
    def updateStatus(self,input_file):
        # TODO: aggiungere labelFooterCentral e labelFooterLeft
            if self.check_file_input(input_file):
                self.ui.labelFooterRight.setText(f'Ready')
            else:
                self.ui.labelFooterRight.setText(f'Formato file non corretto')

    # Aggiornamento del label centrale ed una sezione del footer con una path non troppo lunga
    def dropUptLabels(self, file_path):
        path = file_path
        path_parts = path.split(os.sep)
        i = 2
        k = len(file_path)

        while k> 50 and len(path_parts)>4:
            path = os.sep.join(path_parts[:len(file_path.split(os.sep))-i])+os.sep+'...'+os.sep+os.sep.join(path_parts[-2:])
            path_parts = path.split(os.sep)
            i = i+1
            k = len(path)

        self.ui.dragLabel.setText(f"{path}")
        self.ui.labelFooterLeft.setText(f'...{os.sep}{os.sep.join(path_parts[-1:])}  >  ...{os.sep}{PurePath(file_path).stem}_out.csv')

    #Controllo formato files di input
    def check_file_input(self,file_path):
        if file_path.endswith(('.txt','.csv','.tsv')):
            return True
        else:
            return False

# Execute APP
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Data_Tool_Application()

    sys.exit(app.exec())