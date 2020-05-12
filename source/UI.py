from Pic import *
from Iterator import *
from Methods import *
from built_in_objects import *
from InputDialogs import *

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from PlotCanvas import *


class basicWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        fname, _ = QFileDialog.getOpenFileName(self)
        self.Picture = Pic(fname)
        self.initUI()
        self.refreshPic()

    def refreshPic(self):
        self.Picture.Get_Histogram()
        self.Picture.Fast_FT_Refresh()

        self.Picture.refresh_SpacialCanvas()
        self.Picture.SpacialCanvas.draw_freq()
        self.Picture.SpacialCanvas.draw_hist()
        # self.SpacialLabel.setPixmap(QPixmap.fromImage(self.Picture.submit_QImg()))
        # self.HistogramLabel.setPixmap(QPixmap.fromImage(self.Picture.submit_Histogram()))

    def loadPic(self):
        fname, _ = QFileDialog.getOpenFileName(self)
        if fname == '':
            return
        self.Picture = Pic(fname)
        self.Spacial_Monitor.setWidget(self.Picture.SpacialCanvas.canvas)
        self.Histogram_Monitor.setWidget(self.Picture.SpacialCanvas.hist_canvas)
        self.FreqDomain_Monitor.setWidget(self.Picture.SpacialCanvas.freq_canvas)
        self.refreshPic()

    def savePic(self):
        fname, _ = QFileDialog.getSaveFileName(self)
        if fname == '':
            return
        self.Picture.save_as(fname)

    def saveHG(self):
        fname, _ = QFileDialog.getSaveFileName(self)
        if fname == '':
            return
        self.Picture.save_HG_as(fname)

    def recall(self):
        self.Picture.Step_Back()
        self.refreshPic()

    def redo(self):
        self.Picture.Step_Redo()
        self.refreshPic()

    def ToGrey(self):
        self.Picture.To_Grey()
        self.refreshPic()

    def ToBinDense(self):
        self.Picture.To_Binary_Density()
        self.refreshPic()

    def ToPixSty(self):
        self.Picture.To_Pixel_Style()
        self.refreshPic()

    def R90(self):
        self.Picture.Transpose('R90')
        self.refreshPic()

    def R180(self):
        self.Picture.Transpose('R180')
        self.refreshPic()

    def R270(self):
        self.Picture.Transpose('R270')
        self.refreshPic()

    def UD(self):
        self.Picture.Transpose('UD')
        self.refreshPic()

    def LR(self):
        self.Picture.Transpose('LR')
        self.refreshPic()

    def Resize(self):
        dialog = Resize_Dlg(self)
        dialog.show()

    def HG_Balance(self):
        self.Picture.HG_Balance()
        self.refreshPic()

    def HG_Segmentation(self):
        dialog = Binary_Threshold_Dlg(self)
        dialog.show()

    def simp_ave(self):
        self.Picture.Iterate_by(Simp_Ave_ITR)
        self.refreshPic()

    def four_nbr_ave(self):
        self.Picture.Iterate_by(Four_Nbr_Ave_ITR)
        self.refreshPic()

    def cen_wtd(self):
        self.Picture.Iterate_by(Cen_Wtd_ITR)
        self.refreshPic()

    def dst_wtd(self):
        self.Picture.Iterate_by(Dst_Wtd_ITR)
        self.refreshPic()

    def gray_diff_thresh(self):
        dialog = Grey_Threshold_Dlg(self)
        dialog.show()

    def median_filt(self):
        self.Picture.Iterate_by(Med_Filter_ITR)
        self.refreshPic()

    def max_filt(self):
        self.Picture.Iterate_by(Max_Filter_ITR)
        self.refreshPic()

    def min_filt(self):
        self.Picture.Iterate_by(Min_Filter_ITR)
        self.refreshPic()

    def Sobel_std(self):
        self.Picture.Iterate_by(Sobel_Std)
        self.refreshPic()

    def Lap_4nbr(self):
        self.Picture.Iterate_by(Lap_4nbr)
        self.refreshPic()

    def Lap_8nbr(self):
        self.Picture.Iterate_by(Lap_8nbr)
        self.refreshPic()

    def Modify_Mask(self):
        dialog = Mod_Mask_Dlg(self)
        dialog.show()

    def ILPF(self):
        dialog=ILPF_Dlg(self)
        dialog.show()

    def GLPF(self):
        dialog = GLPF_Dlg(self)
        dialog.show()

    # def show_Moni_Spa(self):
    #     self.SpacialLabel = QLabel()
    #     self.SpacialLabel.setAlignment(Qt.AlignCenter)
    #     self.Spacial_Monitor = QMdiSubWindow()
    #     self.Spacial_Monitor.setWidget(self.Picture.SpacialCanvas.canvas)
    #     self.Spacial_Monitor.setWindowTitle('图像')
    #     self.mdi.addSubWindow(self.Spacial_Monitor)
    #     self.Spacial_Monitor.show()
    #     self.refreshPic()
    #
    # def show_Moni_HG(self):
    #     self.HistogramLabel = QLabel()
    #     self.HistogramLabel.setAlignment(Qt.AlignCenter)
    #     self.Histogram_Monitor = QMdiSubWindow()
    #     self.Histogram_Monitor.setWidget(self.Picture.SpacialCanvas.hist_canvas)
    #     self.Histogram_Monitor.setWindowTitle('灰度直方图')
    #     self.mdi.addSubWindow(self.Histogram_Monitor)
    #     self.Histogram_Monitor.show()
    #     self.refreshPic()

    def initUI(self):
        # ******* ******* ******* ******* ******* ******* ******* #
        # 设置layout(布局)、widgets(控件)、subwindow(子窗口)

        # box = QHBoxLayout()
        #
        # self.label = QLabel()
        #
        # box.addWidget(self.label)
        #
        # widget = QWidget(self)
        # widget.setLayout(box)
        # self.setCentralWidget(widget)

        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)

        # self.SpacialLabel = QLabel()
        # self.SpacialLabel.setAlignment(Qt.AlignCenter)

        # self.HistogramLabel = QLabel()
        # self.HistogramLabel.setAlignment(Qt.AlignCenter)

        self.Spacial_Monitor = QMdiSubWindow()
        self.Spacial_Monitor.setWidget(self.Picture.SpacialCanvas.canvas)
        self.Spacial_Monitor.setWindowTitle('图像')

        self.Histogram_Monitor = QMdiSubWindow()
        self.Histogram_Monitor.setWidget(self.Picture.SpacialCanvas.hist_canvas)
        self.Histogram_Monitor.setWindowTitle('灰度直方图')

        self.FreqDomain_Monitor = QMdiSubWindow()
        self.FreqDomain_Monitor.setWidget(self.Picture.SpacialCanvas.freq_canvas)
        self.FreqDomain_Monitor.setWindowTitle('频域')

        self.mdi.addSubWindow(self.Spacial_Monitor)
        self.mdi.addSubWindow(self.Histogram_Monitor)
        self.mdi.addSubWindow(self.FreqDomain_Monitor)

        self.Spacial_Monitor.show()
        self.Histogram_Monitor.show()
        self.FreqDomain_Monitor.show()

        self.mdi.cascadeSubWindows()

        # ******* ******* ******* ******* ******* ******* ******* #

        # ******* ******* ******* ******* ******* ******* ******* #
        # 设置动作
        act_OpenFile = QAction('打开', self)
        act_OpenFile.setShortcut('Ctrl+O')
        act_OpenFile.setStatusTip('Open new File')
        act_OpenFile.triggered.connect(lambda: self.loadPic())
        act_SaveFile = QAction('图像', self)
        act_SaveFile.setShortcut('Ctrl+S')
        act_SaveFile.triggered.connect(lambda: self.savePic())
        act_SaveFile_HG = QAction('导出直方图', self)
        act_SaveFile_HG.setShortcut('Ctrl+H')
        act_SaveFile_HG.triggered.connect(lambda: self.saveHG())
        act_Refresh = QAction('刷新', self)
        act_Refresh.setShortcut('Ctrl+R')
        act_Refresh.triggered.connect(lambda: self.refreshPic())

        act_Recall = QAction('撤回', self)
        act_Recall.setShortcut('Ctrl+Z')
        act_Recall.triggered.connect(lambda: self.recall())
        act_Redo = QAction('重做', self)
        act_Redo.setShortcut('Ctrl+Alt+Z')
        act_Redo.triggered.connect(lambda: self.redo())

        act_ToGrey = QAction('灰度', self)
        act_ToGrey.triggered.connect(lambda: self.ToGrey())
        act_ToBinDense = QAction('点状', self)
        act_ToBinDense.triggered.connect(lambda: self.ToBinDense())
        act_ToPixSty = QAction('彩色点状', self)
        act_ToPixSty.triggered.connect(lambda: self.ToPixSty())

        act_R90 = QAction('逆时针90度', self)
        act_R90.triggered.connect(lambda: self.R90())
        act_R180 = QAction('180度', self)
        act_R180.triggered.connect(lambda: self.R180())
        act_R270 = QAction('顺时针90度', self)
        act_R270.triggered.connect(lambda: self.R270())
        act_UD = QAction('上下翻转', self)
        act_UD.triggered.connect(lambda: self.UD())
        act_LR = QAction('左右翻转', self)
        act_LR.triggered.connect(lambda: self.LR())

        act_Resize = QAction('重置尺寸', self)
        act_Resize.triggered.connect(lambda: self.Resize())

        act_HG_balance = QAction('直方图均化', self)
        act_HG_balance.triggered.connect(lambda: self.HG_Balance())
        act_HG_Segmentation = QAction('直方图切割', self)
        act_HG_Segmentation.triggered.connect(lambda: self.HG_Segmentation())

        act_smo_simp_ave = QAction('简单均值', self)
        act_smo_simp_ave.triggered.connect(lambda: self.simp_ave())
        act_4nbr_ave = QAction('4-邻域均值', self)
        act_4nbr_ave.triggered.connect(lambda: self.four_nbr_ave())
        act_center_wtd = QAction('中心加权', self)
        act_center_wtd.triggered.connect(lambda: self.cen_wtd())
        act_distance_wtd = QAction('距离加权', self)
        act_distance_wtd.triggered.connect(lambda: self.dst_wtd())
        act_gray_diff_thresh = QAction('带门限均值', self)
        act_gray_diff_thresh.triggered.connect(lambda: self.gray_diff_thresh())
        act_median_filt = QAction('中值滤波', self)
        act_median_filt.triggered.connect(lambda: self.median_filt())
        act_max_filt = QAction('最大值滤波', self)
        act_max_filt.triggered.connect(lambda: self.max_filt())
        act_min_filt = QAction('最小值滤波', self)
        act_min_filt.triggered.connect(lambda: self.min_filt())
        #
        act_shp_std_sobel = QAction('标准', self)
        act_shp_std_sobel.triggered.connect(lambda: self.Sobel_std())

        act_shp_lap_4nbr = QAction('4-邻域拉氏', self)
        act_shp_lap_4nbr.triggered.connect(lambda: self.Lap_4nbr())
        act_shp_lap_8nbr = QAction('8-邻域拉氏', self)
        act_shp_lap_8nbr.triggered.connect(lambda: self.Lap_8nbr())

        act_mod_mask = QAction('自定义3x3线性算子滤波', self)
        act_mod_mask.triggered.connect(lambda: self.Modify_Mask())



        act_ILPF_filt = QAction('理想低通滤波', self)
        act_ILPF_filt.triggered.connect(lambda: self.ILPF())
        act_GLPF_filt = QAction('高斯低通滤波', self)
        act_GLPF_filt.triggered.connect(lambda: self.GLPF())
        # act_show_moni_Spa = QAction('图像', self)
        # act_show_moni_Spa.triggered.connect(lambda: self.show_Moni_Spa())
        # act_show_moni_HG = QAction('直方图', self)
        # act_show_moni_HG.triggered.connect(lambda: self.show_Moni_HG())

        # ******* ******* ******* ******* ******* ******* ******* #

        # ******* ******* ******* ******* ******* ******* ******* #
        # 设置菜单
        menu = self.menuBar()
        menu_file = menu.addMenu('&PicLab')
        menu_file.addAction(act_OpenFile)

        menu_save = menu_file.addMenu('导出')
        menu_save.addAction(act_SaveFile)
        menu_save.addAction(act_SaveFile_HG)

        menu_file.addAction(act_Refresh)

        menu_edit = menu.addMenu('&编辑')
        menu_edit.addAction(act_Recall)
        menu_edit.addAction(act_Redo)

        menu_trans = menu.addMenu('&图像变换')
        menu_trans.addAction(act_Resize)
        menu_trans.addAction(act_ToGrey)
        menu_trans.addAction(act_ToBinDense)
        menu_trans.addAction(act_ToPixSty)
        menu_trans_rot = menu_trans.addMenu('旋转')
        menu_trans_rot.addAction(act_R90)
        menu_trans_rot.addAction(act_R270)
        menu_trans_rot.addAction(act_R180)
        menu_trans_rev = menu_trans.addMenu('翻转')
        menu_trans_rev.addAction(act_UD)
        menu_trans_rev.addAction(act_LR)

        menu_enhance = menu.addMenu('&图像增强')

        menu_histogram = menu_enhance.addMenu('直方图')
        menu_histogram.addAction(act_HG_balance)
        menu_histogram.addAction(act_HG_Segmentation)

        menu_smoothing = menu_enhance.addMenu('平滑')
        menu_average_filt = menu_smoothing.addMenu('3x3均值滤波')
        menu_average_filt.addAction(act_smo_simp_ave)
        menu_average_filt.addAction(act_4nbr_ave)
        menu_average_filt.addAction(act_center_wtd)
        menu_average_filt.addAction(act_distance_wtd)
        menu_average_filt.addAction(act_gray_diff_thresh)
        menu_statistic_filt = menu_smoothing.addMenu('3x3统计滤波')
        menu_statistic_filt.addAction(act_median_filt)
        menu_statistic_filt.addAction(act_max_filt)
        menu_statistic_filt.addAction(act_min_filt)

        menu_smoothing.addAction(act_ILPF_filt)
        menu_smoothing.addAction(act_GLPF_filt)

        menu_sharpening = menu_enhance.addMenu('锐化')

        menu_sharpening_sobel = menu_sharpening.addMenu('Sobel')
        menu_sharpening_sobel.addAction(act_shp_std_sobel)

        menu_sharpening_lap = menu_sharpening.addMenu('拉普拉斯')
        menu_sharpening_lap.addAction(act_shp_lap_4nbr)
        menu_sharpening_lap.addAction(act_shp_lap_8nbr)

        menu_enhance.addAction(act_mod_mask)

        # menu_monitor = menu.addMenu('&窗口')
        # menu_monitor.addAction(act_show_moni_Spa)
        # menu_monitor.addAction(act_show_moni_HG)

        # ******* ******* ******* ******* ******* ******* ******* #

        # ******* ******* ******* ******* ******* ******* ******* #
        # 设置显示参数并显示主窗口

        self.setWindowTitle('PicLab')  # 窗口标题
        self.statusBar().showMessage('Main Window')  # 窗口下方信息栏(状态栏)
        self.showMaximized()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    BasicWindow = basicWindow()
    sys.exit(app.exec_())