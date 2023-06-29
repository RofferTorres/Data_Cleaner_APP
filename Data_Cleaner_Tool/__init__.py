import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QFileDialog


class FileDropWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setAcceptDrops(True)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.label = QLabel("Trascina qui il file")
        layout.addWidget(self.label)

        self.button = QPushButton("Oppure scegli il file")
        self.button.setObjectName("transparent-button")
        layout.addWidget(self.button)

        self.button.clicked.connect(self.openFileDialog)

        self.another_file_label = QLabel("Scegli un altro file...")
        self.another_file_label.setObjectName("another-file-label")
        layout.addWidget(self.another_file_label)
        self.another_file_label.hide()

        self.another_file_label.linkActivated.connect(self.openFileDialog)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        files = [url.toLocalFile() for url in event.mimeData().urls()]
        if files:
            self.label.setText(files[0])
            self.button.hide()
            self.another_file_label.show()

    def openFileDialog(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName()
        if file_path:
            self.label.setText(file_path)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    app.setStyleSheet("""
        #transparent-button {
            border: none;
            background-color: transparent;
            color: blue;
            text-decoration: none;
            padding: 0;
        }

        #another-file-label {
            color: blue;
            text-decoration: underline;
            padding: 0;
        }
    """)

    window = QWidget()
    layout = QVBoxLayout()
    window.setLayout(layout)

    file_drop_widget = FileDropWidget()
    layout.addWidget(file_drop_widget)

    window.setWindowTitle("Trascina un file")
    window.show()

    sys.exit(app.exec())
