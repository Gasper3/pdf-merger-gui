from PyQt5.QtWidgets import QAction, QPushButton, QMainWindow, QListWidget, QFileDialog
from PyQt5.QtGui import QIcon
from pathlib import Path


class PDFMerger(QMainWindow):

    def __init__(self):
        super().__init__()

        self.file_list = QListWidget()
        self.init_ui()

    def init_ui(self):
        self.setCentralWidget(self.file_list)
        self.statusBar()

        menu_open_file = QAction(QIcon('open.png'), 'Open', self)
        menu_open_file.setShortcut('Ctrl+O')
        menu_open_file.setStatusTip('Open new Files')
        menu_open_file.triggered.connect(self.show_dialog)

        btn_merge_files = QPushButton("Merge Files", self)
        btn_merge_files.move(60, 64)
        btn_merge_files.clicked.connect(self.merge_files)

        menu = self.menuBar()
        menu = menu.addMenu('&File')
        menu.addAction(menu_open_file)

        self.setGeometry(300, 300, 550, 450)
        self.setWindowTitle('PDF Merger')
        self.show()

    def show_dialog(self):
        home_dir = str(Path.home())
        filenames = QFileDialog.getOpenFileNames(self, 'Open file', home_dir)

        if filenames[0]:
            self.file_list.insertItems(0, filenames[0])

    def merge_files(self):
        print("Merge files")
