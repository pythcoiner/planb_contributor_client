import logging

from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget, QFrame, QLabel, QComboBox, QLineEdit

from gui.widgets.BaseWidget import BaseWidget


class BaseScreen(BaseWidget):
    
    def __init__(self, parent=None):
        BaseWidget.__init__(self, parent)
        self.parent = parent
                
        self.widget = QFrame()
        self.layout = QHBoxLayout()
        self.widget.setLayout(self.layout)
        self.widgets = []
    
    def load_in(self, destination: QFrame):
        """Load the Screen into a destination QFrame."""
        # Clear destination layout
        logging.info(f"[{self.__class__.__name__}]load_in()")
        
        if destination.layout() is not None:
            while destination.layout().count():
                item = destination.layout().takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)  # This removes widget from layout without deleting it
            # Clear all layouts
            while destination.layout().count():
                destination.layout().takeAt(0)
        else:
            destination.setLayout(QVBoxLayout())
        
        # Add widgets to the new layout
        for widget in self.widgets:
            destination.layout().addWidget(widget)
    
