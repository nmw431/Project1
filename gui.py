# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 400)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.PICK = QtWidgets.QLabel(parent=self.centralwidget)
        self.PICK.setGeometry(QtCore.QRect(110, 20, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.PICK.setFont(font)
        self.PICK.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.PICK.setObjectName("PICK")
        self.ADD = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.ADD.setGeometry(QtCore.QRect(20, 60, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ADD.setFont(font)
        self.ADD.setObjectName("ADD")
        self.SUBTRACT = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.SUBTRACT.setGeometry(QtCore.QRect(110, 60, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SUBTRACT.setFont(font)
        self.SUBTRACT.setObjectName("SUBTRACT")
        self.MULTIPLY = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.MULTIPLY.setGeometry(QtCore.QRect(200, 60, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MULTIPLY.setFont(font)
        self.MULTIPLY.setObjectName("MULTIPLY")
        self.DIVIDE = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.DIVIDE.setGeometry(QtCore.QRect(290, 60, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DIVIDE.setFont(font)
        self.DIVIDE.setObjectName("DIVIDE")
        self.CHOOSE = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.CHOOSE.setGeometry(QtCore.QRect(390, 60, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.CHOOSE.setFont(font)
        self.CHOOSE.setObjectName("CHOOSE")
        self.ENTER = QtWidgets.QLabel(parent=self.centralwidget)
        self.ENTER.setGeometry(QtCore.QRect(170, 100, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ENTER.setFont(font)
        self.ENTER.setObjectName("ENTER")
        self.VALUES = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.VALUES.setGeometry(QtCore.QRect(20, 130, 461, 20))
        self.VALUES.setObjectName("VALUES")
        self.RESPONSE = QtWidgets.QLabel(parent=self.centralwidget)
        self.RESPONSE.setGeometry(QtCore.QRect(30, 160, 431, 181))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.RESPONSE.setFont(font)
        self.RESPONSE.setText("")
        self.RESPONSE.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.RESPONSE.setObjectName("RESPONSE")
        self.SUBMIT = QtWidgets.QPushButton(parent=self.centralwidget)
        self.SUBMIT.setGeometry(QtCore.QRect(190, 340, 56, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.SUBMIT.setFont(font)
        self.SUBMIT.setObjectName("SUBMIT")
        self.CLEAR = QtWidgets.QPushButton(parent=self.centralwidget)
        self.CLEAR.setGeometry(QtCore.QRect(260, 340, 56, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.CLEAR.setFont(font)
        self.CLEAR.setObjectName("CLEAR")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Operator Calulator"))
        self.PICK.setText(_translate("MainWindow", "Pick an Operator"))
        self.ADD.setText(_translate("MainWindow", "Add"))
        self.SUBTRACT.setText(_translate("MainWindow", "Subtract"))
        self.MULTIPLY.setText(_translate("MainWindow", "Multiply"))
        self.DIVIDE.setText(_translate("MainWindow", "Divide"))
        self.CHOOSE.setText(_translate("MainWindow", "Choose"))
        self.ENTER.setText(_translate("MainWindow", "Enter Two Values Minimum Below"))
        self.SUBMIT.setText(_translate("MainWindow", "SUBMIT"))
        self.CLEAR.setText(_translate("MainWindow", "CLEAR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())