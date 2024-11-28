import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget, QMessageBox, QPlainTextEdit
from PyQt6.QtCore import QSize

from version import VERSION


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(f"test project {VERSION}")

        self.run_btn = QPushButton("Run")
        self.run_btn.setMinimumSize(80, 50)
        self.run_btn.clicked.connect(self.on_run_clicked)
        self.stop_btn = QPushButton("Stop")
        self.stop_btn.setMinimumSize(80, 50)
        self.stop_btn.clicked.connect(self.on_stop_clicked)

        self.log_field = QPlainTextEdit()
        self.log_field.setMinimumSize(400, 200)

        self.grid_layout = QGridLayout()
        self.grid_layout.addWidget(self.run_btn, 0, 0)
        self.grid_layout.addWidget(self.stop_btn, 0, 1)
        self.grid_layout.addWidget(self.log_field, 1, 0, 6, 4)

        self.setLayout(self.grid_layout)
        widget = QWidget()
        widget.setLayout(self.grid_layout)
        self.setCentralWidget(widget)
        self.setMinimumSize(QSize(400, 300))

    def on_run_clicked(self):
        self.log_field.appendPlainText('Run button clicked')

    def on_stop_clicked(self):
        self.log_field.appendPlainText('Stop button clicked')

    def closeEvent(self, event):
        reply = QMessageBox.question(self,
                                     'Message',
                                     "Are you sure to quit?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
