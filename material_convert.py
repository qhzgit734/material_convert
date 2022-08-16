import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

'''Ui_main为.ui文件转换.py的文件名，Ui_Form为.ui文件中class名(QWidget作为基类对应的class名),
QWidget为基类:Ui_Form(),MainWindow为基类:Ui_MainWindow()
'''
from qt_for_python.uic import main, window_1, window_2, window_3, window_4, window_5, window_6, window_7, \
    window_8, window_9, window_10, window_11, window_12, window_13

# 全局变量
tie = 7850
a = float()
b = float()
c = float()
d = float()
e = float()
jz1 = float()
jz = float()
xs = float()
res = float()
sender = str()
# 槽钢
dict1 = {'10#': 10.077}
# 镀锌钢管
dict2 = {'15': 1.357, '20': 1.76, '25': 2.554, '32': 3.56, '40': 4.1, '50': 5.607, '65': 7.536, '80': 8.88, '100': 11.53,
         '125': 15.942, '150': 19.27, '200': 36.12, '250': 40.7, '300': 47.86, '600': 131}
# 焊接(厚壁)钢管
dict3 = {'15': 1.26, '20': 1.63, '25': 2.42, '32': 3.13, '40': 3.84, '50': 4.88, '65': 6.64, '80': 8.34, '100': 10.85,
         '125': 14, '150': 17.81, '200': 30.53}
# 不锈钢管
dict4 = {'15': 2.58, '20': 3.34, '25': 4.85, '32': 6.76, '40': 7.79, '50': 10.65, '65': 14.32, '80': 16.87, '100': 21.91,
         '125': 30.29, '150': 36.61, '200': 68.63, '250': 77.33, '300': 90.93, '600': 248.9}
# 类-输入
class Var_in:
    def get_ent(self, widget_v):
        global a, b, c, d, e
        var_ui = widget_v.win_ui
        if len(var_ui.lineEdit_A.text()) != 0 and len(var_ui.lineEdit_B.text()) != 0 and \
            var_ui.lineEdit_C.isEnabled() == False and len(var_ui.lineEdit_D.text()) != 0:
            a = float(var_ui.lineEdit_A.text())
            b = float(var_ui.lineEdit_B.text())
            d = float(var_ui.lineEdit_D.text())
        elif len(var_ui.lineEdit_A.text()) != 0 and var_ui.lineEdit_B.isEnabled() == False and \
            var_ui.lineEdit_C.isEnabled() == False and len(var_ui.lineEdit_D.text()) != 0:
            a = float(var_ui.lineEdit_A.text())
            d = float(var_ui.lineEdit_D.text())
        elif len(var_ui.lineEdit_A.text()) != 0 and len(var_ui.lineEdit_B.text()) != 0 and \
            len(var_ui.lineEdit_C.text()) != 0 and len(var_ui.lineEdit_D.text()) != 0:
            a = float(var_ui.lineEdit_A.text())
            b = float(var_ui.lineEdit_B.text())
            c = float(var_ui.lineEdit_C.text())
            d = float(var_ui.lineEdit_D.text())
        else:
            QMessageBox.information(widget_v, '提示', '请填写完整信息！')
    def get_ent1(self, widget_v):
        global a, b, c, d, e
        var_ui = widget_v.win_ui
        if len(var_ui.lineEdit_A.text()) != 0 and len(var_ui.lineEdit_B.text()) != 0 and \
            len(var_ui.lineEdit_C.text()) != 0 and len(var_ui.lineEdit_D.text()) != 0 and len(var_ui.lineEdit_E.text()) != 0:
            a = float(var_ui.lineEdit_A.text())
            b = float(var_ui.lineEdit_B.text())
            c = float(var_ui.lineEdit_C.text())
            d = float(var_ui.lineEdit_D.text())
            e = float(var_ui.lineEdit_E.text())
        else:
            QMessageBox.information(widget_v, '提示', '请填写完整信息！')
            
    def get_cbx1(self, widget_v):
        global a, d
        var_ui = widget_v.win_ui
        a = float(var_ui.comboBox.currentText())
        if len(var_ui.lineEdit_D.text()) != 0:
            d = float(var_ui.lineEdit_D.text())
        else:
            QMessageBox.information(widget_v, '提示', '请填写完整信息！')
            
    def get_cbx2(self, widget_v, dict_v):
        global xs, d
        var_ui = widget_v.win_ui
        if len(var_ui.lineEdit_D.text()) != 0:
            d = float(var_ui.lineEdit_D.text())
        else:
            QMessageBox.information(widget_v, '提示', '请填写完整信息！')
        xs = dict_v.get(var_ui.comboBox.currentText())
# 类-换算
class Convert:
    def cal_jz(sefl, widget_v):
        global jz1, jz
        cal_ui = widget_v.win_ui
        if cal_ui.comboBox_1.currentText() == '风管防火阀':
            if a * b / 10**6 <= 1:
                jz1 = round(((a * b / 10**6) * 1290 + 200) / 1.13, 2)
            else:
                jz1 = round(((a * b / 10 ** 6) * 1110 + 230) / 1.13, 2)
        elif cal_ui.comboBox_1.currentText() == '风管排烟阀':
            if a * b / 10**6 <= 1:
                jz1 = round(((a * b / 10**6) * 1350 + 385) / 1.13, 2)
            else:
                jz1 = round(((a * b / 10 ** 6) * 1255 + 430) / 1.13, 2)
        elif cal_ui.comboBox_1.currentText() == '风管止回阀':
            jz1 = round(((a * b / 10**6) * 740 + 135) / 1.13, 2)
        elif cal_ui.comboBox_1.currentText() == '风管调节阀-对开多叶':
            jz1 = round(((a * b / 10**6) * 355 + 55) / 1.13, 2)
        elif cal_ui.comboBox_1.currentText() == '风管插板（密闭）阀':
            jz1 = round((a + b) * 2 / 1000 * 240 * 0.6 / 1.13, 2)
        elif cal_ui.comboBox_1.currentText() == '风口-单层':
            jz1 = round(((a * b / 10**6) * 485 + 60) / 1.13, 2)
        elif cal_ui.comboBox_1.currentText() == '风口-双层':
            jz1 = round(((a * b / 10**6) * 540 + 75) / 1.13, 2)
        elif cal_ui.comboBox_1.currentText() == '风口-排烟':
            jz1 = round(((a / 10**3) * (b / 10**3 + 0.2) * 1695 + 575) / 1.13, 2)
        elif cal_ui.comboBox_1.currentText() == '风口-防火':
            jz1 = round(((a / 10**3) * (b / 10**3 + 0.2) * 790 + 520) / 1.13, 2)
        elif cal_ui.comboBox_1.currentText() == '风口-防雨':
            jz1 = round(((a * b / 10**6) * 560 + 60) / 1.13, 2)
        elif cal_ui.comboBox_1.currentText() == '消声弯头':
            jz1 = round((a * b + a * (a + 250) + b * (a + 250)) / 10**6 * 2 * 200 / 1.13, 2)
        elif cal_ui.comboBox_1.currentText() == '静压箱':
            jz1 = round((a + b) * 2 * c / 10**6 * 46.66, 2)
        elif cal_ui.comboBox_1.currentText() == '静压箱-消声':
            jz1 = round((a * b + a * c + b * c) / 10**6 * 2 * 395 / 1.13, 2)
        elif cal_ui.comboBox_1.currentText() == '消声器ZP100':
            jz1 = round((a * b + a * c + b * c) / 10**6 * 2 * 655 / 1.13, 2)
        else:
            pass
        if cal_ui.buttonGroup.checkedButton().text() == '电动':
            jz = round(jz1 + 400, 2)
        elif cal_ui.buttonGroup.checkedButton().text() == '温控':
            jz = round(jz1 + 700, 2)
        elif cal_ui.buttonGroup.checkedButton().text() == '遥控':
            jz = round(jz1 + 1000, 2)
        else:
            jz = jz1
            
    def cal_xs(self, widget_v):
        global xs
        cal_title = widget_v.win.windowTitle()
        cal_ui = widget_v.win_ui
        if cal_title == '镀锌钢板':
            xs = round(a * b * c / 10**9 * tie, 3)
        elif cal_title == '镀锌薄钢板':
            xs = round(a / 10**3 * tie, 3)
        elif cal_title == '角钢':
            xs = round(c * (a + b - c) / 10**6 * tie, 3)
        elif cal_title == '槽钢':
            pass
        elif cal_title == '镀锌圆钢':
            xs = round((a / 2 / 10**3) ** 2 * 3.14 * tie, 3)
        elif cal_title == '镀锌扁钢':
            xs = round(a * b * 1000 / 10**9 * tie, 3)
        elif cal_title == '镀锌钢管':
            pass
        elif cal_title == '焊接钢管':
            pass
        elif cal_title == '不锈钢管':
            pass
        elif cal_title == '风管附件':
            if cal_ui.comboBox_2.currentText() == '镀锌钢板':
                if cal_ui.checkBox.isChecked() == True and cal_ui.checkBox_2.isChecked() == False:
                    xs = round((1 + 0.03 * (d - 6.2) / 0.3) * 1.15, 3)
                elif cal_ui.checkBox.isChecked() == True and cal_ui.checkBox_2.isChecked() == True:
                    xs = round((1 + 0.03 * (d - 6.2) / 0.3) * 1.15 * 4, 3)
                elif cal_ui.checkBox.isChecked() == False and cal_ui.checkBox_2.isChecked() == True:
                    xs = round((1 + 0.03 * (d - 6.2) / 0.3) * 4, 3)
                else:
                    xs = round(1 + 0.03 * (d - 6.2) / 0.3, 3)
            else:
                if cal_ui.checkBox.isChecked() == True and cal_ui.checkBox_2.isChecked() == False:
                    xs = round((1 + 0.05 * (d - 22) / 1.5) * 1.15, 3)
                elif cal_ui.checkBox.isChecked() == True and cal_ui.checkBox_2.isChecked() == True:
                    xs = round((1 + 0.05 * (d - 22) / 1.5) * 1.15 * 4, 3)
                elif cal_ui.checkBox.isChecked() == False and cal_ui.checkBox_2.isChecked() == True:
                    xs = round((1 + 0.05 * (d - 22) / 1.5) * 4, 3)
                else:
                    xs = round(1 + 0.05 * (d - 22) / 1.5, 3)
        elif cal_title == '桥架':
            xs = round((c + e * 2) / (a + b * 2), 3)
        else:
            pass
    
    def cal_res(self, widget_v):
        global res
        cal_title = widget_v.win.windowTitle()
        if cal_title in ['镀锌钢板', '镀锌薄钢板', '角钢', '槽钢', '镀锌钢管', '焊接钢管', '不锈钢管', '桥架']:
            res = round(xs * d, 2)
        elif cal_title in ['镀锌圆钢', '镀锌扁钢']:
            res = round(d / xs, 2)
        elif cal_title == '风管附件':
            res = round(xs * jz, 2)
        else:
            pass
# 类-主窗口
class Creat_root(QMainWindow):
    def __init__(self, Ui_file):
        super().__init__()
        # 创建主窗口
        self.root = QMainWindow()
        # 创建Ui_MainWindow的实例
        self.root_ui = Ui_file.Ui_MainWindow()
        # 调用setupUi在指定窗口(主窗口)中添加控件
        self.root_ui.setupUi(self.root)
        # 创建子窗口信号、槽
        self.root_ui.pushButton_1.clicked.connect(self.open_win_t)
        self.root_ui.pushButton_2.clicked.connect(self.open_win_t)
        self.root_ui.pushButton_3.clicked.connect(self.open_win_t)
        self.root_ui.pushButton_4.clicked.connect(self.open_win_t)
        self.root_ui.pushButton_5.clicked.connect(self.open_win_t)
        self.root_ui.pushButton_6.clicked.connect(self.open_win_t)
        self.root_ui.pushButton_7.clicked.connect(self.open_win_t)
        self.root_ui.pushButton_8.clicked.connect(self.open_win_t)
        self.root_ui.pushButton_9.clicked.connect(self.open_win_t)
        self.root_ui.pushButton_10.clicked.connect(self.open_win_t)
        self.root_ui.pushButton_11.clicked.connect(self.open_win_t)
        # self.root_ui.pushButton_12.clicked.connect(self.open_win_t)
        self.root_ui.pushButton_1.clicked.connect(lambda: self.open_win(widget1))
        self.root_ui.pushButton_2.clicked.connect(lambda: self.open_win(widget2))
        self.root_ui.pushButton_3.clicked.connect(lambda: self.open_win(widget3))
        self.root_ui.pushButton_4.clicked.connect(lambda: self.open_win(widget4))
        self.root_ui.pushButton_5.clicked.connect(lambda: self.open_win(widget5))
        self.root_ui.pushButton_6.clicked.connect(lambda: self.open_win(widget6))
        self.root_ui.pushButton_7.clicked.connect(lambda: self.open_win(widget7))
        self.root_ui.pushButton_8.clicked.connect(lambda: self.open_win(widget8))
        self.root_ui.pushButton_9.clicked.connect(lambda: self.open_win(widget9))
        self.root_ui.pushButton_10.clicked.connect(lambda: self.open_win(widget10))
        self.root_ui.pushButton_11.clicked.connect(lambda: self.open_win(widget11))
        # self.root_ui.pushButton_12.clicked.connect(lambda: self.open_win(widget11))
        self.root_ui.action.triggered.connect(lambda: self.open_win_a(dialog_v))
        self.root_ui.actionhelp.triggered.connect(lambda: self.open_win_a(dialog_h))
        
    def open_win(self, widget_o):
        global sender
        widget_o.win.setWindowTitle(sender)
        # 新窗口
        widget_o.win.show()
     
    def open_win_a(self, widget_o):
        # 新窗口
        widget_o.win.show()
            
    def open_win_t(self):
        global sender
        sender = self.sender().text()
# 类-镀锌钢板
class Creat_win1(QWidget):
    def __init__(self, Ui_file):
        super().__init__()
        self.win = QWidget()
        self.win_ui = Ui_file.Ui_Form()
        self.win_ui.setupUi(self.win)
        self.win_ui.pushButton.clicked.connect(lambda: self.func1(widget1))
        
    def func1(self, widget_f):
        self.var_f = Var_in()
        self.cvt1 = Convert()
        self.var_f.get_ent(widget_f)
        self.cvt1.cal_xs(widget_f)
        self.cvt1.cal_res(widget_f)
        self.win_ui.label_XS_var.setText(str(xs))
        self.win_ui.lineEdit_RES.setText(str(res))
# 类-镀锌薄钢板
class Creat_win2(QWidget):
    def __init__(self, Ui_file):
        super().__init__()
        self.win = QWidget()
        self.win_ui = Ui_file.Ui_Form()
        self.win_ui.setupUi(self.win)
        self.win_ui.pushButton.clicked.connect(lambda: self.func1(widget2))
        
    def func1(self, widget_f):
        self.var_f = Var_in()
        self.cvt1 = Convert()
        self.var_f.get_cbx1(widget_f)
        self.cvt1.cal_xs(widget_f)
        self.cvt1.cal_res(widget_f)
        self.win_ui.label_XS_var.setText(str(xs))
        self.win_ui.lineEdit_RES.setText(str(res))
# 类-角钢
class Creat_win3(QWidget):
    def __init__(self, Ui_file):
        super().__init__()
        self.win = QWidget()
        self.win_ui = Ui_file.Ui_Form()
        self.win_ui.setupUi(self.win)
        self.win_ui.pushButton.clicked.connect(lambda: self.func1(widget3))
        
    def func1(self, widget_f):
        self.var_f = Var_in()
        self.cvt1 = Convert()
        self.var_f.get_ent(widget_f)
        self.cvt1.cal_xs(widget_f)
        self.cvt1.cal_res(widget_f)
        self.win_ui.label_XS_var.setText(str(xs))
        self.win_ui.lineEdit_RES.setText(str(res))
# 类-槽钢
class Creat_win4(QWidget):
    def __init__(self, Ui_file):
        super().__init__()
        self.win = QWidget()
        self.win_ui = Ui_file.Ui_Form()
        self.win_ui.setupUi(self.win)
        self.win_ui.pushButton.clicked.connect(lambda: self.func1(widget4))
        
    def func1(self, widget_f):
        self.var_f = Var_in()
        self.cvt1 = Convert()
        self.var_f.get_cbx2(widget_f, dict1)
        self.cvt1.cal_res(widget_f)
        self.win_ui.label_XS_var.setText(str(xs))
        self.win_ui.lineEdit_RES.setText(str(res))
# 类-镀锌圆钢
class Creat_win5(QWidget):
    def __init__(self, Ui_file):
        super().__init__()
        self.win = QWidget()
        self.win_ui = Ui_file.Ui_Form()
        self.win_ui.setupUi(self.win)
        self.win_ui.pushButton.clicked.connect(lambda: self.func1(widget5))
        
    def func1(self, widget_f):
        self.var_f = Var_in()
        self.cvt1 = Convert()
        self.var_f.get_ent(widget_f)
        self.cvt1.cal_xs(widget_f)
        self.cvt1.cal_res(widget_f)
        self.win_ui.label_XS_var.setText(str(xs))
        self.win_ui.lineEdit_RES.setText(str(res))
# 类-镀锌扁钢
class Creat_win6(QWidget):
    def __init__(self, Ui_file):
        super().__init__()
        self.win = QWidget()
        self.win_ui = Ui_file.Ui_Form()
        self.win_ui.setupUi(self.win)
        self.win_ui.pushButton.clicked.connect(lambda: self.func1(widget6))
        
    def func1(self, widget_f):
        self.var_f = Var_in()
        self.cvt1 = Convert()
        self.var_f.get_ent(widget_f)
        self.cvt1.cal_xs(widget_f)
        self.cvt1.cal_res(widget_f)
        self.win_ui.label_XS_var.setText(str(xs))
        self.win_ui.lineEdit_RES.setText(str(res))
# 类-镀锌钢管
class Creat_win7(QWidget):
    def __init__(self, Ui_file):
        super().__init__()
        self.win = QWidget()
        self.win_ui = Ui_file.Ui_Form()
        self.win_ui.setupUi(self.win)
        self.win_ui.pushButton.clicked.connect(lambda: self.func1(widget7))
        
    def func1(self, widget_f):
        self.var_f = Var_in()
        self.cvt1 = Convert()
        self.var_f.get_cbx2(widget_f, dict2)
        self.cvt1.cal_res(widget_f)
        self.win_ui.label_XS_var.setText(str(xs))
        self.win_ui.lineEdit_RES.setText(str(res))
# 类-焊接钢管
class Creat_win8(QWidget):
    def __init__(self, Ui_file):
        super().__init__()
        self.win = QWidget()
        self.win_ui = Ui_file.Ui_Form()
        self.win_ui.setupUi(self.win)
        self.win_ui.pushButton.clicked.connect(lambda: self.func1(widget8))
        
    def func1(self, widget_f):
        self.var_f = Var_in()
        self.cvt1 = Convert()
        self.var_f.get_cbx2(widget_f, dict3)
        self.cvt1.cal_res(widget_f)
        self.win_ui.label_XS_var.setText(str(xs))
        self.win_ui.lineEdit_RES.setText(str(res))
# 类-不锈钢管
class Creat_win9(QWidget):
    def __init__(self, Ui_file):
        super().__init__()
        self.win = QWidget()
        self.win_ui = Ui_file.Ui_Form()
        self.win_ui.setupUi(self.win)
        self.win_ui.pushButton.clicked.connect(lambda: self.func1(widget9))
        
    def func1(self, widget_f):
        self.var_f = Var_in()
        self.cvt1 = Convert()
        self.var_f.get_cbx2(widget_f, dict4)
        self.cvt1.cal_res(widget_f)
        self.win_ui.label_XS_var.setText(str(xs))
        self.win_ui.lineEdit_RES.setText(str(res))
# 类-风管附件
class Creat_win10(QWidget):
    def __init__(self, Ui_file):
        super().__init__()
        self.win = QWidget()
        self.win_ui = Ui_file.Ui_Form()
        self.win_ui.setupUi(self.win)
        self.win_ui.pushButton.clicked.connect(lambda: self.func1(widget10))
        self.win_ui.comboBox_1.currentIndexChanged.connect(self.state1)
    
    def state1(self):
        if self.win_ui.comboBox_1.currentText() not in ['静压箱', '静压箱-消声', '消声器ZP100']:
            self.win_ui.lineEdit_C.setEnabled(False)
        elif self.win_ui.comboBox_1.currentText() in ['静压箱', '静压箱-消声', '消声器ZP100']:
            self.win_ui.lineEdit_C.setEnabled(True)
        else:
            pass
        
    def func1(self, widget_f):
        self.var_f = Var_in()
        self.cvt1 = Convert()
        self.var_f.get_ent(widget_f)
        self.cvt1.cal_jz(widget_f)
        self.cvt1.cal_xs(widget_f)
        self.cvt1.cal_res(widget_f)
        self.win_ui.label_JZ_var.setText(str(jz))
        self.win_ui.label_XS_var.setText(str(xs))
        self.win_ui.lineEdit_RES.setText(str(res))
# 类-桥架
class Creat_win11(QWidget):
    def __init__(self, Ui_file):
        super().__init__()
        self.win = QWidget()
        self.win_ui = Ui_file.Ui_widget()
        self.win_ui.setupUi(self.win)
        self.win_ui.pushButton.clicked.connect(lambda: self.func1(widget11))
        
    def func1(self, widget_f):
        self.var_f = Var_in()
        self.cvt1 = Convert()
        self.var_f.get_ent1(widget_f)
        self.cvt1.cal_xs(widget_f)
        self.cvt1.cal_res(widget_f)
        self.win_ui.lineEdit_RES.setText(str(res))
# 类-版本
class Creat_win12(QDialog):
    def __init__(self, Ui_file):
        super().__init__()
        self.win = QDialog()
        self.win_ui = Ui_file.Ui_Dialog()
        self.win_ui.setupUi(self.win)
        self.win_ui.commandLinkButton.clicked.connect(self.open_git)
    
    def open_git(self):
        QDesktopServices.openUrl(QUrl("https://github.com/qhzgit734/py_material_convert.git"))
        
if __name__ == '__main__':
    # QApplication类的实例
    app = QApplication(sys.argv)
    # 窗口实例
    mainwindow = Creat_root(main)
    widget1 = Creat_win1(window_1)
    widget2 = Creat_win2(window_2)
    widget3 = Creat_win3(window_3)
    widget4 = Creat_win4(window_4)
    widget5 = Creat_win5(window_5)
    widget6 = Creat_win6(window_6)
    widget7 = Creat_win7(window_7)
    widget8 = Creat_win8(window_8)
    widget9 = Creat_win9(window_9)
    widget10 = Creat_win10(window_10)
    widget11 = Creat_win11(window_11)
    dialog_v = Creat_win12(window_12)
    dialog_h = Creat_win12(window_13)
    # 窗口显示
    mainwindow.root.show()
    app.setWindowIcon(QIcon('logo.ico'))
    # 进入程序的主循环，并通过exit函数确保主循环安全结束
    sys.exit(app.exec_())
    # pyinstaller -F -w material_convert.py -i 'logo.ico'