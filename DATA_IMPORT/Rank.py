from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import json, time


class Ranking(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.main_window()

    def main_window(self):
        background = QImage('PICTURE_FOR_PROJECT/bg_score.png')
        palette = QPalette()
        palette.setBrush(10, QBrush(background))

        with open("data_text.json", "r") as r_file:
            data = json.load(r_file)

        data1 = data[-1]
        name1 = data1[0]
        score1 = data1[1]
        self.label1 = QLabel(self)
        self.label1.setText(f'{name1}\t{score1}')
        self.label1.setFont(QFont('Eras Bold ITC'))
        self.label1.setStyleSheet('font: bold 30px;color: rgb(22, 23, 25);}')
        self.label1.move(430, 300)
        self.label1.adjustSize()

        data2 = data[-2]
        name2 = data2[0]
        score2 = data2[1]
        self.label2 = QLabel(self)
        self.label2.setText(f'{name2}\t{score2}')
        self.label2.setFont(QFont('Eras Bold ITC'))
        self.label2.setStyleSheet('font: bold 30px;color: rgb(22, 23, 25);}')
        self.label2.move(430, 400)
        self.label2.adjustSize()

        data3 = data[-3]
        name3 = data3[0]
        score3 = data3[1]
        self.label3 = QLabel(self)
        self.label3.setText(f'{name3}\t{score3}')
        self.label3.setFont(QFont('Eras Bold ITC'))
        self.label3.setStyleSheet('font: bold 30px;color: rgb(22, 23, 25);}')
        self.label3.move(430, 500)
        self.label3.adjustSize()

        data4 = data[-1]
        name4 = data4[0]
        score4 = data4[1]
        self.label4 = QLabel(self)
        self.label4.setText(f'{name4}\t{score4}')
        self.label4.setFont(QFont('Eras Bold ITC'))
        self.label4.setStyleSheet('font: bold 30px;color: rgb(22, 23, 25);}')
        self.label4.move(430, 600)
        self.label4.adjustSize()

        self.backz = QPushButton('BACK', self)
        self.backz.move(470, 700)
        self.backz.resize(100, 50)
        self.backz.setFont(QFont('Eras Bold ITC'))
        self.backz.setStyleSheet('QPushButton{background-color: rgb(22, 23, 25);border-style: '
                                 'outset;border-width: 2px;border-radius: '
                                 '10px;border-color: rgb(228, 73, 68);font: bold 20px;'
                                 'color: rgb(228, 73, 68);min-width: 10em;padding: 6px;}'
                                 'QPushButton::pressed{background-color: white;}')
        self.backz.clicked.connect(self.back_menu_game)

        self.setPalette(palette)
        self.resize(1200, 800)
        self.setWindowIcon(QIcon('PICTURE_FOR_PROJECT/logo.png'))
        self.setWindowTitle('TYPE RACING GAME')
        self.show()

    def back_menu_game(self):
        import START
        time.sleep(0.3)
        self.openz = START.StartWindow()
        self.openz.show()
        self.close()
