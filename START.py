from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys, time


class StartWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.main_window()

    def main_window(self):
        background = QImage('PICTURE_FOR_PROJECT/bg_start.png')
        palette = QPalette()
        palette.setBrush(10, QBrush(background))

        btn_start = QPushButton('START', self)
        btn_start.setFont(QFont('Eras Bold ITC'))
        btn_start.setGeometry(480, 450, 200, 50)
        btn_start.setStyleSheet('QPushButton{background-color: rgb(22, 23, 25);border-style: '
                                'outset;border-width: 2px;border-radius: '
                                '10px;border-color: rgb(228, 73, 68);font: bold 20px;'
                                'color: rgb(228, 73, 68);min-width: 10em;padding: 6px;}'
                                'QPushButton::pressed{background-color: white;}')
        btn_start.clicked.connect(self.next_guest_input)

        btn_rank = QPushButton('SCORE BOARD', self)
        btn_rank.setFont(QFont('Eras Bold ITC'))
        btn_rank.setGeometry(480, 550, 200, 50)
        btn_rank.setStyleSheet('QPushButton{background-color: rgb(22, 23, 25);border-style: '
                               'outset;border-width: 2px;border-radius: '
                               '10px;border-color: rgb(228, 73, 68);font: bold 20px;'
                               'color: rgb(228, 73, 68);min-width: 10em;padding: 6px;}'
                               'QPushButton::pressed{background-color: white;}')
        btn_rank.clicked.connect(self.rank_guest_input)

        btn_quit = QPushButton('QUIT', self)
        btn_quit.setFont(QFont('Eras Bold ITC'))
        btn_quit.setGeometry(480, 650, 200, 50)
        btn_quit.setStyleSheet('QPushButton{background-color: rgb(22, 23, 25);border-style: '
                               'outset;border-width: 2px;border-radius: '
                               '10px;border-color: rgb(228, 73, 68);font: bold 20px;'
                               'color: rgb(228, 73, 68);min-width: 10em;padding: 6px;}'
                               'QPushButton::pressed{background-color: white;}')
        btn_quit.clicked.connect(QApplication.instance().quit)

        self.setPalette(palette)
        self.resize(1200, 800)
        self.setWindowIcon(QIcon('PICTURE_FOR_PROJECT/logo.png'))
        self.setWindowTitle('TYPE RACING GAME')
        self.show()

    def next_guest_input(self):
        import DATA_IMPORT.GuestInput
        time.sleep(0.3)
        self.openz = DATA_IMPORT.GuestInput.GuestInput()
        self.openz.show()
        self.close()

    def rank_guest_input(self):
        import DATA_IMPORT.Rank
        time.sleep(0.3)
        self.openz = DATA_IMPORT.Rank.Ranking()
        self.openz.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window_first = StartWindow()
    sys.exit(app.exec_())
