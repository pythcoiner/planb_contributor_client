import sys
import logging
import time

from PySide6.QtCore import QObject, QCoreApplication, Signal, QTimer
from PySide6.QtGui import QPalette, QColor, Qt
from PySide6.QtWidgets import QApplication

from gui.GUI import BaseWindow


if __name__ == '__main__':
    
    app = QApplication([])
    
    # HMI
    app.setStyleSheet("""
        """)  # dont delete, i dont know why...
    # Now use a palette to switch to dark colors:
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.black)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)
    window = BaseWindow()
    window.show()
    exit_code = app.exec()
    
    sys.exit(exit_code)
    
    