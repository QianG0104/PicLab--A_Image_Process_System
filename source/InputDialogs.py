from UI import  *
from Pic import  *

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Resize_Dlg(QWidget):
    def __init__(self,owner,parent=None):
        super(Resize_Dlg,self).__init__(parent)
        self.setWindowTitle('重置图像大小')
        self.owner=owner

        layout = QFormLayout()
        Edit1 = QLineEdit()
        layout.addRow('宽',Edit1)
        Edit2 = QLineEdit()
        layout.addRow('高',Edit2)

        self.Btn_OK=QPushButton('确定')
        self.Btn_OK.clicked.connect(lambda: self.resize_owner_Picture(int(Edit1.text()),int(Edit2.text())))
        self.Btn_Cancel=QPushButton('取消')
        self.Btn_Cancel.clicked.connect(lambda :self.close())
        layout.addRow(self.Btn_OK,self.Btn_Cancel)

        self.setLayout(layout)

    def resize_owner_Picture(self,new_width,new_height):
        self.owner.Picture.Resize(new_width,new_height)
        self.owner.refreshPic()
        self.close()

class Grey_Threshold_Dlg(QWidget):
    def __init__(self,owner,parent=None):
        super(Grey_Threshold_Dlg,self).__init__(parent)
        self.setWindowTitle('设置门限')
        self.owner=owner
        layout = QFormLayout()
        Edit=QLineEdit()
        layout.addRow('阈值',Edit)
        self.Btn_OK=QPushButton('确定')
        self.Btn_OK.clicked.connect(lambda: self.owner_go_on_with_ITR_arg([int(Edit.text())]))
        self.Btn_Cancel=QPushButton('取消')
        self.Btn_Cancel.clicked.connect(lambda :self.close())
        layout.addRow(self.Btn_OK,self.Btn_Cancel)
        self.setLayout(layout)

    def owner_go_on_with_ITR_arg(self,new_args):
        Gray_Diff_Thresh_ITR_fmd.reset_cf_args(new_args)
        self.owner.Picture.Iterate_by(Gray_Diff_Thresh_ITR_fmd)
        self.owner.refreshPic()
        self.close()

class Binary_Threshold_Dlg(QWidget):
    def __init__(self,owner,parent=None):
        super(Binary_Threshold_Dlg,self).__init__(parent)
        self.setWindowTitle('设置门限')
        self.owner=owner
        layout = QFormLayout()
        Edit=QLineEdit()
        layout.addRow('阈值',Edit)
        self.Btn_OK=QPushButton('确定')
        self.Btn_OK.clicked.connect(lambda: self.owner_go_on_with_ITR_arg([int(Edit.text())]))
        self.Btn_Cancel=QPushButton('取消')
        self.Btn_Cancel.clicked.connect(lambda :self.close())
        layout.addRow(self.Btn_OK,self.Btn_Cancel)
        self.setLayout(layout)

    def owner_go_on_with_ITR_arg(self,new_args):
        Binary_fmd.reset_cf_args(new_args)
        self.owner.Picture.Iterate_by(Binary_fmd)
        self.owner.refreshPic()
        self.close()

class Mod_Mask_Dlg(QWidget):
    def __init__(self,owner,parent=None):
        super(Mod_Mask_Dlg,self).__init__(parent)
        self.setWindowTitle('自定义3x3线性算子')
        self.owner=owner
        layout = QFormLayout()

        Scale=QLineEdit()
        Bias=QLineEdit()
        M_00=QLineEdit()
        M_01=QLineEdit()
        M_02=QLineEdit()
        M_10=QLineEdit()
        M_11=QLineEdit()
        M_12=QLineEdit()
        M_20=QLineEdit()
        M_21=QLineEdit()
        M_22=QLineEdit()

        layout.addRow('Scale',Scale)
        layout.addRow('Bias',Bias)
        layout.addRow('Mask[0,0]',M_00)
        layout.addRow('Mask[0,1]',M_01)
        layout.addRow('Mask[0,2]',M_02)
        layout.addRow('Mask[1,0]',M_10)
        layout.addRow('Mask[1,1]',M_11)
        layout.addRow('Mask[1,2]',M_12)
        layout.addRow('Mask[2,0]',M_20)
        layout.addRow('Mask[2,1]',M_21)
        layout.addRow('Mask[2,2]',M_22)

        self.Btn_OK=QPushButton('确定')
        self.Btn_OK.clicked.connect(
            lambda: self.owner_go_on_with_mod_ITR(
                [int(M_00.text()),
                 int(M_01.text()),
                 int(M_02.text()),
                 int(M_10.text()),
                 int(M_11.text()),
                 int(M_12.text()),
                 int(M_20.text()),
                 int(M_21.text()),
                 int(M_22.text())
                 ],
                [float(Scale.text()),
                 float(Bias.text())]
            )
        )
        self.Btn_Cancel=QPushButton('取消')
        self.Btn_Cancel.clicked.connect(lambda :self.close())
        layout.addRow(self.Btn_OK,self.Btn_Cancel)
        self.setLayout(layout)

    def owner_go_on_with_mod_ITR(self,new_sf_args,new_rf_args):
        Mask_fmd.reset_sf_args(new_sf_args)
        Mask_fmd.reset_rf_args(new_rf_args)
        self.owner.Picture.Iterate_by(Mask_fmd)
        self.owner.refreshPic()
        self.close()


class ILPF_Dlg(QWidget):
    def __init__(self, owner, parent=None):
        super(ILPF_Dlg, self).__init__(parent)
        self.setWindowTitle('设置门限')
        self.owner = owner
        layout = QFormLayout()
        Edit = QLineEdit()
        layout.addRow('阈值', Edit)
        self.Btn_OK = QPushButton('确定')
        self.Btn_OK.clicked.connect(lambda: self.owner_go_on_with_ITR_arg([int(Edit.text())]))
        self.Btn_Cancel = QPushButton('取消')
        self.Btn_Cancel.clicked.connect(lambda: self.close())
        layout.addRow(self.Btn_OK, self.Btn_Cancel)
        self.setLayout(layout)

    def owner_go_on_with_ITR_arg(self, new_args):
        ILPF_fmd.reset_cf_args(new_args)
        self.owner.Picture.Freq_Iterate_by(ILPF_fmd)
        self.owner.refreshPic()
        self.close()

class GLPF_Dlg(QWidget):
    def __init__(self, owner, parent=None):
        super(GLPF_Dlg, self).__init__(parent)
        self.setWindowTitle('设置门限')
        self.owner = owner
        layout = QFormLayout()
        Edit = QLineEdit()
        layout.addRow('阈值', Edit)
        self.Btn_OK = QPushButton('确定')
        self.Btn_OK.clicked.connect(lambda: self.owner_go_on_with_ITR_arg([int(Edit.text())]))
        self.Btn_Cancel = QPushButton('取消')
        self.Btn_Cancel.clicked.connect(lambda: self.close())
        layout.addRow(self.Btn_OK, self.Btn_Cancel)
        self.setLayout(layout)

    def owner_go_on_with_ITR_arg(self, new_args):
        GLPF_fmd.reset_cf_args(new_args)
        self.owner.Picture.Freq_Iterate_by(GLPF_fmd)
        self.owner.refreshPic()
        self.close()