import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.pyplot import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from PIL import Image,ImageQt,ImageDraw

from Iterator import *

class PlotCanvas():

    def __init__(self,ARY):
        self.Present_ARY=ARY

        self.figure=plt.figure(facecolor='#FFFFFF')
        self.ax=self.figure.add_subplot(111)
        self.canvas=FigureCanvas(self.figure)
        self.refresh()
        #初始化绘图区域

    def change_to(self,ARY):
        self.Present_ARY=ARY
        self.refresh()

    def refresh(self):
        self.ax.imshow(self.Present_ARY,cmap=cm.gray)
        self.canvas.draw()


# import sys
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
#
# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# from matplotlib.figure import Figure
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
#
# from PIL import Image,ImageQt,ImageDraw
#
# from Iterator import *
#
# class PlotCanvas():
#
#     def __init__(self,fname):
#         self.Present_ARY=mpimg.imread(fname)
#         print(self.Present_ARY)
#
#         self.figure=plt.figure(facecolor='#FFFFFF')
#         self.ax=self.figure.add_subplot(111)
#         self.canvas=FigureCanvas(self.figure)
#         self.refresh()
#         #初始化绘图区域
#
#
#
#         self.History_List=[]
#         self.Redo_List=[]
#         #两个队列用于实现撤回和redo功能。
#
#     def load(self,fname):
#         self.Present_ARY=mpimg.imread(fname)
#         self.refresh()
#
#     def refresh(self):
#         self.ax.imshow(self.Present_ARY)
#         self.canvas.draw()
#
#     #######   part 1 对20步撤回与重做的支持   #######
#
#     def Step_Forward(self):
#         self.History_List.append(self.Present_ARY)
#         self.Redo_List.clear()
#         if len(self.History_List) >= 20:
#             self.History_List.remove(0)
#
#     def Step_Back(self):
#         if len(self.History_List) == 0:
#             return False
#         else:
#             self.Redo_List.append(self.Present_ARY)
#             self.Present_ARY = self.History_List.pop()
#             return True
#
#     def Step_Redo(self):
#         if len(self.Redo_List) == 0:
#             return False
#         else:
#             self.History_List.append(self.Present_ARY)
#             self.Present_ARY = self.Redo_List.pop()
#             return True
#
#     #######   part 2 坐标变换功能   #######
#
#     def Transpose(self, flag):  # 逆时针、顺时针旋转90度/旋转180度/垂直、水平翻转
#         if flag == 'R90':
#             self.Step_Forward()
#             tempIMG = Image.fromarray(self.Present_ARY)
#             tempIMG = tempIMG.transpose(Image.ROTATE_90)
#             self.Present_ARY = np.array(tempIMG)
#         elif flag == 'R180':
#             self.Step_Forward()
#             tempIMG = Image.fromarray(self.Present_ARY)
#             tempIMG = tempIMG.transpose(Image.ROTATE_180)
#             self.Present_ARY = np.array(tempIMG)
#         elif flag == 'R270':
#             self.Step_Forward()
#             tempIMG = Image.fromarray(self.Present_ARY)
#             tempIMG = tempIMG.transpose(Image.ROTATE_270)
#             self.Present_ARY = np.array(tempIMG)
#         elif flag == 'UD':
#             self.Step_Forward()
#             tempIMG = Image.fromarray(self.Present_ARY)
#             tempIMG = tempIMG.transpose(Image.FLIP_TOP_BOTTOM)
#             self.Present_ARY = np.array(tempIMG)
#         elif flag == 'LR':
#             self.Step_Forward()
#             tempIMG = Image.fromarray(self.Present_ARY)
#             tempIMG = tempIMG.transpose(Image.FLIP_LEFT_RIGHT)
#             self.Present_ARY = np.array(tempIMG)
#         else:
#             return False
#         return True
#
#     def Resize(self, new_width, new_height):  # 改变大小
#         self.Step_Forward()
#         tempIMG = Image.fromarray(self.Present_ARY)
#         tempIMG = tempIMG.resize((new_width, new_height), Image.NEAREST)
#         self.Present_ARY = np.array(tempIMG)
#
#     #######   part 3 通道变换功能   #######
#
#     def To_Binary_Density(self):  # 转换成黑白密度图
#         self.Step_Forward()
#         tempIMG = Image.fromarray(self.Present_ARY)
#         tempIMG = tempIMG.convert('1')
#         self.Present_ARY = np.array(tempIMG)
#         # self.Present_Img = self.Present_Img.convert('1')
#
#     def To_Grey(self):  # 转换成灰度
#         self.Step_Forward()
#         tempIMG = Image.fromarray(self.Present_ARY)
#         tempIMG = tempIMG.convert('L')
#         self.Present_ARY = np.array(tempIMG)
#         # self.Present_Img = self.Present_Img.convert('L')
#
#     def To_Pixel_Style(self):  # 转换成像素风格
#         self.Step_Forward()
#         tempIMG = Image.fromarray(self.Present_ARY)
#         tempIMG = tempIMG.convert('P')
#         self.Present_ARY = np.array(tempIMG)
#         # self.Present_Img = self.Present_Img.convert('P')
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#         # fig=plt.imshow(self.Present_ARY)
#         # self.axes = fig.add_subplot(111)
#
#         # FigureCanvas.__init__(self, fig)
#         # self.setParent(parent)
#         #
#         # FigureCanvas.setSizePolicy(self,
#         #                            QSizePolicy.Expanding,
#         #                            QSizePolicy.Expanding)
#         # FigureCanvas.updateGeometry(self)
#         # self.init_plot()#打开App时可以初始化图片
#         # self.plot()
#
#     # def plot(self):
#
#
#
#     # def init_plot(self):
#     #     x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     #     y = [23, 21, 32, 13, 3, 132, 13, 3, 1]
#     #     self.axes.plot(x, y)
#
#     # def update_figure(self):
#         # x = np.linspace(0, 10, 10)
#         # y = [random.randint(0, 10) for i in range(10)]
#         # xx = np.linspace(0, 10)
#         # f = interpolate.interp1d(x, y, 'quadratic')  # 产生插值曲线的函数
#         # yy = f(xx)
#         # self.axes.cla()
#         # self.axes.plot(x, y, 'o',xx,yy)
#         # self.draw()
#
# # class PlotCanvas(FigureCanvas):
# #
# #     def __init__(self, parent=None, width=5, height=4, dpi=100):
# #         fig = Figure(figsize=(width, height), dpi=dpi)
# #         self.axes = fig.add_subplot(111)
# #
# #         FigureCanvas.__init__(self, fig)
# #         self.setParent(parent)
# #
# #         FigureCanvas.setSizePolicy(self,
# #                                    QSizePolicy.Expanding,
# #                                    QSizePolicy.Expanding)
# #         FigureCanvas.updateGeometry(self)
# #         self.init_plot()#打开App时可以初始化图片
# #         #self.plot()
# #
# #     def plot(self):
# #
# #         timer = QTimer(self)
# #         timer.timeout.connect(self.update_figure)
# #         timer.start(100)
# #
# #     def init_plot(self):
# #         x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# #         y = [23, 21, 32, 13, 3, 132, 13, 3, 1]
# #         self.axes.plot(x, y)
# #
# #     def update_figure(self):
# #         # x = np.linspace(0, 10, 10)
# #         # y = [random.randint(0, 10) for i in range(10)]
# #         # xx = np.linspace(0, 10)
# #         # f = interpolate.interp1d(x, y, 'quadratic')  # 产生插值曲线的函数
# #         # yy = f(xx)
# #         self.axes.cla()
# #         self.axes.plot(x, y, 'o',xx,yy)
# #         self.draw()
#
#
#
# # if __name__ == '__main__':
# #     app = QApplication(sys.argv)
# #     ex = App()
# #     sys.exit(app.exec_())
