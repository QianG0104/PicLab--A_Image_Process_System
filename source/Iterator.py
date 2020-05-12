from PIL import Image,ImageQt
from Methods import *
import numpy as np

class ITR:
    def __init__(self,sample_func,sf_args,converage_func,cf_args,reflect_func,rf_args):
        self.sample=sample_func
        self.conv=converage_func
        self.reflect=reflect_func

        self.sf_args=sf_args
        self.cf_args=cf_args
        self.rf_args=rf_args

    def Iterate(self,img_ARY):
        m,n=img_ARY.shape
        result=np.zeros((m,n),dtype=img_ARY.dtype)
        for i in range(m):
            for j in range(n):
                result[i,j]=\
                    self.reflect(
                        self.conv(
                            self.sample(
                                (i,j),img_ARY,
                                self.sf_args
                            ),
                            self.cf_args
                        ),
                        self.rf_args
                    )
        return result

    def reset_sf_args(self,new_args):
        self.sf_args=new_args

    def reset_cf_args(self,new_args):
        self.cf_args=new_args

    def reset_rf_args(self,new_args):
        self.rf_args=new_args


# 三种函数的命名规范：

# 取样函数：sf_****(center,img,args):return values
#   参数表：「center=(i,j);img=img;args=args」
#   返回值：values=[center=(i,j),center_value,nbr_value_1,nbr_value_2,.....,nbr_value_n]

# 收敛函数: cf_****(values,args):return value
#   参数表: values是与之搭配的取样函数的返回值
#   返回值：广义单值(list合法)

# 映射函数: rf_****(value,args):return result
#   参数表: value是与之搭配的收敛函数的返回值
#   返回值：严格单值(仅int)
