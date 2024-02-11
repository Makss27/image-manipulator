from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QGroupBox,
    QRadioButton,
    QPushButton,
    QLineEdit,
    QLabel)
from PyQt5 import QtGui
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
import pywinstyles

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
window.setStyleSheet("background:yellow;border:2px dashed white")
window.setWindowTitle("Я не знаю, что здесь записать")

window.setWindowIcon(QtGui.QIcon('лол.png'))
pywinstyles.apply_style(window, 'native')

input_image = QLineEdit()
input_image.setStyleSheet("color:blue; border:2px dashed white; padding:5px; font-size:40px")
input_image.setPlaceholderText("Введите название изображения")
layout.addWidget(input_image)

window.setLayout(layout)
window.show()
app.exec_()


