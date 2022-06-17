from PySide6.QtWidgets import QApplication, QMainWindow,QFileDialog,QMessageBox
import Function
import os
import time
from threading import Thread
from UI import Ui_mainWindow
from  Signal import my_signal
# PySide6-uic PicframeUI.ui -o UI.py
# from ui_demo import Ui_Demo


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_mainWindow()  # UI类的实例化()
        self.ui.setupUi(self)
        self.band()
        #检查当前目录下是否有Setting.conf文件，如果没有则创建,并写入字典
        if not os.path.exists("Setting.conf"):
            with open("Setting.conf","w") as f:
                f.write("{'Input_path':'C:/','Output_path':'C:/','font':'','font_color:'','Outquality':'','rename:''}")
        else:
            print("Setting.conf文件已存在")

    def band(self):#绑定槽函数
        # self.ui.___ACTION___.triggered.connect(___FUNCTION___)
        # self.ui.___BUTTON___.clicked.connect(___FUNCTION___)
        # self.ui.___COMBO_BOX___.currentIndexChanged.connect(___FUNCTION___)
        # self.ui.___SPIN_BOX___.valueChanged.connect(___FUNCTION___)
        # 自定义信号.属性名.connect(___FUNCTION___)
        self.ui.Input_Button.clicked.connect(self.Input_msg)
        self.ui.Output_Button.clicked.connect(self.Output_msg)
        self.ui.startButton.clicked.connect(self.start_click)
        my_signal.setmake.connect(self.set_make)
        my_signal.setremain_num.connect(self.set_remain_num)
        my_signal.setmodel.connect(self.set_model)
        my_signal.setProgressBar.connect(self.set_ProgressBar)
        my_signal.setfilename.connect(self.set_filename)
        my_signal.setdetal.connect(self.set_detal)



    def set_remain_num(self,num:str):
        self.ui.remain_num.setText(num)

    def set_make(self,make:str):
        self.ui.make.setText(make)

    def set_ProgressBar(self,progress:int):
        self.ui.progressBar.setValue(progress)

    def set_model(self,model:str):
        self.ui.model.setText(model)

    def set_detal(self,detal:str):
        self.ui.detail_label.setText(detal)

    def set_filename(self,filename:str):
        self.ui.filename.setText(filename)

    def Input_msg(self):
        directory = QFileDialog.getExistingDirectory(None,"选取文件夹","C:/")  # 获取文件夹路径
        self.ui.Input_path.setText(directory)

    def Output_msg(self):
        directory = QFileDialog.getExistingDirectory(None,"选取文件夹","C:/")
        self.ui.Output_path.setText(directory)



    def start_click(self):
        def innerFunc():
            start_time = time.time()
            qlity = int(self.ui.quality.text())
            input_path, output_path = self.ui.Input_path.text(), self.ui.Output_path.text()
            if input_path == "暂未选择导入目录":
                QMessageBox.warning(self, "警告", "请选择输入路径")
            elif output_path == "暂未选择导出目录":
                QMessageBox.warning(self, "警告", "请选择输出路径")
            else:
                file_list = []
                for filename in os.listdir(input_path):
                    if filename[-4:].lower() == ".jpg":
                        file_list.append(filename)
                if len(file_list) == 0:
                    QMessageBox.information(self, "信息", "该目录下没有Jpg图片")
                else:
                    count = 0
                    my_signal.setdetal.emit("开始处理")
                    for filename in file_list:
                        count += 1
                        file_path = input_path + "/" + filename
                        my_signal.setdetal.emit("准备读取{}Exif信息".format(filename))
                        exif_dict = Function.get_exif(file_path)
                        my_signal.setdetal.emit("{}Exif信息读取完毕".format(filename))
                        my_signal.setfilename.emit(filename)
                        my_signal.setremain_num.emit(str(len(file_list) - count))
                        my_signal.setmake.emit(str(exif_dict["品牌"]))
                        my_signal.setmodel.emit(str(exif_dict["型号"]))
                        my_signal.setProgressBar.emit(int(count / len(file_list) * 100))
                        outputname = output_path + "/Blank--" + filename
                        my_signal.setdetal.emit("准备生成")
                        Function.image_borde(exif_dict, qlity, file_path, outputname)
                        my_signal.setdetal.emit("{}图片生成完毕".format(filename))
                    end_time = time.time()
                    QMessageBox.information(self, "信息", "任务完成，{}张图片共花费时间：{:.2f}秒" .format(str(len(file_list)),end_time - start_time))

        task = Thread(target=innerFunc)
        task.start()




if __name__ == '__main__':
    app = QApplication([])  # 启动一个应用
    window = MainWindow()  # 实例化主窗口
    window.show()  # 展示主窗口
    app.exec()  # 避免程序执行到这一行后直接退出