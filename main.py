# imports
import sys
import os
from pathlib import PurePath
# import GUI libraries and core files
from PySide6.QtGui import (QDragEnterEvent, QDropEvent)
from PySide6.QtCore import (QPropertyAnimation, QEasingCurve)
from PySide6.QtWidgets import (QFileDialog)
from Data_Cleaner_Tool.UI.ui_data_tool import *
from Data_Cleaner_Tool.CORE.cleaner_core import *


# Main Class
class DataToolApplication(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        """ ATTRIBUTES LIST """

        self.oldPos = None  # Cursor default position
        self.file_path = None   # FilePath default value

        """ GUI ELEMENTS """

        # Default hidden elements
        self.ui.iconLabelFooterLeft.hide()

        # Show/Hide Menu
        self.ui.MenuBtn.clicked.connect(self.slide_left_menu_container)

        # Events close/minimize/fullScreen
        self.ui.closeBtn.clicked.connect(self.close)
        self.ui.minimizeBtn.clicked.connect(self.showMinimized)
        self.ui.restoreBtn.clicked.connect(self.toggle_fullscreen)

        # Events hover per cambiare icone di sistema
        self.ui.systemBtns.enterEvent = lambda event: self.hover_system_icons()
        self.ui.systemBtns.leaveEvent = lambda event: self.reset_system_icons()
        
        # Events hover per cambiare underline dei file dialog link
        self.ui.browserFileLabel.enterEvent = lambda event: self.file_dialog_link_hover()
        self.ui.browserFileLabel.leaveEvent = lambda event: self.file_dialog_link_normal()

        # Evento drag&Drop
        self.ui.dropBoxFrame.dragEnterEvent = lambda event: self.dragEnterEvent(event)
        self.ui.dropBoxFrame.dropEvent = lambda event: self.dropEvent(event)

        # Frameless
        self.setWindowFlags(Qt.FramelessWindowHint)

        # animation left menubar
        self.animation = QPropertyAnimation(self.ui.leftMenuContainer, b'maximumWidth')

        # This gets the folder the Python file is in and creates the path for the stylesheet
        stylesheet_path = os.path.join(os.path.dirname(__file__), 'Dark_Style.qss')

        with open(stylesheet_path, 'r') as f:
            self.setStyleSheet(f.read())

        # Open File Dialog event
        self.ui.browserFileLabel.mousePressEvent = lambda event: self.open_file_dialog()

        self.show()

    """ STATIC METHODS """
    @staticmethod
    # Truncate too longs paths
    def truncate_path(file_path):
        path = file_path.replace('/', os.sep)
        path_parts = path.split(os.sep)
        i = 2
        k = len(file_path)

        # Truncate long paths
        while k > 50 and len(path_parts) > 4:
            path = (os.sep.join(path_parts[:len(file_path.split(os.sep)) - i]) + os.sep + '...' + os.sep +
                    os.sep.join(path_parts[-2:]))
            path_parts = path.split(os.sep)
            i = i + 1
            k = len(path)
        return path, path_parts

    @staticmethod
    # Validate input files format
    def check_file_input(file_path):
        if file_path.endswith(('.txt', '.csv', '.tsv', '.xls', '.xlsx')):
            return True
        else:
            return False

    """ GUI FUNCTIONS """

    # Workaround function to show underline text on label:hover
    def file_dialog_link_normal(self):
        self.ui.browserFileLabel.setStyleSheet("#browserFileLabel { color: #78A2F6; }")
        
    def file_dialog_link_hover(self):
        self.ui.browserFileLabel.setStyleSheet("#browserFileLabel { color: #78A2F6; text-decoration: underline;}")
    
    # Move windows function
    def mousePressEvent(self, event):
        if (event.button() == Qt.MouseButton.LeftButton and 
                self.ui.headerContainer.geometry().contains(event.position().toPoint())):
            self.oldPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if self.oldPos is not None:
            delta = event.globalPosition().toPoint() - self.oldPos
            self.move(self.pos() + delta)
            self.oldPos = event.globalPosition().toPoint()

    def mouseReleaseEvent(self, event):
        self.oldPos = None

    # Funzioni tasti di sistema
    def toggle_fullscreen(self):
        if self.isFullScreen():
            self.showNormal()  # Ripristina la finestra al suo stato precedente
        else:
            self.showFullScreen()
    
    def hover_system_icons(self):
        # print('enter')
        self.ui.closeBtn.setIcon(QIcon(u":/icons/icons/hover-closeIconMacOS.svg"))
        self.ui.minimizeBtn.setIcon(QIcon(u":/icons/icons/hover-minimizeIconMacOS.svg"))
        self.ui.restoreBtn.setIcon(QIcon(u":/icons/icons/hover-fullscreenIconMacOS.svg"))
    
    def reset_system_icons(self):
        self.ui.closeBtn.setIcon(QIcon(u":/icons/icons/closeIconMacOS.svg"))
        self.ui.minimizeBtn.setIcon(QIcon(u":/icons/icons/minimizeIconMacOS.svg"))
        self.ui.restoreBtn.setIcon(QIcon(u":/icons/icons/fullscreenIconMacOS.svg"))

    # Funzioni drag&drop file input
    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        urls = event.mimeData().urls()

        if urls:
            file_path = urls[0].toLocalFile()
            # print(file_path, len(file_path))
            self.drop_upt_labels(file_path)
            self.update_status(file_path)

    # Aggiornamento barra di stato
    def update_status(self, input_file):
        # TODO: aggiungere labelFooterCentral e labelFooterLeft
        if self.check_file_input(input_file):
            self.ui.labelFooterRight.setText(f'Ready')
        else:
            self.ui.labelFooterRight.setText(f'Formato file non corretto')

    # Aggiornamento del label centrale ed una sezione del footer con una path non troppo lunga
    def drop_upt_labels(self, file_path):
        path, path_parts = self.truncate_path(file_path)

        self.ui.dragLabel.setText(f"{path}")
        self.upt_footer_path(path)

    def upt_footer_path(self, file_path):
        if self.check_file_input(file_path):
            self.ui.iconLabelFooterLeft.show()
            self.ui.labelFooterLeft.setText(
                f'{PurePath(file_path).stem}_out.csv')
        else:
            self.ui.labelFooterLeft.setText(f'[Warning]: Prova a selezionare un altro file')

    # Show/hide menu laterale sinistro
    def slide_left_menu_container(self):
        width = self.ui.leftMenuSubContainer.width()

        if self.ui.MenuBtn.isChecked():
            new_width = 30
            self.ui.homeBtn.setStyleSheet("#homeBtn { border-left: 3px solid #3573f0; border-radius: 0px}")
            self.ui.MenuBtn.setIcon(QIcon(u":/icons/icons/align-justify.svg"))
        else:
            new_width = 156
            self.ui.homeBtn.setStyleSheet("#homeBtn { border: 3px solid #3573f0; background-color: #3573f0; border-radius: 6px}")
            self.ui.MenuBtn.setIcon(QIcon(u":/icons/icons/chevrons-left.svg"))
        # Animate Left Menubar
        self.animation.setDuration(750)
        self.animation.setStartValue(width)
        self.animation.setEndValue(new_width)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()

    # Open file dialog function
    def open_file_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        # options |= QFileDialog.DontUseNativeDialog  # fix for mac ventura error

        self.file_path, type_file = QFileDialog.getOpenFileName(
            self, "Select File", "", "CSV Files (*.csv, *.tsv, *.txt);;Excel Files (*.xls *.xlsx);;Tutti i file (*)",
            options=options)
        file_path, file_parts = self.truncate_path(self.file_path)
        if file_path:
            self.ui.dragLabel.setText(file_path)
            self.upt_footer_path(file_path)
            self.update_status(file_path)


# Execute APP
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DataToolApplication()

    sys.exit(app.exec())
