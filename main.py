#подключение библиотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QMessageBox, QRadioButton, QLabel)

def show_win():
    v_win = QMessageBox()
    v_win.setText('Верно! Вы выиграли!')
    v_win.exec_()
def show_lose():
    l_win = QMessageBox()
    l_win.setText('Нет, оказывается, это синий кит')
    l_win.exec_()
#-----------------------------------------------------------
#создание приложения и главного окна
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Викторина')
main_win.resize(400, 200)
#создание виджетов главного окна
question = QLabel('Какое животное в мире самое большое?')
answer1 = QRadioButton('Синий кит')
answer2 = QRadioButton('Касатка')
answer3 = QRadioButton('Слон')
answer4 = QRadioButton('Белый медведь')

#расположение виджетов по лэйаутам
layout_main = QVBoxLayout()
layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()
layoutH4 = QHBoxLayout()

layoutH1.addWidget(question, alignment = Qt.AlignCenter)
layoutH2.addWidget(answer1, alignment = Qt.AlignCenter)
layoutH2.addWidget(answer2, alignment = Qt.AlignCenter)
layoutH3.addWidget(answer3, alignment = Qt.AlignCenter)
layoutH3.addWidget(answer4, alignment = Qt.AlignCenter)



layout_main.addLayout(layoutH1)
layout_main.addLayout(layoutH2)
layout_main.addLayout(layoutH3)
layout_main.addLayout(layoutH4)
main_win.setLayout(layout_main)
#обработка нажатий на переключатели
answer1.clicked.connect(show_win)
answer3.clicked.connect(show_lose)
answer2.clicked.connect(show_lose)
answer4.clicked.connect(show_lose)

#отображение окна приложения 
main_win.show()
app.exec_()
