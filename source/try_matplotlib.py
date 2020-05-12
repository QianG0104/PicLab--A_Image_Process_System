import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

class Pic_m:
    def __init__(self,fname):
        self.Present_ARY=mpimg.imread(fname)

        self.Freq_ARY = np.fft.fftshift(
            np.fft.fft2(
                self.Present_ARY
            )
        )

        self.Histogram_Vector=[]

        self.History_List=[]
        self.Redo_List=[]
        #两个队列用于实现撤回和redo功能。
