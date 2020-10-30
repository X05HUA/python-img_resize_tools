#!/usr/bin/env python3


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import Tools.img_main


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(0, 0, 885, 600))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("red_blue.png"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 340, 171, 41))
        self.pushButton.clicked.connect(self.clicked)
        self.pushButton.setObjectName("pushButton")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(260, 230, 301, 31))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")

        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(260, 280, 301, 31))
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName("textEdit_2")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 240, 77, 18))
        self.label.setFont(QFont('Times', 10))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 290, 77, 18))
        self.label_2.setFont(QFont('Times', 10))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(277, 150, 700, 51))
        self.label_3.setFont(QFont('Times', 45))
        self.label_3.setObjectName("label_3")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(590, 340, 78, 26))
        self.width_list = list(range(10, 1930, 10))
        # l_file_type = [each_string.lower() for each_string in file_types] # EXAMPLE
        self.width_list = [str(num) for num in self.width_list]
        # self.comboBox.setEditable(True)
        self.comboBox.addItems(self.width_list)
        self.comboBox.setObjectName("comboBox")

        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(590, 390, 78, 26))
        self.height_list = list(range(10, 1090, 10))
        self.height_list = [str(num) for num in self.height_list]
        # self.comboBox_2.setEditable(True)
        self.comboBox_2.addItems(self.height_list)
        self.comboBox_2.setObjectName("comboBox_2")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(560, 230, 80, 31))
        self.pushButton_2.clicked.connect(self.in_click)
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(560, 280, 80, 31))
        self.pushButton_3.clicked.connect(self.out_click)
        self.pushButton_3.setObjectName("pushButton_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(600, 320, 58, 18))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(600, 370, 58, 18))
        self.label_5.setObjectName("label_5")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "File Resize"))
        self.pushButton.setText(_translate("MainWindow", "Resize Images"))
        self.label.setText(_translate("MainWindow", "Input Dir"))
        self.label_2.setText(_translate("MainWindow", "Output Dir"))
        self.label_3.setText(_translate("MainWindow", "File Resize"))
        self.pushButton_2.setText(_translate("MainWindow", "Browse"))
        self.pushButton_3.setText(_translate("MainWindow", "Browse"))
        self.label_4.setText(_translate("MainWindow", "Width"))
        self.label_5.setText(_translate("MainWindow", "Height"))

    def clicked(self):
        self.cb_width = self.comboBox.currentText()
        self.cb_height = self.comboBox_2.currentText()
        Tools.img_main.resize_pics(int(self.cb_width), int(self.cb_height), str(self.in_dir), str(self.out_dir))

    def in_click(self):
        self.in_dir = str(QFileDialog.getExistingDirectory(self.centralwidget, 'Select Directory',
                                                   "/run/media/chaos/850 evo/Images"))
        self.textEdit.setPlaceholderText(f"{self.in_dir}")

    def out_click(self):
        self.out_dir = str(QFileDialog.getExistingDirectory(self.centralwidget, 'Select Directory',
                                                   "/run/media/chaos/850 evo/Images"))
        self.textEdit_2.setPlaceholderText(f"{self.out_dir}")

    def get_image_dir(self):
        file_name, _ = QFileDialog.getOpenFileName(self.centralwidget, 'Open Image File',
                                                   "/run/media/chaos/850 evo/Images")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
