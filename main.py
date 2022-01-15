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
        self.image = cv2.imread("sample.png")

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

        self.resize_txt = QLineEdit("(256,256)")
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

    def resize(self, img):
        img_size = ast.literal_eval(self.resize_txt.text())
        return cv2.resize(img, tuple(img_size))

    def translation(self, img):
        tx = int(self.xtrans_txt.text())
        ty = int(self.ytrans_txt.text())
        width = img.shape[1] + tx
        height = img.shape[0] + ty

        # translation matrix
        M = np.float32([[1, 0, tx], [0, 1, ty]])
        return cv2.warpAffine(img, M, (width, height))

    def rotation(self, img):
        windowsize = ast.literal_eval(self.windowsize_txt.text())
        imgsize = ast.literal_eval(self.resize_txt.text())
        tx = int(self.xtrans_txt.text())
        ty = int(self.ytrans_txt.text())
        center = (imgsize[0] / 2 + tx, imgsize[1] / 2 + ty)
        angle = int(self.angle_txt.text())
        scale = float(self.scale_txt.text())

        M = cv2.getRotationMatrix2D(center, angle, scale)
        return cv2.warpAffine(img, M, tuple(windowsize))

    def affine_transformation(self, img):
        imgsize = (img.shape[1], img.shape[0])

        old_loc = ast.literal_eval(self.orig_pts_txt.text())
        old_loc = np.float32(old_loc)
        new_loc = ast.literal_eval(self.shearing_pts_txt.text())
        new_loc = np.float32(new_loc)
        M = cv2.getAffineTransform(old_loc, new_loc)
        return cv2.warpAffine(img, M, imgsize)

    # ============================================================================
    # button handling funtions
    # ============================================================================

    def push_resize_button(self):
        img = self.image.copy()
        cv2.imshow("Resize", self.resize(img))

    def push_translation_button(self):
        img = self.image.copy()
        img = self.resize(img)
        cv2.imshow("Translation", self.translation(img))

    def push_rotation_button(self):
        img = self.image.copy()
        img = self.resize(img)
        cv2.imshow("Rotation, Scaling", self.rotation(img))

    def push_shearing_button(self):
        img = self.image.copy()
        img = self.resize(img)
        img = self.rotation(img)
        cv2.imshow("Shearing", self.affine_transformation(img))


def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
