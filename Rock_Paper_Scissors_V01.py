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

random_list = ["Rock", "Paper", "Scissors"]


class AppWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Rock_Paper_Scissors()
        self.ui.setupUi(self)
        self.setup_control()
        self.show()

    def setup_control(self):
        self.ui.Rock_Button.clicked.connect(self.Rock_Button_clicked)
        self.ui.Paper_Button.clicked.connect(self.Paper_Button_clicked)
        self.ui.Scissors_Button.clicked.connect(self.Scissors_Button_clicked)

    def Rock_Button_clicked(self):
        rock_img = QtGui.QPixmap('Rock.png').scaled(100, 100)
        you_scene = QtWidgets.QGraphicsScene()
        you_scene.addPixmap(rock_img)
        self.ui.You_Image.setScene(you_scene)

        opponent_scene = QtWidgets.QGraphicsScene()
        opponent_result = np.random.choice(random_list)
        if opponent_result == "Rock":
            opponent_scene.addPixmap(rock_img)
            self.ui.Opponent_Image.setScene(opponent_scene)
            self.ui.Deuce_Count.setText(str(int(self.ui.Deuce_Count.toPlainText()) + 1))
            self.ui.Deuce_Count.setAlignment(Qt.AlignRight)
            self.ui.Game_Result.setText("Deuce!")
            self.ui.Game_Result.setAlignment(Qt.AlignCenter)
        elif opponent_result == "Paper":
            paper_img = QtGui.QPixmap('Paper.png').scaled(75, 75)
            opponent_scene.addPixmap(paper_img)
            self.ui.Opponent_Image.setScene(opponent_scene)
            self.ui.Loss_Count.setText(str(int(self.ui.Loss_Count.toPlainText()) + 1))
            self.ui.Loss_Count.setAlignment(Qt.AlignRight)
            self.ui.Game_Result.setText("You Lose :<")
            self.ui.Game_Result.setAlignment(Qt.AlignCenter)
        elif opponent_result == "Scissors":
            scissors_img = QtGui.QPixmap('Scissors.png').scaled(100, 100)
            opponent_scene.addPixmap(scissors_img)
            self.ui.Opponent_Image.setScene(opponent_scene)
            self.ui.Win_Count.setText(str(int(self.ui.Win_Count.toPlainText()) + 1))
            self.ui.Win_Count.setAlignment(Qt.AlignRight)
            self.ui.Game_Result.setText("You Win :>")
            self.ui.Game_Result.setAlignment(Qt.AlignCenter)
        pass

    def Paper_Button_clicked(self):
        paper_img = QtGui.QPixmap('Paper.png').scaled(75, 75)
        you_scene = QtWidgets.QGraphicsScene()
        you_scene.addPixmap(paper_img)
        self.ui.You_Image.setScene(you_scene)

        opponent_scene = QtWidgets.QGraphicsScene()
        opponent_result = np.random.choice(random_list)
        if opponent_result == "Rock":
            rock_img = QtGui.QPixmap('Rock.png').scaled(100, 100)
            opponent_scene.addPixmap(rock_img)
            self.ui.Opponent_Image.setScene(opponent_scene)
            self.ui.Win_Count.setText(str(int(self.ui.Win_Count.toPlainText()) + 1))
            self.ui.Win_Count.setAlignment(Qt.AlignRight)
            self.ui.Game_Result.setText("You Win :>")
            self.ui.Game_Result.setAlignment(Qt.AlignCenter)
        elif opponent_result == "Paper":
            opponent_scene.addPixmap(paper_img)
            self.ui.Opponent_Image.setScene(opponent_scene)
            self.ui.Deuce_Count.setText(str(int(self.ui.Deuce_Count.toPlainText()) + 1))
            self.ui.Deuce_Count.setAlignment(Qt.AlignRight)
            self.ui.Game_Result.setText("Deuce!")
            self.ui.Game_Result.setAlignment(Qt.AlignCenter)
        elif opponent_result == "Scissors":
            scissors_img = QtGui.QPixmap('Scissors.png').scaled(100, 100)
            opponent_scene.addPixmap(scissors_img)
            self.ui.Opponent_Image.setScene(opponent_scene)
            self.ui.Loss_Count.setText(str(int(self.ui.Loss_Count.toPlainText()) + 1))
            self.ui.Loss_Count.setAlignment(Qt.AlignRight)
            self.ui.Game_Result.setText("You Lose :<")
            self.ui.Game_Result.setAlignment(Qt.AlignCenter)
        pass

    def Scissors_Button_clicked(self):
        scissors_img = QtGui.QPixmap('Scissors.png').scaled(100, 100)
        you_scene = QtWidgets.QGraphicsScene()
        you_scene.addPixmap(scissors_img)
        self.ui.You_Image.setScene(you_scene)

        opponent_scene = QtWidgets.QGraphicsScene()
        opponent_result = np.random.choice(random_list)
        if opponent_result == "Rock":
            rock_img = QtGui.QPixmap('Rock.png').scaled(100, 100)
            opponent_scene.addPixmap(rock_img)
            self.ui.Opponent_Image.setScene(opponent_scene)
            self.ui.Loss_Count.setText(str(int(self.ui.Loss_Count.toPlainText()) + 1))
            self.ui.Loss_Count.setAlignment(Qt.AlignRight)
            self.ui.Game_Result.setText("You Lose :<")
            self.ui.Game_Result.setAlignment(Qt.AlignCenter)
        elif opponent_result == "Paper":
            paper_img = QtGui.QPixmap('Paper.png').scaled(75, 75)
            opponent_scene.addPixmap(paper_img)
            self.ui.Opponent_Image.setScene(opponent_scene)
            opponent_scene.addPixmap(paper_img)
            self.ui.Opponent_Image.setScene(opponent_scene)
            self.ui.Win_Count.setText(str(int(self.ui.Win_Count.toPlainText()) + 1))
            self.ui.Win_Count.setAlignment(Qt.AlignRight)
            self.ui.Game_Result.setText("You Win :>")
            self.ui.Game_Result.setAlignment(Qt.AlignCenter)
        elif opponent_result == "Scissors":
            opponent_scene.addPixmap(scissors_img)
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
