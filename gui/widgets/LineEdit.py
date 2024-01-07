import PySide6
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QLineEdit


class LineEdit(QLineEdit):
    
    focusLost = Signal()
    
    def __init__(self):
        QLineEdit.__init__(self)
    
    def focusOutEvent(self, event):
        self.focusLost.emit()
        super().focusOutEvent(event)
        
        