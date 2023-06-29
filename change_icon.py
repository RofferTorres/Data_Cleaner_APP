import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class CustomWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Rimuove la barra dei titoli della finestra
        self.setWindowFlag(Qt.FramelessWindowHint)

        # Imposta il colore di sfondo
        self.setStyleSheet("background-color: white;")

        # Crea il pulsante rosso per chiudere la finestra
        close_button = QPushButton("Chiudi", self)
        close_button.setStyleSheet("background-color: red; color: white;")
        close_button.setGeometry(100, 100, 100, 50)
        close_button.clicked.connect(self.close)

        # Crea il pulsante verde per minimizzare la finestra
        minimize_button = QPushButton("Minimizza", self)
        minimize_button.setStyleSheet("background-color: green; color: white;")
        minimize_button.setGeometry(100, 50, 100, 50)
        minimize_button.clicked.connect(self.showMinimized)

        # Crea il pulsante giallo per ingrandire/ripristinare la finestra
        fullscreen_button = QPushButton("Fullscreen", self)
        fullscreen_button.setStyleSheet("background-color: yellow; color: black;")
        fullscreen_button.setGeometry(100, 150, 100, 50)
        fullscreen_button.clicked.connect(self.toggleFullscreen)

        # Imposta le dimensioni della finestra
        self.setGeometry(300, 300, 300, 200)

        # Mostra la finestra
        self.show()

    def toggleFullscreen(self):
        if self.isFullScreen():
            self.showNormal()  # Ripristina la finestra al suo stato precedente
        else:
            self.showFullScreen()  # Ingrandisce la finestra a tutto schermo


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CustomWindow()
    sys.exit(app.exec())
