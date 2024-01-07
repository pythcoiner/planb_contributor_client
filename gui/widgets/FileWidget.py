import os
import random
from pathlib import Path
import logging

from PySide6.QtCore import Signal
from PySide6.QtGui import Qt, QIcon
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QLineEdit, QPushButton


class FileWidget(QWidget):
    
    clicked_plus = Signal(str)
    clicked_minus = Signal(object)
    
    def __init__(self, button_text: str, file: str, label_width=100):
        QWidget.__init__(self)
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)
        
        self.id = random.randint(0, 2**16 - 1)
        
        self.button_text = button_text
        
        self.button = QPushButton(button_text)

        self.button.setFixedHeight(25)
        self.button.setFixedWidth(20)
        
        self.file = file
        
        self.file_label = QLabel(self.file)
        self.file_label.setFixedWidth(label_width)
        self.file_label.setFixedHeight(25)
        self.file_label.setStyleSheet("border: 1px solid black;")
        self.file_label.setAlignment(Qt.AlignCenter)
        
        self.spacer = QWidget()

        layout.addWidget(self.button)
        layout.addWidget(self.file_label)
        layout.addWidget(self.spacer)
        layout.setStretchFactor(self.spacer, 1)

        # --------------------------------------------
        
        # self.button.clicked.connect(self.on_clicked)

    def on_clicked(self, event):
        if self.button_text == '+':
            self.clicked_plus.emit(self.io)
        if self.button_text == '-':
            self.clicked_minus.emit(self.id)
            
    def on_update(self, debug=False):
        if debug:
            logging.info(f"[{self.__class__.__name__}][{self.io_type}{self.io}].on_update()")
        pass
    
    def on_button0_clicked(self):
        pass
    
    def on_button1_clicked(self):
        pass
        
    