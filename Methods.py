from PIL import Image,ImageQt
import numpy as np
from collections import Counter

# 三种函数的命名规范：

# 取样函数：def sf_****(center,img,args):return values
#   参数表：「center=(i,j);img=img;args=args」
#   返回值：values=[center=(i,j),center_value,nbr_value_1,nbr_value_2,.....,nbr_value_n]

# 收敛函数: def cf_****(values,args):return value
#   参数表: values是与之搭配的取样函数的返回值
#   返回值：广义单值(list合法)

# 映射函数: def rf_****(value,args):return result
#   参数表: value是与之搭配的收敛函数的返回值
#   返回值：严格单值(仅int)



#######    SF   #######

def sf_8nbr(center,img,args):
    # args=[weight0,weight1,...,weight8]
    m,n=img.shape
    i,j=center
    values=[center,0,  0,0,0,  0,  0,  0,0,0]
    values[1]=img[i,j]*args[4]

    if i!=0 and j!=0:
        values[2]=img[i-1,j-1]*args[0]
    if i!=0:
        values[3]=img[i-1,j]*args[1]
    if i!=0 and j!=(n-1):
        values[4]=img[i-1,j+1]*args[2]
    if j!=0:
        values[5]=img[i,j-1]*args[3]
    if j!=(n-1):
        values[6]=img[i,j+1]*args[5]
    if i!=(m-1) and j!=0:
        values[7]=img[i+1,j-1]*args[6]
    if i!=(m-1):
        values[8]=img[i+1,j]*args[7]
    if i!=(m-1) and j!=(n-1):
        values[9]=img[i+1,j+1]*args[8]

    return values

def sf_4nbr(center,img,args):
    # args=[weight0,weight1,...,weight4]
    m,n=img.shape
    i,j=center
    values=[center,0,  0,  0,0,  0]
    values[1]=img[i,j]*args[2]

    if i!=0:
        values[2]=img[i-1,j]*args[0]
    if j!=0:
        values[3]=img[i,j-1]*args[1]
    if j!=(n-1):
        values[4]=img[i,j+1]*args[3]
    if i!=(m-1):
        values[5]=img[i+1,j]*args[4]

    return values

def sf_single(center,img,args):
    # args=[]
    i,j=center
    values=[center,img[i,j]]
    return values


#######    CF   #######

def cf_add(values,args):
    # args=[]
    value=0
    for i in range(len(values)):
        if i ==0:
            continue
        else:
            value=value+values[i]
    return value

def cf_sobel(values,args):
    # args=[]
    Gx=[0, 0,    1,2,1,    0,  0,    -1,-2,-1]
    Gy=[0, 0,    1,0,-1,    2,  -2,    1,0,-1]
    sub_x=0
    sub_y=0
    for i in range(len(values)):
        if i==0:
            continue
        else:
            sub_x=sub_x+values[i]*Gx[i]
            sub_y=sub_y+values[i]*Gy[i]

    value=np.sqrt(sub_x**2+sub_y**2)

    return value

def cf_gray_thresh(values,args):
    T=args[0]
    ori=values[1]
    value=0
    for i in range(len(values)):
        if i==0:
            continue
        else:
            value=value+values[i]
    value=value/(len(values)-1)

    e=np.abs(ori-value)
    if e>T:
        value=value
    else:
        value=ori

    return value


def cf_statistic_filt(values,args):
    #args=[flag,weight_center,weight_nbr_0,weignt_nbr_2,...,weight_nbr_n]
    flag=args[0]
    group=[]
    for order in range(len(values)):
        if order==0:
            continue
        else:
            for t in range(args[order]):
                group.append(values[order])
    group.sort()
    value=group[int(len(group)/2)]
    if flag=='min':
        value=group[0]
    elif flag=='max':
        value=group[-1]
    elif flag=='median':
        value=value
    elif flag=='midpoint':
        value=(group[0]+group[-1])/2
    elif flag=='most_freq':
        temp=Counter(group)
        value=list(dict(temp.most_common()).keys())[0]

    return value

def cf_for_histogram(values,args):
    # args=[owner]
    value=values[1]
    owner=args[0]
    new_values=owner.Histogram_Vector
    new_values[int(value)]=new_values[int(value)]+1
    owner.Histogram_Vector=new_values
    return value


def cf_single(values,args):
    # args=[]
    value=values[1]
    return value


#######    RF   #######

def rf_linear(value,args):
    # args=[scale,bias]
    result=value*args[0]+args[1]
    if result<0:
        result=0
    elif result>255:
        result=255
    return result

def rf_binary(value,args):
    # args=[threshold]
    T=args[0]
    result=value
    if result<T:
        result=0
    else:
        result=255
    return result

def rf_refrence_list(value,args):
    # args=[refrence_list]
    refrence_list=args[0]
    result=rf_linear(refrence_list[value],[255.0,0])
    return result


#######    杂项函数   #######

def Histogram_Balance(ori_vec):
    s=[0]*256
    new_vec=[]
    N=sum(ori_vec)
    for i in range(256):
        # print(ori_vec[i]/N)
        # s[i]=int(ori_vec[i]/N)
        s[i]=ori_vec[i]/N
        if i==0:
            new_vec.append(s[i])
        else:
            new_vec.append(s[i]+new_vec[i-1])
    # print(s)
    # print(new_vec)
    return new_vec