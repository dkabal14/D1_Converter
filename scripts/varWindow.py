from PyQt6 import uic
from PyQt6.QtWidgets import QDialog

class VarWindow(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/varWindow.ui", self)