#создай тут фоторедактор Easy Editor!
from PIL import Image, ImageFilter
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog , QApplication, QWidget, QPushButton, QInputDialog, QHBoxLayout, QVBoxLayout, QLabel, QTextEdit, QListWidget,QLineEdit
import os
import json
from PyQt5.QtGui import QPixmap
app=QApplication([])

#окно
main_win=QWidget()
#main_win.size(700,400)
main_win.setWindowTitle('Easy Editor')
#список папок
field_text = QListWidget()

#Buttons:
btn_dir=QPushButton()
btn_dir.setText("Папка")
image_win=QLabel()
image_win.setText("картинка")
btn_left=QPushButton()
btn_left.setText("Лево")
btn_right=QPushButton()
btn_right.setText("Право")
btn_mirror=QPushButton()
btn_mirror.setText("Зеркало")
btn_sharpness=QPushButton()
btn_sharpness.setText("Резкость")
btn_l=QPushButton()
btn_l.setText("Ч/Б")

#Лэйауты:
layout_4=QHBoxLayout()
layout_3=QVBoxLayout()
layout_2=QHBoxLayout()
layout_1=QVBoxLayout()

#Добавление одного лэйаута к другому:
layout_4.addLayout(layout_1)
layout_4.addLayout(layout_3)

#Добавление виджетов к лэйаутам:
layout_1.addWidget(btn_dir)
layout_1.addWidget(field_text)
layout_3.addWidget(image_win)
layout_2.addWidget(btn_left)
layout_2.addWidget(btn_right)
layout_2.addWidget(btn_mirror)
layout_2.addWidget(btn_sharpness)
layout_2.addWidget(btn_l)
#Добавление 2го лэйаута к 3му:
layout_3.addLayout(layout_2)

def open():
    try:
        original=Image.open(filename)
    except:
        print("Файл не найден!")
    original.show()
    
def do_left():
    left=original.transpote(original.ROTATE_90)
    left.show()
def do_right():
    right=left.transpote(left.ROTATE_90)
    right.show()
def do_cropped():
    box=(100,100,400,450)
    cropped=oroginal.crop(box)
    cropped.save("crop")
    cropped.show()


def filter(files,ext):
    res=[]
    for y in files:
        for z in ext:
            if y.endswith(z):
                res.append(y)
    return res

cur_dir=''

def show():
    global cur_dir
    cur_dir = QFileDialog.getExistingDirectory()
    files = os.listdir(cur_dir)
    ext=['bmp','jpg','png']
    res=filter(files,ext)
    for y in files:
        for z in files:
            if y.endswith(z):
                res.append(y)
    field_text.clear()
    for i in res:
        field_text.addItem(i)


class ImageProceccor():
    def __init__(self):
        self.image=None
        self.filename=None
        self.savedir="Mod/"

    def saveImage(self):
        path = os.path.join(cur_dir, self.savedir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)

    def do_bw(self):
        self.image = self.image.convert("L")
        self.saveImage()
        image_path=os.path.join(cur_dir,self.savedir,self.filename)
        self.showImage(image_path)

    def do_left():
        self.image=self.image.transpote(self.image.ROTATE_90)
        self.saveImage()
        image_path=os.path.join(cur_dir,self.savedir,self.filename)
        self.showImage(image_path)

    def loadImage(self,filename):
        self.filename=filename
        image_path=os.path.join(cur_dir, filename)
        self.image=Image.open(image_path)

    def showImage(self,path):
        image_win.hide()
        pixmapimage=QPixmap(path)
        w, h =image_win.width(), image_win.height()
        pixmapimage=pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        image_win.setPixmap(pixmapimage)
        image_win.show()

b=ImageProceccor()
def showim():
    if field_text.currentRow() >=0:
        filename=field_text.currentItem().text()
        b.loadImage(filename)
        path=os.path.join(cur_dir,b.filename)
        b.showImage(path)

btn_dir.clicked.connect(show)
#функционал кнопок:
btn_left.clicked.connect(b.do_left)
btn_l.clicked.connect(b.do_bw)
field_text.currentRowChanged.connect(showim)
main_win.setLayout(layout_4)
main_win.show()
app.exec()