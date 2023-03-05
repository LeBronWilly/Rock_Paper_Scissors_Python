# -*- coding: utf-8 -*-
"""
Created on 09/24, 2022
@author: Willy Fang

"""

# https://www.w3schools.com/python/ref_random_choice.asp
# https://www.jb51.net/article/206117.htm
# https://www.796t.com/article.php?id=299323
# https://walkonnet.com/archives/18139
# https://rk.edu.pl/en/qgraphicsview-and-qgraphicsscene/
# https://steam.oxxostudio.tw/category/python/pyqt5/qgraphicsview.html
# https://stackoverflow.com/questions/28536306/inserting-an-image-in-gui-using-qt-designer/42776478#42776478

from UI_V01 import *
import numpy as np
from PySide2 import QtGui, QtWidgets
import urllib.request

random_list = ["Rock", "Paper", "Scissors"]


class AppWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Rock_Paper_Scissors()
        self.ui.setupUi(self)
        self.rock_img = None
        self.paper_img = None
        self.scissors_img = None
        self.window_img = None
        self.setup_control()
        self.show()

    def setup_control(self):
        self.ui.Rock_Button.clicked.connect(self.Rock_Button_clicked)
        self.ui.Paper_Button.clicked.connect(self.Paper_Button_clicked)
        self.ui.Scissors_Button.clicked.connect(self.Scissors_Button_clicked)
        # Rock
        self.rock_img = QPixmap()
        url1 = 'https://raw.githubusercontent.com/LeBronWilly/Rock_Paper_Scissors_Python/main/Rock.png'
        img_data1 = urllib.request.urlopen(url1).read()
        self.rock_img.loadFromData(img_data1)
        self.rock_img = self.rock_img.scaled(100, 100)
        # Paper
        self.paper_img = QPixmap()
        url2 = 'https://raw.githubusercontent.com/LeBronWilly/Rock_Paper_Scissors_Python/main/Paper.png'
        img_data2 = urllib.request.urlopen(url2).read()
        self.paper_img.loadFromData(img_data2)
        self.paper_img = self.paper_img.scaled(75, 75)
        # Scissors
        self.scissors_img = QPixmap()
        url3 = 'https://raw.githubusercontent.com/LeBronWilly/Rock_Paper_Scissors_Python/main/Scissors.png'
        img_data3 = urllib.request.urlopen(url3).read()
        self.scissors_img.loadFromData(img_data3)
        self.scissors_img = self.scissors_img.scaled(100, 100)
        # WindowIcon
        self.window_img = QPixmap()
        url = 'https://raw.githubusercontent.com/LeBronWilly/Rock_Paper_Scissors_Python/main/Rock_Paper_Scissors.png'
        img_data = urllib.request.urlopen(url).read()
        self.window_img.loadFromData(img_data)
        self.window_img = self.window_img.scaled(75, 75)
        self.setWindowIcon(QIcon(self.window_img))

    def Rock_Button_clicked(self):
        # self.ui.rock_img = QtGui.QPixmap('Rock.png').scaled(100, 100)
        you_scene = QtWidgets.QGraphicsScene()
        you_scene.addPixmap(self.rock_img)
        self.ui.You_Image.setScene(you_scene)

        opponent_scene = QtWidgets.QGraphicsScene()
        opponent_result = np.random.choice(random_list)
        if opponent_result == "Rock":
            opponent_scene.addPixmap(self.rock_img)
            self.ui.Opponent_Image.setScene(opponent_scene)
            self.ui.Deuce_Count.setText(str(int(self.ui.Deuce_Count.toPlainText()) + 1))
            self.ui.Deuce_Count.setAlignment(Qt.AlignRight)
            self.ui.Game_Result.setText("Deuce!")
            self.ui.Game_Result.setAlignment(Qt.AlignCenter)
        elif opponent_result == "Paper":
            # self.ui.paper_img = QtGui.QPixmap('Paper.png').scaled(75, 75)
            opponent_scene.addPixmap(self.paper_img)
            self.ui.Opponent_Image.setScene(opponent_scene)
            self.ui.Loss_Count.setText(str(int(self.ui.Loss_Count.toPlainText()) + 1))
            self.ui.Loss_Count.setAlignment(Qt.AlignRight)
            self.ui.Game_Result.setText("You Lose :<")
            self.ui.Game_Result.setAlignment(Qt.AlignCenter)
        elif opponent_result == "Scissors":
            # self.ui.scissors_img = QtGui.QPixmap('Scissors.png').scaled(100, 100)
            opponent_scene.addPixmap(self.scissors_img)
            self.ui.Opponent_Image.setScene(opponent_scene)
            self.ui.Win_Count.setText(str(int(self.ui.Win_Count.toPlainText()) + 1))
            self.ui.Win_Count.setAlignment(Qt.AlignRight)
            self.ui.Game_Result.setText("You Win :>")
            self.ui.Game_Result.setAlignment(Qt.AlignCenter)
        pass

    def Paper_Button_clicked(self):
        # self.ui.paper_img = QtGui.QPixmap('Paper.png').scaled(75, 75)
        you_scene = QtWidgets.QGraphicsScene()
        you_scene.addPixmap(self.paper_img)
        self.ui.You_Image.setScene(you_scene)

        opponent_scene = QtWidgets.QGraphicsScene()
        opponent_result = np.random.choice(random_list)
        if opponent_result == "Rock":
            # self.ui.rock_img = QtGui.QPixmap('Rock.png').scaled(100, 100)
            opponent_scene.addPixmap(self.rock_img)
            self.ui.Opponent_Image.setScene(opponent_scene)
            self.ui.Win_Count.setText(str(int(self.ui.Win_Count.toPlainText()) + 1))
            self.ui.Win_Count.setAlignment(Qt.AlignRight)
            self.ui.Game_Result.setText("You Win :>")
            self.ui.Game_Result.setAlignment(Qt.AlignCenter)
        elif opponent_result == "Paper":
            opponent_scene.addPixmap(self.paper_img)
            self.ui.Opponent_Image.setScene(opponent_scene)
            self.ui.Deuce_Count.setText(str(int(self.ui.Deuce_Count.toPlainText()) + 1))
            self.ui.Deuce_Count.setAlignment(Qt.AlignRight)
            self.ui.Game_Result.setText("Deuce!")
            self.ui.Game_Result.setAlignment(Qt.AlignCenter)
        elif opponent_result == "Scissors":
            # self.ui.scissors_img = QtGui.QPixmap('Scissors.png').scaled(100, 100)
            opponent_scene.addPixmap(self.scissors_img)
            self.ui.Opponent_Image.setScene(opponent_scene)
            self.ui.Loss_Count.setText(str(int(self.ui.Loss_Count.toPlainText()) + 1))
            self.ui.Loss_Count.setAlignment(Qt.AlignRight)
            self.ui.Game_Result.setText("You Lose :<")
            self.ui.Game_Result.setAlignment(Qt.AlignCenter)
        pass

    def Scissors_Button_clicked(self):
        # self.ui.scissors_img = QtGui.QPixmap('Scissors.png').scaled(100, 100)
        you_scene = QtWidgets.QGraphicsScene()
        you_scene.addPixmap(self.scissors_img)
        self.ui.You_Image.setScene(you_scene)

        opponent_scene = QtWidgets.QGraphicsScene()
        opponent_result = np.random.choice(random_list)
        if opponent_result == "Rock":
            # self.ui.rock_img = QtGui.QPixmap('Rock.png').scaled(100, 100)
            opponent_scene.addPixmap(self.rock_img)
            self.ui.Opponent_Image.setScene(opponent_scene)
            self.ui.Loss_Count.setText(str(int(self.ui.Loss_Count.toPlainText()) + 1))
            self.ui.Loss_Count.setAlignment(Qt.AlignRight)
            self.ui.Game_Result.setText("You Lose :<")
            self.ui.Game_Result.setAlignment(Qt.AlignCenter)
        elif opponent_result == "Paper":
            # self.ui.paper_img = QtGui.QPixmap('Paper.png').scaled(75, 75)
            opponent_scene.addPixmap(self.paper_img)
            self.ui.Opponent_Image.setScene(opponent_scene)
            self.ui.Win_Count.setText(str(int(self.ui.Win_Count.toPlainText()) + 1))
            self.ui.Win_Count.setAlignment(Qt.AlignRight)
            self.ui.Game_Result.setText("You Win :>")
            self.ui.Game_Result.setAlignment(Qt.AlignCenter)
        elif opponent_result == "Scissors":
            opponent_scene.addPixmap(self.scissors_img)
            self.ui.Opponent_Image.setScene(opponent_scene)
            self.ui.Deuce_Count.setText(str(int(self.ui.Deuce_Count.toPlainText()) + 1))
            self.ui.Deuce_Count.setAlignment(Qt.AlignRight)
            self.ui.Game_Result.setText("Deuce!")
            self.ui.Game_Result.setAlignment(Qt.AlignCenter)
        pass


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Rock_Paper_Scissors_Machine = AppWindow()
    Rock_Paper_Scissors_Machine.show()
    sys.exit(app.exec_())
