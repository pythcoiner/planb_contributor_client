from PySide6.QtCore import Signal
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QCheckBox


class CheckUnit(QWidget):
    checked = Signal()
    unchecked = Signal()
    
    def __init__(self, label_text, label_width=None):
        QWidget.__init__(self)
    
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)
        self.check = QCheckBox()
        self.label = QLabel(label_text)
        
        if label_width:
            self.label.setFixedWidth(label_width)
        layout.addWidget(self.check)
        layout.addWidget(self.label)
        
        self.check.stateChanged.connect(self.on_clicked)
    
    def on_clicked(self, state):
        if state == 2:
            self.checked.emit()
        elif state == 0:
            self.unchecked.emit()
            
            
            