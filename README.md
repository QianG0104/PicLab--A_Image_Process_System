# PicLab--A_Image_Process_System

自己编写的一个图像处理系统，可以进行基本的图像处理工作。参考自本科《图像处理》教材。
为了提高系统的可拓展性，我将图像处理的步骤进行了归纳总结，抽象出了一个模块化流程，据此编写了迭代器（Iterator）类，
定义了一系列基本function，通过这些function的搭配组合，既能够方便地对图片的每一个像素进行遍历，又能在遍历的过程兼顾图像整体以进行计算和处理。

