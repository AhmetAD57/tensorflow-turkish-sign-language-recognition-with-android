# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tasarim.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1045, 579)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1031, 521))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.pushButton = QtWidgets.QPushButton(self.tab_3)
        self.pushButton.setGeometry(QtCore.QRect(30, 20, 111, 31))
        self.pushButton.setObjectName("pushButton")
        self.groupBox = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox.setGeometry(QtCore.QRect(220, 10, 201, 81))
        self.groupBox.setObjectName("groupBox")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 30, 141, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 150, 401, 121))
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(190, 30, 181, 80))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(110, 20, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(110, 50, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 81, 23))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(20, 50, 91, 21))
        self.label_4.setObjectName("label_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 72, 111, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 30, 120, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.spinBox = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(100)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_4.setGeometry(QtCore.QRect(560, 10, 381, 131))
        self.groupBox_4.setObjectName("groupBox_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_4.setEnabled(False)
        self.pushButton_4.setGeometry(QtCore.QRect(120, 20, 141, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_23 = QtWidgets.QLabel(self.groupBox_4)
        self.label_23.setGeometry(QtCore.QRect(30, 80, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.groupBox_4)
        self.label_24.setGeometry(QtCore.QRect(130, 80, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("color: \"green\"")
        self.label_24.setObjectName("label_24")
        self.groupBox_12 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_12.setGeometry(QtCore.QRect(30, 420, 971, 71))
        self.groupBox_12.setObjectName("groupBox_12")
        self.label_26 = QtWidgets.QLabel(self.groupBox_12)
        self.label_26.setGeometry(QtCore.QRect(30, 20, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.groupBox_12)
        self.label_27.setGeometry(QtCore.QRect(30, 40, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.groupBox_13 = QtWidgets.QGroupBox(self.groupBox_12)
        self.groupBox_13.setGeometry(QtCore.QRect(440, 10, 501, 51))
        self.groupBox_13.setObjectName("groupBox_13")
        self.label_28 = QtWidgets.QLabel(self.groupBox_13)
        self.label_28.setGeometry(QtCore.QRect(20, 20, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.groupBox_13)
        self.label_29.setGeometry(QtCore.QRect(240, 10, 251, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("color:\"green\"")
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.groupBox_13)
        self.label_30.setGeometry(QtCore.QRect(240, 30, 251, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("color:\"blue\"")
        self.label_30.setObjectName("label_30")
        self.label_50 = QtWidgets.QLabel(self.groupBox_12)
        self.label_50.setGeometry(QtCore.QRect(200, 30, 201, 16))
        self.label_50.setStyleSheet("color: green")
        self.label_50.setObjectName("label_50")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(80, 30, 111, 20))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 51, 20))
        self.label_2.setObjectName("label_2")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_5.setGeometry(QtCore.QRect(30, 80, 301, 141))
        self.groupBox_5.setObjectName("groupBox_5")
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_6.setEnabled(False)
        self.groupBox_6.setGeometry(QtCore.QRect(20, 50, 131, 80))
        self.groupBox_6.setObjectName("groupBox_6")
        self.label_5 = QtWidgets.QLabel(self.groupBox_6)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 41, 16))
        self.label_5.setObjectName("label_5")
        self.spinBox_2 = QtWidgets.QSpinBox(self.groupBox_6)
        self.spinBox_2.setGeometry(QtCore.QRect(80, 20, 42, 22))
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(150)
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_3 = QtWidgets.QSpinBox(self.groupBox_6)
        self.spinBox_3.setGeometry(QtCore.QRect(80, 50, 42, 22))
        self.spinBox_3.setMinimum(1)
        self.spinBox_3.setMaximum(150)
        self.spinBox_3.setObjectName("spinBox_3")
        self.label_8 = QtWidgets.QLabel(self.groupBox_6)
        self.label_8.setGeometry(QtCore.QRect(10, 50, 61, 16))
        self.label_8.setObjectName("label_8")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton.setGeometry(QtCore.QRect(20, 20, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_2.setGeometry(QtCore.QRect(170, 20, 101, 17))
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_7.setGeometry(QtCore.QRect(170, 50, 111, 80))
        self.groupBox_7.setObjectName("groupBox_7")
        self.label_9 = QtWidgets.QLabel(self.groupBox_7)
        self.label_9.setGeometry(QtCore.QRect(10, 20, 61, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_7)
        self.label_10.setGeometry(QtCore.QRect(10, 50, 71, 16))
        self.label_10.setObjectName("label_10")
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_8.setEnabled(False)
        self.groupBox_8.setGeometry(QtCore.QRect(30, 240, 301, 171))
        self.groupBox_8.setObjectName("groupBox_8")
        self.groupBox_9 = QtWidgets.QGroupBox(self.groupBox_8)
        self.groupBox_9.setEnabled(False)
        self.groupBox_9.setGeometry(QtCore.QRect(20, 80, 131, 80))
        self.groupBox_9.setObjectName("groupBox_9")
        self.label_11 = QtWidgets.QLabel(self.groupBox_9)
        self.label_11.setGeometry(QtCore.QRect(10, 20, 41, 16))
        self.label_11.setObjectName("label_11")
        self.spinBox_4 = QtWidgets.QSpinBox(self.groupBox_9)
        self.spinBox_4.setGeometry(QtCore.QRect(80, 20, 42, 22))
        self.spinBox_4.setMinimum(1)
        self.spinBox_4.setMaximum(150)
        self.spinBox_4.setObjectName("spinBox_4")
        self.spinBox_5 = QtWidgets.QSpinBox(self.groupBox_9)
        self.spinBox_5.setGeometry(QtCore.QRect(80, 50, 42, 22))
        self.spinBox_5.setMinimum(1)
        self.spinBox_5.setMaximum(150)
        self.spinBox_5.setObjectName("spinBox_5")
        self.label_12 = QtWidgets.QLabel(self.groupBox_9)
        self.label_12.setGeometry(QtCore.QRect(10, 50, 61, 16))
        self.label_12.setObjectName("label_12")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_8)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 50, 82, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_8)
        self.radioButton_4.setGeometry(QtCore.QRect(170, 50, 101, 17))
        self.radioButton_4.setChecked(True)
        self.radioButton_4.setObjectName("radioButton_4")
        self.groupBox_10 = QtWidgets.QGroupBox(self.groupBox_8)
        self.groupBox_10.setGeometry(QtCore.QRect(170, 80, 111, 80))
        self.groupBox_10.setObjectName("groupBox_10")
        self.label_13 = QtWidgets.QLabel(self.groupBox_10)
        self.label_13.setGeometry(QtCore.QRect(10, 20, 61, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox_10)
        self.label_14.setGeometry(QtCore.QRect(10, 50, 71, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.groupBox_8)
        self.label_15.setGeometry(QtCore.QRect(20, 20, 41, 16))
        self.label_15.setObjectName("label_15")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_8)
        self.comboBox_2.setGeometry(QtCore.QRect(60, 20, 91, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.groupBox_11 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_11.setGeometry(QtCore.QRect(350, 10, 651, 51))
        self.groupBox_11.setObjectName("groupBox_11")
        self.label_16 = QtWidgets.QLabel(self.groupBox_11)
        self.label_16.setGeometry(QtCore.QRect(20, 20, 201, 16))
        self.label_16.setObjectName("label_16")
        self.label_19 = QtWidgets.QLabel(self.groupBox_11)
        self.label_19.setGeometry(QtCore.QRect(230, 20, 61, 16))
        self.label_19.setObjectName("label_19")
        self.label_21 = QtWidgets.QLabel(self.groupBox_11)
        self.label_21.setGeometry(QtCore.QRect(300, 20, 81, 16))
        self.label_21.setObjectName("label_21")
        self.label_17 = QtWidgets.QLabel(self.groupBox_11)
        self.label_17.setGeometry(QtCore.QRect(400, 20, 241, 16))
        self.label_17.setObjectName("label_17")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab)
        self.pushButton_5.setEnabled(False)
        self.pushButton_5.setGeometry(QtCore.QRect(760, 240, 201, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.groupBox_16 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_16.setGeometry(QtCore.QRect(30, 420, 971, 71))
        self.groupBox_16.setObjectName("groupBox_16")
        self.label_37 = QtWidgets.QLabel(self.groupBox_16)
        self.label_37.setGeometry(QtCore.QRect(30, 20, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.groupBox_16)
        self.label_38.setGeometry(QtCore.QRect(30, 40, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_38.setFont(font)
        self.label_38.setObjectName("label_38")
        self.groupBox_17 = QtWidgets.QGroupBox(self.groupBox_16)
        self.groupBox_17.setGeometry(QtCore.QRect(440, 10, 501, 51))
        self.groupBox_17.setObjectName("groupBox_17")
        self.label_39 = QtWidgets.QLabel(self.groupBox_17)
        self.label_39.setGeometry(QtCore.QRect(20, 20, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self.groupBox_17)
        self.label_40.setGeometry(QtCore.QRect(240, 10, 251, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_40.setFont(font)
        self.label_40.setStyleSheet("color:\"green\"")
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(self.groupBox_17)
        self.label_41.setGeometry(QtCore.QRect(240, 30, 251, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_41.setFont(font)
        self.label_41.setStyleSheet("color:\"blue\"")
        self.label_41.setObjectName("label_41")
        self.label_52 = QtWidgets.QLabel(self.groupBox_16)
        self.label_52.setGeometry(QtCore.QRect(200, 30, 201, 16))
        self.label_52.setStyleSheet("color: green")
        self.label_52.setObjectName("label_52")
        self.groupBox_20 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_20.setGeometry(QtCore.QRect(350, 220, 331, 61))
        self.groupBox_20.setObjectName("groupBox_20")
        self.label_25 = QtWidgets.QLabel(self.groupBox_20)
        self.label_25.setGeometry(QtCore.QRect(20, 20, 51, 16))
        self.label_25.setObjectName("label_25")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_20)
        self.lineEdit.setGeometry(QtCore.QRect(50, 20, 131, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_20)
        self.pushButton_9.setGeometry(QtCore.QRect(230, 20, 75, 23))
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_46 = QtWidgets.QLabel(self.tab)
        self.label_46.setGeometry(QtCore.QRect(370, 380, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_46.setFont(font)
        self.label_46.setObjectName("label_46")
        self.label_47 = QtWidgets.QLabel(self.tab)
        self.label_47.setGeometry(QtCore.QRect(470, 380, 281, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_47.setFont(font)
        self.label_47.setStyleSheet("color:\"green\"")
        self.label_47.setObjectName("label_47")
        self.groupBox_22 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_22.setGeometry(QtCore.QRect(350, 70, 471, 121))
        self.groupBox_22.setObjectName("groupBox_22")
        self.groupBox_21 = QtWidgets.QGroupBox(self.groupBox_22)
        self.groupBox_21.setGeometry(QtCore.QRect(20, 20, 291, 81))
        self.groupBox_21.setObjectName("groupBox_21")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_21)
        self.checkBox.setGeometry(QtCore.QRect(20, 20, 70, 17))
        self.checkBox.setObjectName("checkBox")
        self.widget = QtWidgets.QWidget(self.groupBox_21)
        self.widget.setGeometry(QtCore.QRect(20, 40, 233, 22))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_20 = QtWidgets.QLabel(self.widget)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_2.addWidget(self.label_20)
        self.spinBox_6 = QtWidgets.QSpinBox(self.widget)
        self.spinBox_6.setMinimum(1)
        self.spinBox_6.setMaximum(10)
        self.spinBox_6.setObjectName("spinBox_6")
        self.horizontalLayout_2.addWidget(self.spinBox_6)
        self.groupBox_23 = QtWidgets.QGroupBox(self.groupBox_22)
        self.groupBox_23.setGeometry(QtCore.QRect(330, 20, 121, 51))
        self.groupBox_23.setObjectName("groupBox_23")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_23)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 20, 70, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_22 = QtWidgets.QLabel(self.tab_2)
        self.label_22.setGeometry(QtCore.QRect(20, 30, 61, 21))
        self.label_22.setObjectName("label_22")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_3.setGeometry(QtCore.QRect(90, 30, 171, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setEnabled(False)
        self.pushButton_6.setGeometry(QtCore.QRect(180, 230, 131, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_7.setEnabled(False)
        self.pushButton_7.setGeometry(QtCore.QRect(180, 140, 141, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.groupBox_14 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_14.setGeometry(QtCore.QRect(470, 110, 441, 191))
        self.groupBox_14.setObjectName("groupBox_14")
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_14)
        self.pushButton_10.setEnabled(False)
        self.pushButton_10.setGeometry(QtCore.QRect(30, 30, 111, 31))
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_51 = QtWidgets.QLabel(self.groupBox_14)
        self.label_51.setGeometry(QtCore.QRect(30, 100, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_51.setFont(font)
        self.label_51.setObjectName("label_51")
        self.label_53 = QtWidgets.QLabel(self.groupBox_14)
        self.label_53.setGeometry(QtCore.QRect(30, 140, 371, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_53.setFont(font)
        self.label_53.setStyleSheet("color:\"green\"")
        self.label_53.setObjectName("label_53")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1045, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Türkçe İşaret Dili Algılayıcı"))
        self.pushButton.setText(_translate("MainWindow", "Yükle"))
        self.groupBox.setTitle(_translate("MainWindow", "Veri seti içeriği"))
        self.pushButton_2.setText(_translate("MainWindow", "Bilgi"))
        self.groupBox_2.setTitle(_translate("MainWindow", "İşlemler"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Bilgiler"))
        self.label_6.setText(_translate("MainWindow", "0"))
        self.label_7.setText(_translate("MainWindow", "0"))
        self.label_3.setText(_translate("MainWindow", "Test resim adeti:"))
        self.label_4.setText(_translate("MainWindow", "Eğitim resim adeti:"))
        self.pushButton_3.setText(_translate("MainWindow", "Böl"))
        self.label.setText(_translate("MainWindow", "Test seti (%):"))
        self.groupBox_4.setTitle(_translate("MainWindow", "CSV Veri seti"))
        self.pushButton_4.setText(_translate("MainWindow", "Oluştur"))
        self.label_23.setText(_translate("MainWindow", "İşlem durumu:"))
        self.label_24.setText(_translate("MainWindow", "Hazır"))
        self.groupBox_12.setTitle(_translate("MainWindow", "Veri seti bilgileri"))
        self.label_26.setText(_translate("MainWindow", "Resim sayısı: 0"))
        self.label_27.setText(_translate("MainWindow", "Sınıf sayısı: 0"))
        self.groupBox_13.setTitle(_translate("MainWindow", "CSV Veri seti"))
        self.label_28.setText(_translate("MainWindow", "Adı: Yok"))
        self.label_29.setText(_translate("MainWindow", "Oluşturulma tarihi: 0000"))
        self.label_30.setText(_translate("MainWindow", "Son güncelleme tarihi: 0000"))
        self.label_50.setText(_translate("MainWindow", "Test oranı: 0%, Eğitim oranı: 0%"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Veri Seti"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Özel CNN ağı"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Transfer öğrenme"))
        self.label_2.setText(_translate("MainWindow", "Yöntem:"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Özel ağ"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Özel ayarlar"))
        self.label_5.setText(_translate("MainWindow", "Epochs:"))
        self.label_8.setText(_translate("MainWindow", "Batch size:"))
        self.radioButton.setText(_translate("MainWindow", "Özel ayar"))
        self.radioButton_2.setText(_translate("MainWindow", "Varsayılan ayar"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Varsayılan ayarlar"))
        self.label_9.setText(_translate("MainWindow", "Epochs: 10"))
        self.label_10.setText(_translate("MainWindow", "Batch size: 64"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Transfer öğrenme"))
        self.groupBox_9.setTitle(_translate("MainWindow", "Özel ayarlar"))
        self.label_11.setText(_translate("MainWindow", "Epochs:"))
        self.label_12.setText(_translate("MainWindow", "Batch size:"))
        self.radioButton_3.setText(_translate("MainWindow", "Özel ayar"))
        self.radioButton_4.setText(_translate("MainWindow", "Varsayılan ayar"))
        self.groupBox_10.setTitle(_translate("MainWindow", "Özel ayarlar"))
        self.label_13.setText(_translate("MainWindow", "Epochs: 10"))
        self.label_14.setText(_translate("MainWindow", "Batch size: 64"))
        self.label_15.setText(_translate("MainWindow", "Model:"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "MobileNetV2"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "ResNet50"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "InceptionV3"))
        self.groupBox_11.setTitle(_translate("MainWindow", "Eğtim bilgileri"))
        self.label_16.setText(_translate("MainWindow", "Yöntem: Özel CNN ağı"))
        self.label_19.setText(_translate("MainWindow", "Epochs: 10"))
        self.label_21.setText(_translate("MainWindow", "Batch size: 64"))
        self.label_17.setText(_translate("MainWindow", "Tam ad:  -"))
        self.pushButton_5.setText(_translate("MainWindow", "Eğit"))
        self.groupBox_16.setTitle(_translate("MainWindow", "Veri seti bilgileri"))
        self.label_37.setText(_translate("MainWindow", "Resim sayısı: 0"))
        self.label_38.setText(_translate("MainWindow", "Sınıf sayısı: 0"))
        self.groupBox_17.setTitle(_translate("MainWindow", "CSV Veri seti"))
        self.label_39.setText(_translate("MainWindow", "Adı: Yok"))
        self.label_40.setText(_translate("MainWindow", "Oluşturulma tarihi: 0000"))
        self.label_41.setText(_translate("MainWindow", "Son güncelleme tarihi: 0000"))
        self.label_52.setText(_translate("MainWindow", "Test oranı: 0%, Eğitim oranı: 0%"))
        self.groupBox_20.setTitle(_translate("MainWindow", "Model adı"))
        self.label_25.setText(_translate("MainWindow", "Adı:"))
        self.pushButton_9.setText(_translate("MainWindow", "Onayal"))
        self.label_46.setText(_translate("MainWindow", "İşlem durumu:"))
        self.label_47.setText(_translate("MainWindow", "Hazır"))
        self.groupBox_22.setTitle(_translate("MainWindow", "Ek özellikler"))
        self.groupBox_21.setTitle(_translate("MainWindow", "Early Stopping"))
        self.checkBox.setText(_translate("MainWindow", "Uygula"))
        self.label_20.setText(_translate("MainWindow", "Maksimum başarı olmayan Epoch sayısı:"))
        self.groupBox_23.setTitle(_translate("MainWindow", "Model check point"))
        self.checkBox_2.setText(_translate("MainWindow", "Uygula"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Eğitim"))
        self.label_22.setText(_translate("MainWindow", "Model Seç:"))
        self.pushButton_6.setText(_translate("MainWindow", "OpenCV ile test"))
        self.pushButton_7.setText(_translate("MainWindow", "TensorBoard Bilgi Göster"))
        self.groupBox_14.setTitle(_translate("MainWindow", "Dönüşüm"))
        self.pushButton_10.setText(_translate("MainWindow", "Dönüştür"))
        self.label_51.setText(_translate("MainWindow", "İşlem durumu:"))
        self.label_53.setText(_translate("MainWindow", "Hazır"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Bilgi, Test ve Tensorflow Lite dönüşüm"))
