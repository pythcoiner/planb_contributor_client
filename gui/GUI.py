import sys

from PySide6.QtCore import QSize
from PySide6.QtGui import Qt, QPalette, QColor
from PySide6.QtWidgets import QMainWindow, QWidget, QStatusBar, QLabel, QHBoxLayout, QFrame, QVBoxLayout, QPushButton, \
    QApplication

from gui.screens.CoursesScreen import CoursesScreen


class BaseWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PlanB Contributor Client')


        # Set minimum size of the window
        self.setMinimumSize(QSize(1280, 800))
        
        self.menu_height = 50
        self.button_width = 150
        self.button_spacing = 50
        
        # Footer
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.footer_label = QLabel("PlanB")
        self.status_bar.addWidget(self.footer_label)
        
        # Set up the main widget and its layout
        self.main_widget = QWidget()
        self.main_layout = QVBoxLayout()
        self.main_widget.setLayout(self.main_layout)

        # Top menu
        self.menu_frame = QFrame(self.main_widget)
        self.menu_layout = QHBoxLayout()
        self.menu_frame.setLayout(self.menu_layout)
        # self.menu_frame.setStyleSheet("background-color: red;")
        
        # Main frame
        self.main_frame = QFrame(self.main_widget)
        # self.main_frame.setStyleSheet("background-color: pink;")
        
        # Add frames to main layout with appropriate sizing
        self.main_layout.addWidget(self.menu_frame, 1, Qt.AlignLeft)
        self.main_layout.addWidget(self.main_frame, 1)
        
        # menu Buttons
        self.btn_courses = QPushButton('Courses', self.menu_frame)
        self.btn_courses.setCheckable(True)
        self.btn_courses.clicked.connect(self.on_courses_clicked)
        self.menu_layout.addWidget(self.btn_courses)
        
        self.btn_resourses = QPushButton('Resources', self.menu_frame)
        self.btn_resourses.setCheckable(True)
        self.btn_resourses.clicked.connect(self.on_resources_clicked)
        self.menu_layout.addWidget(self.btn_resourses)
        
        self.btn_tutorial = QPushButton('Tutorials', self.menu_frame)
        self.btn_tutorial.setCheckable(True)
        self.btn_tutorial.clicked.connect(self.on_tutorial_clicked)
        self.menu_layout.addWidget(self.btn_tutorial)
        
        self.btn_quizz = QPushButton('Quizz', self.menu_frame)
        self.btn_quizz.setCheckable(True)
        self.btn_quizz.clicked.connect(self.on_quizz_clicked)
        self.menu_layout.addWidget(self.btn_quizz)
        
        # Set main widget of the window
        self.setCentralWidget(self.main_widget)
        
        self.courses_screen = CoursesScreen(self)
        
        self.courses_screen.load_in(self.main_frame)
        
        self.do_resize()
        
        self.on_courses_clicked()
        
    def uncheck_all_buttons(self, _except: str = None):
        btn_count = self.menu_layout.count()
        for i in range(btn_count):
            btn: QPushButton = self.menu_layout.itemAt(i).widget()
            if btn.text() != _except:
                btn.setChecked(False)
            else:
                btn.setChecked(True)
        
    def resizeEvent(self, event) -> None:
        self.do_resize()
    
    def do_resize(self):
        main_height = self.size().height() - self.menu_height
        
        main_frame_height = main_height - self.menu_height - 20
        
        self.menu_frame.setFixedHeight(self.menu_height)
        self.main_frame.setFixedHeight(main_frame_height)
        
        self.resize_menu_buttons()
        # self.alarm_screen.do_resize()
        
    def resize_menu_buttons(self):
        width = self.button_width
        height = self.menu_height - 15
        btn_count = self.menu_layout.count()
        for i in range(btn_count):
            btn = self.menu_layout.itemAt(i).widget()
            if isinstance(btn, QPushButton):
                btn.setMinimumHeight(height)
                btn.setMaximumHeight(height)
                
                btn.setMinimumWidth(width)
                btn.setMaximumWidth(width)
        
    def on_courses_clicked(self):
        self.uncheck_all_buttons(_except='Courses')
        self.courses_screen.load_in(self.main_frame)
    
    def on_resources_clicked(self):
        self.uncheck_all_buttons(_except='Resources')
        # self.io_screen.load_in(self.main_frame)
    
    def on_tutorial_clicked(self):
        self.uncheck_all_buttons(_except='Tutorials')
        # self.grafcet_screen.load_in(self.main_frame)
    
    def on_quizz_clicked(self):
        self.uncheck_all_buttons(_except='Quizz')
        # self.alarm_screen.load_in(self.main_frame)
        

if __name__ == "__main__":
    app = QApplication([])
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
    sys.exit(app.exec())
    
    