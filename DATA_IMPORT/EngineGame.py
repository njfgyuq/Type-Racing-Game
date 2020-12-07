from DATA_WORD.WORD_RANDOM import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random, time, json


class EngineGame(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.count_value = 30
        self.score_value = 0
        self.start_Flag = False
        self.word_list = store()

        bg = QImage('PICTURE_FOR_PROJECT/bg_landscape.png')
        self.palette = QPalette()
        self.palette.setBrush(10, QBrush(bg))
        self.setPalette(self.palette)

        self.resize(1200, 800)
        self.setWindowIcon(QIcon('PICTURE_FOR_PROJECT/logo.png'))
        self.setWindowTitle('TYPE RACING GAME')

        self.ui_start()

    def ui_start(self):

        self.backz = QPushButton('BACK', self)
        self.backz.move(120, 600)
        self.backz.resize(100, 50)
        self.backz.setFont(QFont('Eras Bold ITC'))
        self.backz.setStyleSheet('QPushButton{background-color: rgb(22, 23, 25);border-style: '
                                 'outset;border-width: 2px;border-radius: '
                                 '10px;border-color: rgb(228, 73, 68);font: bold 14px;'
                                 'color: rgb(228, 73, 68);min-width: 10em;padding: 6px;}'
                                 'QPushButton::pressed{background-color: white;}')
        self.backz.clicked.connect(self.back_menu_game)

        self.nextz = QPushButton('FINISH', self)
        self.nextz.move(900, 600)
        self.nextz.resize(100, 50)
        self.nextz.setFont(QFont('Eras Bold ITC'))
        self.nextz.setStyleSheet('QPushButton{background-color: rgb(22, 23, 25);border-style: '
                                 'outset;border-width: 2px;border-radius: '
                                 '10px;border-color: rgb(228, 73, 68);font: bold 14px;'
                                 'color: rgb(228, 73, 68);min-width: 10em;padding: 6px;}'
                                 'QPushButton::pressed{background-color: white;}')
        self.nextz.clicked.connect(self.next_menu_game)

        self.input_text = QLineEdit(self)
        self.input_text.move(400, 450)
        self.input_text.resize(400, 100)
        self.input_text.setAlignment(Qt.AlignCenter)
        self.input_text.setFont(QFont('Eras Bold ITC'))
        self.input_text.setStyleSheet('background-color: white;border-style: '
                                      'outset;border-width: 2px;border-radius: '
                                      '10px;border-color: rgb(228, 73, 68);font: bold 50px;'
                                      'color: rgb(228, 73, 68);')
        self.input_text.setDisabled(True)
        self.input_text.returnPressed.connect(self.input_action)

        self.start = QPushButton("Start", self)
        self.start.move(413, 585)
        self.start.resize(50, 80)
        self.start.setFont(QFont('Eras Bold ITC'))
        self.start.setStyleSheet('QPushButton{background-color: rgb(22, 23, 25);border-style: '
                                 'outset;border-width: 2px;border-radius: '
                                 '10px;border-color: rgb(228, 73, 68);font: bold 30px;'
                                 'color: rgb(228, 73, 68);min-width: 10em;padding: 6px;}'
                                 'QPushButton::pressed{background-color: white;}')
        self.start.clicked.connect(self.start_action)

        self.word = QLabel("Word", self)
        self.word.setFont(QFont('Eras Bold ITC'))
        self.word.setAlignment(Qt.AlignCenter)
        self.word.resize(400, 100)
        self.word.move(230, 320)
        self.word.setStyleSheet('background-color: rgb(22, 23, 25);border-style: '
                                'outset;border-width: 2px;border-radius: '
                                '10px;border-color: rgb(228, 73, 68);font: bold 60px;'
                                'color: rgb(228, 73, 68);min-width: 10em;padding: 6px;}')

        self.score = QLabel("SCORE", self)
        self.score.move(250, 230)
        self.score.resize(100, 50)
        self.score.setAlignment(Qt.AlignCenter)
        self.score.setFont(QFont('Eras Bold ITC', 20))
        self.score.setStyleSheet('font: bold 60px; color: rgb(22, 23, 25);min-width: 10em;}')

        self.count = QLabel("TIME", self)
        self.count.move(250, 120)
        self.count.resize(300, 100)
        self.count.setAlignment(Qt.AlignCenter)
        self.count.setFont(QFont('Eras Bold ITC', 20))
        self.count.setStyleSheet('font: bold 60px; color: rgb(22, 23, 25);min-width: 10em;}')

        timer = QTimer(self)
        timer.timeout.connect(self.show_time)
        timer.start(1000)

    def save_data(self):
        import DATA_IMPORT.GuestInput as GuestInput
        lst = []
        text = GuestInput.test()
        score = self.score.text()
        data = text, score
        try:
            with open("data_text.json", "r") as r_file:
                read = json.load(r_file)
                for data_text in read:
                    lst.append(data_text)
        except FileNotFoundError:
            pass

        with open('data_text.json', 'w') as file:
            lst.append(data)
            json.dump(lst, file)

    def show_time(self):
        if self.start_Flag:

            self.count.setText(str(self.count_value))

            if self.count_value == 1:
                self.start_Flag = False
                self.input_text.setDisabled(True)

            self.count_value -= 1
            self.count.setText("TIME : " + str(self.count_value))

    def start_action(self):
        self.start_Flag = True
        # Reset
        self.score.setText("Score : 0")
        self.score_value = 0
        self.count_value = 30
        # Reset
        self.count_value = 30

        self.input_text.clear()
        self.input_text.setEnabled(True)

        self.random_word = random.choice(self.word_list)
        self.random_word.lower()

        self.word.setText(self.random_word)

        self.start.close()

    def input_action(self):
        text = self.input_text.text()
        text.lower()

        if text == self.random_word:
            self.input_text.clear()
            self.score_value += 1
            self.score.setText("SCORE : " + str(self.score_value))

            self.random_word = random.choice(self.word_list)
            self.random_word.lower()

            self.word.setText(self.random_word)

    def next_menu_game(self):
        import START
        import DATA_IMPORT.GuestInput as GuestInput
        lst = []
        text = GuestInput.test()
        score = self.score.text()
        data = text, score
        try:
            with open("data_text.json", "r") as r_file:
                read = json.load(r_file)
                for data_text in read:
                    lst.append(data_text)
        except FileNotFoundError:
            pass

        with open('data_text.json', 'w') as file:
            lst.append(data)
            json.dump(lst, file)

        time.sleep(0.3)
        self.openz = START.StartWindow()
        self.openz.show()
        self.close()

    def back_menu_game(self):
        import DATA_IMPORT.GuestInput
        time.sleep(0.3)
        self.openz = DATA_IMPORT.GuestInput.GuestInput()
        self.openz.show()
        self.close()
