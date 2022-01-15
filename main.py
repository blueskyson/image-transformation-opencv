import sys
import cv2
import numpy as np
import ast
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QLineEdit,
)


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(200, 200, 300, 400)
        self.setWindowTitle("Image Transformation")
        self.initUI()
        self.img = cv2.imread("sample.png")

    def initUI(self):
        button = [None] * 4
        button[0] = QPushButton("1. Resize", self)
        button[0].clicked.connect(self.push_resize_button)
        button[1] = QPushButton("2. Translation", self)
        button[1].clicked.connect(self.push_translation_button)
        button[2] = QPushButton("3. Rotation, Scaling", self)
        button[2].clicked.connect(self.push_rotation_button)
        button[3] = QPushButton("4. Shearing", self)
        button[3].clicked.connect(self.push_shearing_button)

        self.resize_txt = QLineEdit("256,256")
        self.xtrans_txt = QLineEdit("0")
        self.ytrans_txt = QLineEdit("60")
        self.angle_txt = QLineEdit("10")
        self.scale_txt = QLineEdit("0.5")
        self.windowsize_txt = QLineEdit("(400,300)")
        self.orig_pts_txt = QLineEdit("[[50,50],[200,50],[50,200]]")
        self.shearing_pts_txt = QLineEdit("[[10,100],[200,50],[100,250]]")

        vbox = QVBoxLayout()
        vbox.addWidget(QLabel("resize"))
        vbox.addWidget(self.resize_txt)
        vbox.addWidget(button[0])

        vbox.addWidget(QLabel("translation X:"))
        vbox.addWidget(self.xtrans_txt)
        vbox.addWidget(QLabel("translation Y:"))
        vbox.addWidget(self.ytrans_txt)
        vbox.addWidget(button[1])

        vbox.addWidget(QLabel("angle"))
        vbox.addWidget(self.angle_txt)
        vbox.addWidget(QLabel("scale"))
        vbox.addWidget(self.scale_txt)
        vbox.addWidget(QLabel("window size"))
        vbox.addWidget(self.windowsize_txt)
        vbox.addWidget(button[2])

        vbox.addWidget(QLabel("original points:"))
        vbox.addWidget(self.orig_pts_txt)
        vbox.addWidget(QLabel("shearing points:"))
        vbox.addWidget(self.shearing_pts_txt)
        vbox.addWidget(button[3])
        vbox.addStretch(1)
        self.setLayout(vbox)

    # ============================================================================
    # image processing funtions
    # ============================================================================

    # ============================================================================
    # button handling funtions
    # ============================================================================

    def push_resize_button(self):
        pass

    def push_translation_button(self):
        pass

    def push_rotation_button(self):
        pass

    def push_shearing_button(self):
        pass


def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
