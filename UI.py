# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PicframeUIYdlmXz.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFontComboBox,
    QFrame, QHBoxLayout, QLabel, QLayout,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(730, 626)
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(102, 83, 531, 421))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"MiSans"])
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.Input_path = QLabel(self.widget)
        self.Input_path.setObjectName(u"Input_path")
        self.Input_path.setFont(font)

        self.horizontalLayout.addWidget(self.Input_path)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.Input_Button = QPushButton(self.widget)
        self.Input_Button.setObjectName(u"Input_Button")
        self.Input_Button.setFont(font)

        self.horizontalLayout.addWidget(self.Input_Button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.Output_path = QLabel(self.widget)
        self.Output_path.setObjectName(u"Output_path")

        self.horizontalLayout_2.addWidget(self.Output_path)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.Output_Button = QPushButton(self.widget)
        self.Output_Button.setObjectName(u"Output_Button")
        self.Output_Button.setFont(font)

        self.horizontalLayout_2.addWidget(self.Output_Button)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_8.addWidget(self.label_4)

        self.fontComboBox = QFontComboBox(self.widget)
        self.fontComboBox.setObjectName(u"fontComboBox")

        self.horizontalLayout_8.addWidget(self.fontComboBox)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_8.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_9.addWidget(self.label_7)

        self.doubleSpinBox = QDoubleSpinBox(self.widget)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")

        self.horizontalLayout_9.addWidget(self.doubleSpinBox)

        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_9.addWidget(self.label_9)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_4)

        self.label_13 = QLabel(self.widget)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_9.addWidget(self.label_13)

        self.comboBox = QComboBox(self.widget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_9.addWidget(self.comboBox)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_5)

        self.quality = QSpinBox(self.widget)
        self.quality.setObjectName(u"quality")
        self.quality.setMinimum(40)
        self.quality.setMaximum(100)
        self.quality.setSingleStep(10)
        self.quality.setValue(80)

        self.horizontalLayout_3.addWidget(self.quality)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_11)

        self.renameBox = QComboBox(self.widget)
        self.renameBox.addItem("")
        self.renameBox.addItem("")
        self.renameBox.setObjectName(u"renameBox")
        self.renameBox.setFont(font)

        self.horizontalLayout_3.addWidget(self.renameBox)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)

        self.startButton = QPushButton(self.widget)
        self.startButton.setObjectName(u"startButton")
        font1 = QFont()
        font1.setFamilies([u"MiSans Demibold"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.startButton.setFont(font1)
        self.startButton.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_4.addWidget(self.startButton)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_5.addWidget(self.label_6)

        self.filename = QLabel(self.widget)
        self.filename.setObjectName(u"filename")
        self.filename.setFont(font)

        self.horizontalLayout_5.addWidget(self.filename)

        self.label_12 = QLabel(self.widget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_12)

        self.remain_num = QLabel(self.widget)
        self.remain_num.setObjectName(u"remain_num")
        self.remain_num.setFont(font)

        self.horizontalLayout_5.addWidget(self.remain_num)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.horizontalLayout_6.addWidget(self.label_8)

        self.make = QLabel(self.widget)
        self.make.setObjectName(u"make")
        self.make.setFont(font)

        self.horizontalLayout_6.addWidget(self.make)

        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.horizontalLayout_6.addWidget(self.label_10)

        self.model = QLabel(self.widget)
        self.model.setObjectName(u"model")
        self.model.setFont(font)

        self.horizontalLayout_6.addWidget(self.model)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.detail_label = QLabel(self.widget)
        self.detail_label.setObjectName(u"detail_label")
        self.detail_label.setLayoutDirection(Qt.LeftToRight)
        self.detail_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.detail_label)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_7.addWidget(self.label_3)

        self.progressBar = QProgressBar(self.widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.horizontalLayout_7.addWidget(self.progressBar)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"Picframe", None))
        self.label.setText(QCoreApplication.translate("mainWindow", u"\u5bfc\u5165\u76ee\u5f55\uff1a", None))
        self.Input_path.setText(QCoreApplication.translate("mainWindow", u"\u6682\u672a\u9009\u62e9\u5bfc\u5165\u76ee\u5f55", None))
        self.Input_Button.setText(QCoreApplication.translate("mainWindow", u"\u9009\u62e9", None))
        self.label_2.setText(QCoreApplication.translate("mainWindow", u"\u5bfc\u51fa\u76ee\u5f55\uff1a", None))
        self.Output_path.setText(QCoreApplication.translate("mainWindow", u"\u6682\u672a\u9009\u62e9\u5bfc\u51fa\u76ee\u5f55", None))
        self.Output_Button.setText(QCoreApplication.translate("mainWindow", u"\u9009\u62e9", None))
        self.label_4.setText(QCoreApplication.translate("mainWindow", u"\u5b57\u4f53\u8bbe\u7f6e\uff1a", None))
        self.pushButton.setText(QCoreApplication.translate("mainWindow", u"\u9009\u62e9\u5b57\u4f53", None))
        self.label_7.setText(QCoreApplication.translate("mainWindow", u"\u5b57\u4f53\u7f29\u653e\uff1a", None))
        self.label_9.setText(QCoreApplication.translate("mainWindow", u"\u500d", None))
        self.label_13.setText(QCoreApplication.translate("mainWindow", u"\u5b57\u4f53\u989c\u8272\uff1a", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("mainWindow", u"\u9ed1\u8272", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("mainWindow", u"\u7ea2\u8272", None))

        self.label_5.setText(QCoreApplication.translate("mainWindow", u"\u8f93\u51fa\u8d28\u91cf\uff1a", None))
        self.label_11.setText(QCoreApplication.translate("mainWindow", u"\u547d\u540d\u65b9\u5f0f\uff1a", None))
        self.renameBox.setItemText(0, QCoreApplication.translate("mainWindow", u"Blank+\u539f\u6587\u4ef6\u540d", None))
        self.renameBox.setItemText(1, QCoreApplication.translate("mainWindow", u"\u5e8f\u5217\u53f7", None))

        self.startButton.setText(QCoreApplication.translate("mainWindow", u"\u5f00\u59cb", None))
        self.label_6.setText(QCoreApplication.translate("mainWindow", u"\u6b63\u5728\u5904\u7406\uff1a", None))
        self.filename.setText("")
        self.label_12.setText(QCoreApplication.translate("mainWindow", u"\u5269\u4f59\u6570\u76ee\uff1a", None))
        self.remain_num.setText("")
        self.label_8.setText(QCoreApplication.translate("mainWindow", u"\u5236\u9020\u5546\uff1a", None))
        self.make.setText("")
        self.label_10.setText(QCoreApplication.translate("mainWindow", u"\u76f8\u673a\u578b\u53f7\uff1a", None))
        self.model.setText("")
        self.detail_label.setText(QCoreApplication.translate("mainWindow", u"\u5904\u7406\u8be6\u60c5", None))
        self.label_3.setText(QCoreApplication.translate("mainWindow", u"\u8fdb\u5ea6\uff1a", None))
    # retranslateUi

