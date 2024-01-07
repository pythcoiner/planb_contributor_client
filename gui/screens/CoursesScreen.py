import logging
import threading

from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QIcon, QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QWidget, QSizePolicy, QTreeView

from gui.screens.BaseScreen import BaseScreen
from gui.widgets.BaseWidget import BaseWidget
from gui.widgets.FileWidget import FileWidget


def create_item(text, icon='gui/widgets/icon/database.png'):
    item = QStandardItem(text)
    item.setIcon(QIcon(icon))  # Replace with path to your icon
    return item


def create_course(text):
    return create_item(text, 'gui/widgets/icon/book.png')


def create_metadata(text):
    return create_item(text, 'gui/widgets/icon/information-frame.png')


def create_section(text):
    return create_item(text, 'gui/widgets/icon/blue-folder.png')


def create_chapter(text):
    return create_item(text, 'gui/widgets/icon/book-open-text.png')


class CoursesScreen(BaseScreen):
    
    def __init__(self, parent=None):
        BaseScreen.__init__(self, parent)
       
        # Main QWidget to contain both self.columns
        self.main_widget = QWidget()
        # self.main_widget.setStyleSheet("background-color: red;")
        main_horizontal_layout = QHBoxLayout(self.main_widget)

        # Column 1 => Courses
        self.column_1 = BaseWidget()
        # self.column_1.widget.setStyleSheet("background-color: red;")
        self.column_1.addRow([None, QLabel("Courses"), None])
        self.column1_scroll_area = self.column_1.addScrollArea()
        
        # Column 2 => Course content
        self.column_2 = BaseWidget()
        self.column_2.addRow([None, QLabel("Content"), None])
        self.column2_scroll_area = self.column_2.addScrollArea()

        # Column 3 => Assets
        self.column_3 = BaseWidget()
        self.column_3.addRow([None, QLabel("Assets"), None])
        self.column3_scroll_area = self.column_3.addScrollArea()
        
        # Add BaseWidgets to the self.main_widget layout
        main_horizontal_layout.addWidget(self.column_1.widget, 20)
        main_horizontal_layout.addWidget(self.column_2.widget, 65)
        main_horizontal_layout.addWidget(self.column_3.widget, 15)
        
        # Add the self.main_widget to the Screen
        self.addWidget(self.main_widget)
        
        # Fill courses column
        
        # Create the model
        model = QStandardItemModel()
        rootNode = model.invisibleRootItem()
        
        # Create tree items
        btc101 = create_course('btc101')
        attributes = create_metadata('attributes')
        section0 = create_section('section0')
        chapter_0 = create_chapter('chapter_0')
        section1 = create_section('section1')
        chapter_1 = create_chapter('chapter_1')
        chapter_2 = create_chapter('chapter_2')
        chapter_3 = create_chapter('chapter_3')
        section2 = create_section('section2')
        chapter_4 = create_chapter('chapter_4')
        chapter_5 = create_chapter('chapter_5')
        chapter_6 = create_chapter('chapter_6')
        
        # Build the tree
        btc101.appendRow(attributes)
        section0.appendRow(chapter_0)
        section1.appendRows([chapter_1, chapter_2, chapter_3])
        section2.appendRows([chapter_4, chapter_5, chapter_6])
        btc101.appendRows([section0, section1, section2])
        rootNode.appendRow(btc101)
        
        # Create the tree view
        treeView = QTreeView()
        treeView.setModel(model)
        treeView.setHeaderHidden(True)
        # treeView.expandAll()  # Expand all nodes for visibility
        
        self.column1_scroll_area.addWidget(treeView)
        
        # Fill assets column
        assets = [
            '0.png',
            '1.png',
            '2.png',
            '3.png',
            '4.png',
            '0.png',
            '1.png',
            '2.png',
            '3.png',
            '4.png',
            '0.png',
            '1.png',
            '2.png',
            '3.png',
            '4.png',
            '0.png',
            '1.png',
            '2.png',
            '3.png',
            '4.png',
            '0.png',
            '1.png',
            '2.png',
            '3.png',
            '4.png',
            '0.png',
            '1.png',
            '2.png',
        ]
        
        for i in assets:
            btn = QPushButton(i)
            btn.setFixedWidth(75)
            
            del_button = QPushButton()
            del_button.setIcon(QIcon('gui/widgets/icon/cross.png'))
            
            copy_button = QPushButton()
            copy_button.setIcon(QIcon('gui/widgets/icon/blue-document-copy.png'))
            
            self.column3_scroll_area.addRow([None, del_button, btn, copy_button, None])
        
        btn_plus = QPushButton()
        btn_plus.setFixedWidth(25)
        btn_plus.setIcon(QIcon('gui/widgets/icon/plus.png'))
        
        btn_add_course = QPushButton('Add asset')
        btn_add_course.setFixedWidth(110)
        self.column3_scroll_area.addRow([None, btn_plus, btn_add_course, None])
        
        self.column3_scroll_area.addStretch()
    

        
    