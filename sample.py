import sys
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton, QFileDialog

class FileDialogApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.label = QLabel("Clicca qui per aprire il file dialog")
        layout.addWidget(self.label)

        # Collega il click del label al metodo per aprire il file dialog
        self.label.mousePressEvent = self.open_file_dialog

        self.setLayout(layout)

    def open_file_dialog(self, event):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        file_name, _ = QFileDialog.getOpenFileName(
            self, "Apri file", "", "CSV Files (*.csv);;Excel Files (*.xls *.xlsx);;Tutti i file (*)", options=options
        )

        if file_name:
            self.label.setText(file_name)

def main():
    app = QApplication(sys.argv)
    window = FileDialogApp()
    window.setGeometry(100, 100, 400, 200)  # Imposta le dimensioni della finestra
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
