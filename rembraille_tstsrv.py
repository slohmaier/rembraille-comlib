import os
import sys
import socket
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget, QGridLayout, QTextEdit, QLabel, QPushButton

class RemBrailleServer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RemBraille Server")
        self.show()

        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._gridLayout = QGridLayout(self._centralWidget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RemBrailleServer()
    sys.exit(app.exec())