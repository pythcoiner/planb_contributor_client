from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QComboBox, QLineEdit, QVBoxLayout, QScrollArea


class Stretch(QWidget):
    
    def __init__(self):
        QWidget.__init__(self)


class BaseWidget:
    
    def __init__(self, parent=None):
        self.parent = parent
        if self.parent:
            if hasattr(parent, 'config'):
                self.config = parent.config
            
            if hasattr(parent, 'root'):
                self.root = parent.root()
                
        self.widget = QWidget()
        self.layout = QVBoxLayout()
        self.widget.setLayout(self.layout)
        self.widgets = []
    
    def addWidget(self, widget):
        self.layout.addWidget(widget)
        self.widgets.append(widget)  # Add the widget to self.widgets
    
    def addRow(self, widgets: [], stretch=False):
        h_layout = QHBoxLayout()
        h_layout.setContentsMargins(0, 0, 0, 0)
        h_layout.setSpacing(2)
        
        max_height = 0
        total_width = 0  # Keep track of the total width of all preceding widgets
        
        for widget in widgets:
            if isinstance(widget, tuple):
                # Handle the special case where we have (widget, x_coordinate)
                actual_widget, x_coordinate = widget
                spacer_width = x_coordinate - total_width  # Calculate required spacer width
                if spacer_width > 0:
                    spacer = QWidget()
                    spacer.setFixedWidth(spacer_width)
                    h_layout.addWidget(spacer)
                    total_width += spacer_width
                if actual_widget:
                    h_layout.addWidget(actual_widget)
                    max_height = max(max_height, actual_widget.sizeHint().height())
                    total_width += actual_widget.sizeHint().width()  # Update total width
            
            elif isinstance(widget, int):
                h_layout.addStretch(widget)
            
            elif widget:
                h_layout.addWidget(widget)
                max_height = max(max_height, widget.sizeHint().height())
                total_width += widget.sizeHint().width()  # Update total width
            else:
                h_layout.addStretch(1)
        
        h_widget = QWidget()
        h_widget.setLayout(h_layout)
        # h_widget.setStyleSheet('QWidget {border-radius: 0px;}')
        h_widget.setFixedHeight(max_height + 2)
        self.addWidget(h_widget)
        if stretch:
            self.layout.setStretchFactor(h_widget, 1)
        return h_widget
    
    def addScrollArea(self):
        scroll_area = QScrollArea(self.widget)
        scroll_area.setWidgetResizable(True)
        
        content_base_widget = BaseWidget(self.widget)
        scroll_area.setWidget(content_base_widget.widget)
        
        self.addWidget(scroll_area)
        return content_base_widget

    def addStretch(self, factor=1):
        self.spacer = Stretch()
        self.addWidget(self.spacer)
        self.layout.setStretchFactor(self.spacer, factor)
        
    def removeStretch(self):
        last_item = self.layout.itemAt(self.layout.count() - 1)
        if last_item:
            widget = last_item.widget()
            if widget and widget.__class__.__name__ == 'Stretch':
                self.layout.removeWidget(widget)
                widget.deleteLater()
                
    def addItem(self, item):
        self.layout.addItem(item)
    
    def comboLine(self, label, label_width=None, content=['', ''], combo_width=None, add=True):
        label = QLabel(label)
        if label_width:
            label.setFixedWidth(label_width)
        combo = QComboBox()
        combo.addItems(content)
        if combo_width:
            combo.setFixedWidth(combo_width)
        if add:
            row = self.addRow([label, combo, None])
            return row, combo
        else:
            return [label, combo]
    
    def inputLine(self, label, label_width=None, input_width=None, add=True):
        # Wallet file
        label = QLabel(label)
        if label_width:
            label.setFixedWidth(label_width)
        _input = QLineEdit()
        if input_width:
            _input.setFixedWidth(input_width)
        if add:
            row = self.addRow([label, _input, None])
            return row, _input
        else:
            return [label, _input]
