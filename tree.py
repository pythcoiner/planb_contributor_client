import sys
from PySide6.QtWidgets import QApplication, QTreeView
from PySide6.QtGui import QStandardItemModel, QStandardItem, QIcon
from PySide6.QtCore import Qt


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


app = QApplication(sys.argv)

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
treeView.expandAll()  # Expand all nodes for visibility

# Show the tree view
treeView.show()
sys.exit(app.exec())
