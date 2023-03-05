# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Rock_Paper_Scissors_UI_V01aSUSvj.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Rock_Paper_Scissors(object):
    def setupUi(self, Rock_Paper_Scissors):
        if not Rock_Paper_Scissors.objectName():
            Rock_Paper_Scissors.setObjectName(u"Rock_Paper_Scissors")
        Rock_Paper_Scissors.resize(641, 533)
        Rock_Paper_Scissors.setLayoutDirection(Qt.LeftToRight)
        self.Rock_Button = QPushButton(Rock_Paper_Scissors)
        self.Rock_Button.setObjectName(u"Rock_Button")
        self.Rock_Button.setEnabled(True)
        self.Rock_Button.setGeometry(QRect(20, 400, 161, 41))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Rock_Button.setFont(font)
        self.Developer_Willy = QLabel(Rock_Paper_Scissors)
        self.Developer_Willy.setObjectName(u"Developer_Willy")
        self.Developer_Willy.setGeometry(QRect(10, 500, 411, 31))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setItalic(True)
        font1.setWeight(75)
        self.Developer_Willy.setFont(font1)
        self.Developer_Willy.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.Opponent_Text = QLabel(Rock_Paper_Scissors)
        self.Opponent_Text.setObjectName(u"Opponent_Text")
        self.Opponent_Text.setGeometry(QRect(220, 20, 200, 51))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setWeight(75)
        self.Opponent_Text.setFont(font2)
        self.Opponent_Text.setLayoutDirection(Qt.LeftToRight)
        self.Opponent_Text.setAlignment(Qt.AlignCenter)
        self.You_Image = QGraphicsView(Rock_Paper_Scissors)
        self.You_Image.setObjectName(u"You_Image")
        self.You_Image.setGeometry(QRect(270, 270, 100, 100))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.You_Image.sizePolicy().hasHeightForWidth())
        self.You_Image.setSizePolicy(sizePolicy)
        self.You_Image.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.You_Image.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.You_Text = QLabel(Rock_Paper_Scissors)
        self.You_Text.setObjectName(u"You_Text")
        self.You_Text.setGeometry(QRect(220, 460, 200, 51))
        self.You_Text.setFont(font2)
        self.You_Text.setLayoutDirection(Qt.LeftToRight)
        self.You_Text.setAlignment(Qt.AlignCenter)
        self.Win_Count = QTextEdit(Rock_Paper_Scissors)
        self.Win_Count.setObjectName(u"Win_Count")
        self.Win_Count.setEnabled(False)
        self.Win_Count.setGeometry(QRect(530, 260, 101, 31))
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(14)
        font3.setBold(False)
        font3.setWeight(50)
        self.Win_Count.setFont(font3)
        self.Win_Count.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Win_Count.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Opponent_Image = QGraphicsView(Rock_Paper_Scissors)
        self.Opponent_Image.setObjectName(u"Opponent_Image")
        self.Opponent_Image.setGeometry(QRect(270, 80, 100, 100))
        sizePolicy.setHeightForWidth(self.Opponent_Image.sizePolicy().hasHeightForWidth())
        self.Opponent_Image.setSizePolicy(sizePolicy)
        self.Opponent_Image.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Opponent_Image.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Paper_Button = QPushButton(Rock_Paper_Scissors)
        self.Paper_Button.setObjectName(u"Paper_Button")
        self.Paper_Button.setEnabled(True)
        self.Paper_Button.setGeometry(QRect(240, 400, 161, 41))
        self.Paper_Button.setFont(font)
        self.Scissors_Button = QPushButton(Rock_Paper_Scissors)
        self.Scissors_Button.setObjectName(u"Scissors_Button")
        self.Scissors_Button.setEnabled(True)
        self.Scissors_Button.setGeometry(QRect(460, 400, 161, 41))
        self.Scissors_Button.setFont(font)
        self.Deuce_Count = QTextEdit(Rock_Paper_Scissors)
        self.Deuce_Count.setObjectName(u"Deuce_Count")
        self.Deuce_Count.setEnabled(False)
        self.Deuce_Count.setGeometry(QRect(530, 300, 101, 31))
        self.Deuce_Count.setFont(font3)
        self.Deuce_Count.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Deuce_Count.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Loss_Count = QTextEdit(Rock_Paper_Scissors)
        self.Loss_Count.setObjectName(u"Loss_Count")
        self.Loss_Count.setEnabled(False)
        self.Loss_Count.setGeometry(QRect(530, 340, 101, 31))
        self.Loss_Count.setFont(font3)
        self.Loss_Count.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Loss_Count.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Win_Count_Text = QLabel(Rock_Paper_Scissors)
        self.Win_Count_Text.setObjectName(u"Win_Count_Text")
        self.Win_Count_Text.setGeometry(QRect(440, 260, 91, 31))
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setPointSize(13)
        font4.setBold(False)
        font4.setWeight(50)
        self.Win_Count_Text.setFont(font4)
        self.Win_Count_Text.setLayoutDirection(Qt.LeftToRight)
        self.Win_Count_Text.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.Deuce_Count_Text = QLabel(Rock_Paper_Scissors)
        self.Deuce_Count_Text.setObjectName(u"Deuce_Count_Text")
        self.Deuce_Count_Text.setGeometry(QRect(440, 300, 91, 31))
        self.Deuce_Count_Text.setFont(font4)
        self.Deuce_Count_Text.setLayoutDirection(Qt.LeftToRight)
        self.Deuce_Count_Text.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.Loss_Count_Text = QLabel(Rock_Paper_Scissors)
        self.Loss_Count_Text.setObjectName(u"Loss_Count_Text")
        self.Loss_Count_Text.setGeometry(QRect(440, 340, 91, 31))
        self.Loss_Count_Text.setFont(font4)
        self.Loss_Count_Text.setLayoutDirection(Qt.LeftToRight)
        self.Loss_Count_Text.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.Win_Count_Text_2 = QLabel(Rock_Paper_Scissors)
        self.Win_Count_Text_2.setObjectName(u"Win_Count_Text_2")
        self.Win_Count_Text_2.setGeometry(QRect(440, 210, 191, 31))
        font5 = QFont()
        font5.setFamily(u"Arial")
        font5.setPointSize(15)
        font5.setBold(True)
        font5.setWeight(75)
        self.Win_Count_Text_2.setFont(font5)
        self.Win_Count_Text_2.setLayoutDirection(Qt.LeftToRight)
        self.Win_Count_Text_2.setAlignment(Qt.AlignCenter)
        self.Game_Result = QTextEdit(Rock_Paper_Scissors)
        self.Game_Result.setObjectName(u"Game_Result")
        self.Game_Result.setEnabled(False)
        self.Game_Result.setGeometry(QRect(250, 210, 141, 31))
        self.Game_Result.setFont(font3)
        self.Game_Result.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Game_Result.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.retranslateUi(Rock_Paper_Scissors)

        QMetaObject.connectSlotsByName(Rock_Paper_Scissors)
    # setupUi

    def retranslateUi(self, Rock_Paper_Scissors):
        Rock_Paper_Scissors.setWindowTitle(QCoreApplication.translate("Rock_Paper_Scissors", u"Rock_Paper_Scissors", None))
        self.Rock_Button.setText(QCoreApplication.translate("Rock_Paper_Scissors", u"Rock", None))
        self.Developer_Willy.setText(QCoreApplication.translate("Rock_Paper_Scissors", u"Developed by Willy Fang", None))
        self.Opponent_Text.setText(QCoreApplication.translate("Rock_Paper_Scissors", u"Opponent", None))
        self.You_Text.setText(QCoreApplication.translate("Rock_Paper_Scissors", u"You", None))
        self.Win_Count.setHtml(QCoreApplication.translate("Rock_Paper_Scissors", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>", None))
        self.Paper_Button.setText(QCoreApplication.translate("Rock_Paper_Scissors", u"Paper", None))
        self.Scissors_Button.setText(QCoreApplication.translate("Rock_Paper_Scissors", u"Scissors", None))
        self.Deuce_Count.setHtml(QCoreApplication.translate("Rock_Paper_Scissors", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>", None))
        self.Loss_Count.setHtml(QCoreApplication.translate("Rock_Paper_Scissors", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>", None))
        self.Win_Count_Text.setText(QCoreApplication.translate("Rock_Paper_Scissors", u"Wins: ", None))
        self.Deuce_Count_Text.setText(QCoreApplication.translate("Rock_Paper_Scissors", u"Deuces: ", None))
        self.Loss_Count_Text.setText(QCoreApplication.translate("Rock_Paper_Scissors", u"Losses: ", None))
        self.Win_Count_Text_2.setText(QCoreApplication.translate("Rock_Paper_Scissors", u"Your Report", None))
        self.Game_Result.setHtml(QCoreApplication.translate("Rock_Paper_Scissors", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

