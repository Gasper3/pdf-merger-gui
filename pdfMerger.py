import sys
from app.main import PDFMerger
from PyQt5.QtWidgets import QApplication


def main():
    app = QApplication(sys.argv)
    ex = PDFMerger()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
