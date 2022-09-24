# -*- coding: utf-8 -*-
"""
Created on 09/24, 2022
@author: Willy Fang

"""
# https://www.w3schools.com/python/ref_random_choice.asp
# https://www.jb51.net/article/206117.htm
# https://www.796t.com/article.php?id=299323
# https://walkonnet.com/archives/18139


from UI_V01 import *
import numpy as np
random_list = ["Rock", "Paper", "Scissors"]

# import matplotlib
# matplotlib.use("Qt5Agg")  # 聲明使用QT5
# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# import matplotlib.pyplot as plt
# import matplotlib.ticker as ticker
# from matplotlib.font_manager import FontProperties
# myfont=FontProperties(fname='微软正黑体.ttf')
# import seaborn as sns
# sns.set(color_codes=True,font=myfont.get_family())

# from matplotlib.figure import Figure
# from PySide2 import QtWidgets, QtCore


# class Figure_Canvas(FigureCanvas):   # 通過繼承FigureCanvas類，使得該類既是一個PyQt5的Qwidget，又是一個matplotlib的FigureCanvas，這是連線pyqt5與matplotlib的關鍵
#     def __init__(self, parent=None, width=10, height=10):
#         fig, self.ax1 = plt.subplots(figsize=(width, height), tight_layout=True)
#         FigureCanvas.__init__(self, fig)
#         self.setParent(parent)
#
#
#     def plot_chart(self, mode="Shelf", label_data=None):
#         # Encoder Mode
#         if mode == "Encoder":
#             plt.title("P12 Map (Encoder Mode)", fontproperties=myfont, fontsize=12)
#             plt.xlabel('Position_X', fontproperties=myfont, fontsize=10)
#             plt.ylabel('Position_Y', fontproperties=myfont, fontsize=10)
#             plt.xticks(fontsize=12)
#             plt.yticks(fontsize=12)
#             # https://moonbooks.org/Articles/How-to-plot-points-in-front-of-a-line-in-matplotlib-/
#             for i in range(0, map_data.shape[0], 2):
#                 plt.plot("Position_X", "Position_Y", data=map_data.iloc[i:i+2], linewidth=5, c="black", zorder=1)  # c="C0"
#             if isinstance(label_data, pd.DataFrame):
#                 label_data = label_data[["Position_X", "Position_Y"]].drop_duplicates().sort_values(by=["Position_X", "Position_Y"])
#                 plt.scatter("Position_X", "Position_Y", data=label_data, c="red", zorder=2, s=50)
#             self.ax1.xaxis.set_major_locator(ticker.MultipleLocator(5000))
#             self.ax1.yaxis.set_major_locator(ticker.MultipleLocator(2500))
#             self.ax1.invert_yaxis()
#             self.ax1.set_ylim((48500, -2000))
#             self.ax1.set_xlim((-4000, 48500))
#         # Shelf Mode
#         elif mode == "Shelf":
#             plt.title("P12 Map (Shelf Mode)", fontproperties=myfont, fontsize=12)
#             plt.xlabel('Position_X', fontproperties=myfont, fontsize=8)
#             plt.ylabel('Position_Y', fontproperties=myfont, fontsize=8)
#             plt.xticks(fontsize=9)
#             plt.yticks(fontsize=8)
#             # https://matplotlib.org/3.5.1/users/prev_whats_new/dflt_style_changes.html
#             # https://matplotlib.org/stable/api/markers_api.html
#             plt.scatter("Position_X", "Position_Y", data=pd.read_csv("P12_map_V03-1.csv"), marker="s", color="white", zorder=0, s=13)  # 通道+儲位
#             plt.scatter("Position_X", "Position_Y", data=pd.read_csv("P12_map_V03-2.csv"), marker="s", color="C0", zorder=1, s=13)  # 通道
#             plt.scatter("Position_X", "Position_Y", data=pd.read_csv("P12_map_V03-3.csv"), marker="s", color="yellow", zorder=2, s=13)  # 充電樁
#             if isinstance(label_data, pd.DataFrame):
#                 label_data = label_data[["Position_X", "Position_Y"]].drop_duplicates().sort_values(by=["Position_X", "Position_Y"])
#                 plt.scatter("Position_X", "Position_Y", data=label_data, marker="s", color="red", zorder=3, s=15)  # 異常點位置
#             plt.grid(None)
#             self.ax1.set_facecolor('black')
#             self.ax1.xaxis.set_major_locator(ticker.MultipleLocator(2))
#             self.ax1.yaxis.set_major_locator(ticker.MultipleLocator(2))
#             self.ax1.set_ylim((83.9, 0.1))
#             self.ax1.set_xlim((0.1, 64.9))
#
#         global error_location
#         if isinstance(label_data, pd.DataFrame):
#             error_location = ""
#             for xy in label_data[["Position_X", "Position_Y"]].values.tolist():
#                 error_location += str(xy)+"\n\n"
#             error_location = error_location.strip()
#         else:
#             error_location = ""


class AppWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Rock_Paper_Scissors()
        self.ui.setupUi(self)
        self.setup_control()
        self.show()

    def setup_control(self):
        # # 加载的图形（FigureCanvas）不能直接放到graphicview控件中，必须先放到graphicScene，然后再把graphicscene放到graphicview中
        # dr = Figure_Canvas(width=self.ui.graphicsView_1.width()/100.5, height=self.ui.graphicsView_1.height()/100.5)
        # dr.plot_chart()
        # GS = QGraphicsScene()  # 创建一个QGraphicsScene
        # GS.addWidget(dr)  # 把图形放到QGraphicsScene中，注意：图形是作为一个QWidget放到放到QGraphicsScene中的
        # self.ui.graphicsView_1.setScene(GS)  # 把QGraphicsScene放入QGraphicsView
        # self.ui.graphicsView_1.show()  # 调用show方法呈现图形
        self.ui.Rock_Button.clicked.connect(self.Rock_Button_clicked)
        self.ui.Paper_Button.clicked.connect(self.Paper_Button_clicked)
        self.ui.Scissors_Button.clicked.connect(self.Scissors_Button_clicked)

    def Rock_Button_clicked(self):
        # self.ui.graphicsView_1.setScene(None)
        # dr = Figure_Canvas(width=self.ui.graphicsView_1.width()/100.5, height=self.ui.graphicsView_1.height()/100.5)
        # dr.plot_chart(mode=self.ui.comboBox_5.currentText())
        # GS = QGraphicsScene()
        # GS.addWidget(dr)
        # self.ui.graphicsView_1.setScene(GS)
        # self.ui.graphicsView_1.show()
        opponent_result = np.random.choice(random_list)
        if opponent_result == "Rock":
            self.ui.Deuce_Count.setText(str(int(self.ui.Deuce_Count.toPlainText()) + 1))
            self.ui.Deuce_Count.setAlignment(Qt.AlignRight)
            self.ui.Game_Result.setText("Deuce!")
            self.ui.Game_Result.setAlignment(Qt.AlignCenter)
        elif opponent_result == "Paper":
            self.ui.Loss_Count.setText(str(int(self.ui.Loss_Count.toPlainText()) + 1))
            self.ui.Loss_Count.setAlignment(Qt.AlignRight)
            self.ui.Game_Result.setText("You Lose :<")
            self.ui.Game_Result.setAlignment(Qt.AlignCenter)
        elif opponent_result == "Scissors":
            self.ui.Win_Count.setText(str(int(self.ui.Win_Count.toPlainText()) + 1))
            self.ui.Win_Count.setAlignment(Qt.AlignRight)
            self.ui.Game_Result.setText("You Win :>")
            self.ui.Game_Result.setAlignment(Qt.AlignCenter)
        pass

    def Paper_Button_clicked(self):
        opponent_result = np.random.choice(random_list)
        if opponent_result == "Rock":
            self.ui.Win_Count.setText(str(int(self.ui.Win_Count.toPlainText()) + 1))
            self.ui.Win_Count.setAlignment(Qt.AlignRight)
            self.ui.Game_Result.setText("You Win :>")
            self.ui.Game_Result.setAlignment(Qt.AlignCenter)
        elif opponent_result == "Paper":
            self.ui.Deuce_Count.setText(str(int(self.ui.Deuce_Count.toPlainText()) + 1))
            self.ui.Deuce_Count.setAlignment(Qt.AlignRight)
            self.ui.Game_Result.setText("Deuce!")
            self.ui.Game_Result.setAlignment(Qt.AlignCenter)
        elif opponent_result == "Scissors":
            self.ui.Loss_Count.setText(str(int(self.ui.Loss_Count.toPlainText()) + 1))
            self.ui.Loss_Count.setAlignment(Qt.AlignRight)
            self.ui.Game_Result.setText("You Lose :<")
            self.ui.Game_Result.setAlignment(Qt.AlignCenter)
        pass

    def Scissors_Button_clicked(self):
        opponent_result = np.random.choice(random_list)
        if opponent_result == "Rock":
            self.ui.Loss_Count.setText(str(int(self.ui.Loss_Count.toPlainText()) + 1))
            self.ui.Loss_Count.setAlignment(Qt.AlignRight)
            self.ui.Game_Result.setText("You Lose :<")
            self.ui.Game_Result.setAlignment(Qt.AlignCenter)
        elif opponent_result == "Paper":
            self.ui.Win_Count.setText(str(int(self.ui.Win_Count.toPlainText()) + 1))
            self.ui.Win_Count.setAlignment(Qt.AlignRight)
            self.ui.Game_Result.setText("You Win :>")
            self.ui.Game_Result.setAlignment(Qt.AlignCenter)
        elif opponent_result == "Scissors":
            self.ui.Deuce_Count.setText(str(int(self.ui.Deuce_Count.toPlainText()) + 1))
            self.ui.Deuce_Count.setAlignment(Qt.AlignRight)
            self.ui.Game_Result.setText("Deuce!")
            self.ui.Game_Result.setAlignment(Qt.AlignCenter)
        pass


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Error_Data_Plot = AppWindow()
    Error_Data_Plot.show()
    sys.exit(app.exec_())
