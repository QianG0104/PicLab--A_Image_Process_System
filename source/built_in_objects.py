from Methods import *
from Iterator import *
from Pic import *

#######    Iterator : 3*3 Operator   #######

Simp_Ave_ITR=ITR(
    sf_8nbr,[1,1,1,1,1,1,1,1,1],
    cf_add,[],
    rf_linear,[1.0/9.0,0]
)

Four_Nbr_Ave_ITR=ITR(
    sf_4nbr,[1,1,1,1,1],
    cf_add,[],
    rf_linear,[1.0/5.0,0]
)

Cen_Wtd_ITR=ITR(
    sf_4nbr,[1,1,2,1,1],
    cf_add,[],
    rf_linear,[1.0/6.0,0]
)

Dst_Wtd_ITR=ITR(
    sf_8nbr,[1,2,1,2,4,2,1,2,1],
    cf_add,[],
    rf_linear,[1.0/16.0,0]
)

Gray_Diff_Thresh_ITR_fmd=ITR(
    sf_8nbr,[1,1,1,1,1,1,1,1,1],
    cf_gray_thresh,[0],
    rf_linear,[1.0,0]
)

Med_Filter_ITR=ITR(
    sf_8nbr,[1,1,1,1,1,1,1,1,1],
    cf_statistic_filt,['median',1,1,1,1,1,1,1,1,1],
    rf_linear,[1.0,0]
)

Max_Filter_ITR=ITR(
    sf_8nbr,[1,1,1,1,1,1,1,1,1],
    cf_statistic_filt,['max',1,1,1,1,1,1,1,1,1],
    rf_linear,[1.0,0]
)

Min_Filter_ITR=ITR(
    sf_8nbr,[1,1,1,1,1,1,1,1,1],
    cf_statistic_filt,['min',1,1,1,1,1,1,1,1,1],
    rf_linear,[1.0,0]
)

Lap_4nbr=ITR(
    sf_4nbr,[-1,-1,5,-1,-1],
    cf_add,[],
    rf_linear,[1.0,0]
)

Lap_8nbr=ITR(
    sf_8nbr,[-1,-1,-1,-1,9,-1,-1,-1,-1],
    cf_add,[],
    rf_linear,[1.0,0]
)

Sobel_Std=ITR(
    sf_8nbr,[1,1,1,1,1,1,1,1,1],
    cf_sobel,[],
    rf_linear,[1,0]
)

Mask_fmd=ITR(
    sf_8nbr, [1, 1, 1, 1, 1, 1, 1, 1, 1],
    cf_add, [],
    rf_linear, [1.0 / 9.0, 0]
)

Binary_fmd=ITR(
    sf_single,[],
    cf_single,[],
    rf_binary,[128]
)

ILPF_fmd=ITR(
    sf_single_freq,[],
    cf_ILPF,[100],
    rf_pass,[]
)

GLPF_fmd=ITR(
    sf_single_freq,[],
    cf_GLPF,[100],
    rf_pass,[]
)


#######    Iterator : For Histogram   #######



























