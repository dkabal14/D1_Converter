from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QMainWindow 
import sys

import varWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Carrega tela principal
        uic.loadUi("ui/mainWindow.ui", self)

        self.btn_vars.clicked.connect(self.open_var_window)


    def open_var_window(self):
        popup = varWindow.VarWindow()
        popup.exec() 
        
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())