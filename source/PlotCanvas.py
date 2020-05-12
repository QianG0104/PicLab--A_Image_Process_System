# import sys
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *

from Iterator import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.pyplot import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import numpy as np

from PIL import Image,ImageQt,ImageDraw


class PlotCanvas():

    def __init__(self,ARY,owner):
        self.Present_ARY=ARY
        self.owner=owner
        # self.Amplitude_Spectrum =20 * np.log(np.abs(owner.Freq_ARY))  # 幅度谱,乘20是为了保证显示效果
        # self.Phase_Spectrum =20 * np.log(np.angle(owner.Freq_ARY)*180/np.pi)  # 相位谱,同理乘20
        # self.Amplitude_Spectrum
        # self.Phase_Spectrum


        self.figure = plt.figure(facecolor='#FFFFFF')
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self.figure)

        self.freq_figure = plt.figure(facecolor='#FFFFFF')
        self.amp_ax = self.freq_figure.add_subplot(121)
        self.pha_ax = self.freq_figure.add_subplot(122)
        self.freq_canvas = FigureCanvas(self.freq_figure)

        self.refresh()
        # 初始化绘图区域

        self.hist_figure = plt.figure(facecolor='#FFFFFF')
        self.hist_ax = self.hist_figure.add_subplot(111)
        self.hist_canvas = FigureCanvas(self.hist_figure)
        # 初始化绘图区域

    def change_to(self,ARY):
        self.Present_ARY=ARY
        self.refresh()

    def refresh(self):
        self.ax.imshow(self.Present_ARY,cmap=cm.gray)
        self.canvas.draw()

    def draw_freq(self):
        Amplitude_Spectrum =10 * np.log(np.abs(self.owner.Freq_ARY))  # 幅度谱,乘20是为了保证显示效果
        Phase_Spectrum =10 * np.log(np.angle(self.owner.Freq_ARY)*180/np.pi)  # 相位谱,同理乘20
        self.amp_ax.imshow(Amplitude_Spectrum.astype(np.uint8),cmap=cm.gray)
        self.pha_ax.imshow(Phase_Spectrum.astype(np.uint8),cmap=cm.gray)
        self.freq_canvas.draw()

    def draw_hist(self):
        self.hist_ax.clear()
        keys=np.array(range(0,256))
        data=np.array(self.owner.Histogram_Vector)
        # self.hist_ax.hist(data)
        self.hist_ax.bar(keys,data,width=1.0)
        self.hist_canvas.draw()
