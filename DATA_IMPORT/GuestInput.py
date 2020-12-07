from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import time


class GuestInput(QMainWindow):
    label = None

    def __init__(self, parent=None):
        super().__init__(parent)

        label_name = QLabel('ENTER YOUR NAME', self)
        label_name.setFont(QFont('Eras Bold ITC'))
        label_name.setStyleSheet('font: bold 50px; color: rgb(22, 23, 25);')
        label_name.move(340, 380)
        label_name.adjustSize()

        bg = QImage('PICTURE_FOR_PROJECT/bg_input_name.png')
        palette = QPalette()
        palette.setBrush(10, QBrush(bg))

        self.line = QLineEdit(self)
        self.line.move(400, 460)
        self.line.resize(400, 100)
        self.line.setMaxLength(10)
        self.line.setAlignment(Qt.AlignCenter)
        self.line.setFont(QFont('Eras Bold ITC'))
        self.line.textChanged.connect(self.text_upper)
        self.line.setStyleSheet('background-color: white;border-style: '
                                'outset;border-width: 2px;border-radius: '
                                '10px;border-color: rgb(228, 73, 68);font: bold 50px;'
                                'color: rgb(228, 73, 68);')
        self.line.returnPressed.connect(self.next_menu_game)

        self.backz = QPushButton('BACK', self)
        self.backz.move(500, 650)
        self.backz.resize(100, 50)
        self.backz.setFont(QFont('Eras Bold ITC'))
        self.backz.setStyleSheet('QPushButton{background-color: rgb(22, 23, 25);border-style: '
                                 'outset;border-width: 2px;border-radius: '
                                 '10px;border-color: rgb(228, 73, 68);font: bold 14px;'
                                 'color: rgb(228, 73, 68);min-width: 10em;padding: 6px;}'
                                 'QPushButton::pressed{background-color: white;}')
        self.backz.clicked.connect(self.back_menu_game)

        pic = QLabel(self)
        pixmap = QPixmap('PICTURE_FOR_PROJECT/light.png')
        pic.setPixmap(pixmap)
        pic.setScaledContents(True)
        pic.resize(100, 100)
        pic.move(300, 460)

        pic1 = QLabel(self)
        pixmap1 = QPixmap('PICTURE_FOR_PROJECT/car.png')
        pic1.setPixmap(pixmap1)
        pic1.setScaledContents(True)
        pic1.resize(100, 100)
        pic1.move(820, 460)

        self.setPalette(palette)
        self.resize(1200, 800)
        self.setWindowIcon(QIcon('PICTURE_FOR_PROJECT/logo.png'))
        self.setWindowTitle('TYPE RACING GAME')

    def back_menu_game(self):
        import START
        time.sleep(0.3)
        self.openz = START.StartWindow()
        self.openz.show()
        self.close()

    def text_upper(self, text):
        self.line.setText(text.upper())

    def labelz(self):
        type(self).label = QLabel(self)
        type(self).label.setText(self.line.text())
        type(self).label.move(400, 460)
        type(self).label.resize(400, 100)
        type(self).label.setAlignment(Qt.AlignCenter)
        type(self).label.setFont(QFont('Eras Bold ITC'))
        type(self).label.setStyleSheet('background-color: white;border-style: '
                                       'outset;border-width: 2px;border-radius: '
                                       '10px;border-color: red;font: bold 50px;'
                                       'color: red;')
        type(self).label.show()

    def str(self):
        return type(self).label.text()

    def next_menu_game(self):
        self.labelz()
        import DATA_IMPORT.EngineGame
        DATA_IMPORT.EngineGame.time.sleep(0.3)
        self.openz = DATA_IMPORT.EngineGame.EngineGame()
        self.openz.show()
        self.close()


def test():
    return GuestInput().str()
