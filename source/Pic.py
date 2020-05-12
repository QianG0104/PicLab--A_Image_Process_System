from PIL import Image,ImageQt,ImageDraw
import numpy as np
from Iterator import *

from PlotCanvas import *

class Pic:
    def __init__(self,fname):
        self.Ori_IMG=Image.open(fname)

        self.Present_ARY=np.array(self.Ori_IMG)

        self.Freq_ARY=np.fft.fftshift(
            np.fft.fft2(
                self.Present_ARY
            )
        )

        self.Histogram_Vector=[]

        self.History_List=[]
        self.Redo_List=[]
        #两个队列用于实现撤回和redo功能。

        self.SpacialCanvas=PlotCanvas(self.Present_ARY,self)



    #######   part * 直方图相关功能   #######
    def Get_Histogram(self):
        self.Histogram_Vector=[]
        for i in range(256):
            self.Histogram_Vector.append(0)
        # self.Histogram_Vector=np.zeros((256, 1), dtype=self.Present_ARY.dtype)

        Histogram_ITR=ITR(
            sf_single,[],
            # cf_for_histogram,[self.Histogram_Vector],
            cf_for_histogram,[self],
            rf_linear,[1.0,0]
        )
        self.temp_Iterate_by(Histogram_ITR)

    def HG_Balance(self):
        HG_Balance_ITR=ITR(
            sf_single,[],
            cf_single,[],
            rf_refrence_list,[Histogram_Balance(self.Histogram_Vector)]
        )
        self.Iterate_by(HG_Balance_ITR)



    #######   part * 使用通用迭代器   #######

    def Iterate_by(self,Itr):
        self.To_Grey()
        self.Present_ARY=Itr.Iterate(self.Present_ARY)

    def Freq_Iterate_by(self,Itr):
        self.To_Grey()
        self.Freq_ARY=Itr.Iterate(self.Freq_ARY)
        self.Fast_iFT_Rebuilt()

    def temp_Iterate_by(self,Itr):
        tempIMG=Image.fromarray(self.Present_ARY)
        tempIMG=tempIMG.convert('L')
        Itr.Iterate(np.array(tempIMG))

    #######   part * 频域变换基本功能   #######

    def Fast_FT_Refresh(self):
        self.Freq_ARY = np.fft.fftshift(
            np.fft.fft2(
                self.Present_ARY
            )
        )

    def Fast_iFT_Rebuilt(self):
        self.Present_ARY=np.fft.ifft2(
            np.fft.ifftshift(
                self.Freq_ARY
            )
        )
        self.Present_ARY=np.abs(self.Present_ARY)

    #######   part 1 对20步撤回与重做的支持   #######

    def Step_Forward(self):
        self.History_List.append(self.Present_ARY)
        self.Redo_List.clear()
        if len(self.History_List)>=20:
            self.History_List.remove(0)
    def Step_Back(self):
        if len(self.History_List)==0:
            return False
        else:
            self.Redo_List.append(self.Present_ARY)
            self.Present_ARY=self.History_List.pop()
            return True
    def Step_Redo(self):
        if len(self.Redo_List)==0:
            return False
        else:
            self.History_List.append(self.Present_ARY)
            self.Present_ARY=self.Redo_List.pop()
            return True

    #######   part 2 坐标变换功能   #######

    def Transpose(self,flag):       # 逆时针、顺时针旋转90度/旋转180度/垂直、水平翻转
        if flag=='R90':
            self.Step_Forward()
            tempIMG=Image.fromarray(self.Present_ARY)
            tempIMG=tempIMG.transpose(Image.ROTATE_90)
            self.Present_ARY=np.array(tempIMG)
        elif flag=='R180':
            self.Step_Forward()
            tempIMG=Image.fromarray(self.Present_ARY)
            tempIMG=tempIMG.transpose(Image.ROTATE_180)
            self.Present_ARY=np.array(tempIMG)
        elif flag=='R270':
            self.Step_Forward()
            tempIMG=Image.fromarray(self.Present_ARY)
            tempIMG=tempIMG.transpose(Image.ROTATE_270)
            self.Present_ARY=np.array(tempIMG)
        elif flag=='UD':
            self.Step_Forward()
            tempIMG=Image.fromarray(self.Present_ARY)
            tempIMG=tempIMG.transpose(Image.FLIP_TOP_BOTTOM)
            self.Present_ARY=np.array(tempIMG)
        elif flag=='LR':
            self.Step_Forward()
            tempIMG=Image.fromarray(self.Present_ARY)
            tempIMG=tempIMG.transpose(Image.FLIP_LEFT_RIGHT)
            self.Present_ARY=np.array(tempIMG)
        else:
            return False
        return True

    def Resize(self,new_width,new_height):  # 改变大小
        self.Step_Forward()
        tempIMG=Image.fromarray(self.Present_ARY)
        tempIMG=tempIMG.resize((new_width,new_height),Image.NEAREST)
        self.Present_ARY=np.array(tempIMG)

    #######   part 3 通道变换功能   #######

    def To_Binary_Density(self):        # 转换成黑白密度图
        self.Step_Forward()
        tempIMG=Image.fromarray(self.Present_ARY)
        tempIMG=tempIMG.convert('1')
        self.Present_ARY=np.array(tempIMG)
        # self.Present_Img = self.Present_Img.convert('1')

    def To_Grey(self):      # 转换成灰度
        self.Step_Forward()
        tempIMG=Image.fromarray(self.Present_ARY)
        tempIMG=tempIMG.convert('L')
        self.Present_ARY=np.array(tempIMG)
        # self.Present_Img = self.Present_Img.convert('L')

    def To_Pixel_Style(self):       # 转换成像素风格
        self.Step_Forward()
        tempIMG=Image.fromarray(self.Present_ARY)
        tempIMG=tempIMG.convert('P')
        self.Present_ARY=np.array(tempIMG)
        # self.Present_Img = self.Present_Img.convert('P')


    #######   part -1 杂项功能   #######
    def save_as(self,fname):
        tempIMG=Image.fromarray(self.Present_ARY)
        tempIMG.save(fname)

    def display(self):      # 用系统图片浏览工具显示
        tempIMG=Image.fromarray(self.Present_ARY)
        tempIMG.show()

    # def submit_QImg(self):
    #     tempIMG=Image.fromarray(self.Present_ARY)
    #     submit=ImageQt.ImageQt(tempIMG)
    #     return submit
    def refresh_SpacialCanvas(self):
        self.SpacialCanvas.change_to(self.Present_ARY)
        self.SpacialCanvas.refresh()

    # def submit_Histogram(self):
    #     tempHis=Image.new('RGB',(256,256),(255,255,255))
    #     draw=ImageDraw.Draw(tempHis)
    #     for i in range(256):
    #         h=(self.Histogram_Vector[i]*200)/(max(self.Histogram_Vector))
    #         source=(i,255)
    #         target=(i,255-h)
    #         draw.line([source,target],(70,70,255))
    #
    #         draw.line([(31,255),(31,0)],(0,0,0))
    #         draw.line([(63,255),(63,0)],(0,0,0))
    #         draw.line([(95,255),(95,0)],(0,0,0))
    #         draw.line([(127,255),(127,0)],(0,0,0))
    #         draw.line([(159,255),(159,0)],(0,0,0))
    #         draw.line([(191,255),(191,0)],(0,0,0))
    #         draw.line([(223,255),(223,0)],(0,0,0))
    #
    #     submit=ImageQt.ImageQt(tempHis)
    #     return submit
    def refresh_Histogram(self):
        self.SpacialCanvas.draw_hist()

    def save_HG_as(self,fname):
        tempHis=Image.new('RGB',(256,256),(255,255,255))
        draw=ImageDraw.Draw(tempHis)
        for i in range(256):
            h=(self.Histogram_Vector[i]*200)/(max(self.Histogram_Vector))
            source=(i,255)
            target=(i,255-h)
            draw.line([source,target],(70,70,255))

            draw.line([(31,255),(31,0)],(0,0,0))
            draw.line([(63,255),(63,0)],(0,0,0))
            draw.line([(95,255),(95,0)],(0,0,0))
            draw.line([(127,255),(127,0)],(0,0,0))
            draw.line([(159,255),(159,0)],(0,0,0))
            draw.line([(191,255),(191,0)],(0,0,0))
            draw.line([(223,255),(223,0)],(0,0,0))

        tempHis.save(fname)