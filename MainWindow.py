# Form implementation generated from reading ui file '.\maintest.ui'
#
# Created by: PyQt6 UI code generator 6.0.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_baramWindow(object):
    def setupUi(self, baramWindow):
        baramWindow.setObjectName("baramWindow")
        baramWindow.resize(532, 271)
        self.baramWidget = QtWidgets.QWidget(baramWindow)
        self.baramWidget.setObjectName("baramWidget")
        self.allExecuteBtn = QtWidgets.QPushButton(self.baramWidget)
        self.allExecuteBtn.setGeometry(QtCore.QRect(440, 190, 71, 24))
        self.allExecuteBtn.setObjectName("allExecuteBtn")
        self.deleteBtn = QtWidgets.QPushButton(self.baramWidget)
        self.deleteBtn.setGeometry(QtCore.QRect(440, 10, 71, 24))
        self.deleteBtn.setObjectName("deleteBtn")
        self.addBtn = QtWidgets.QPushButton(self.baramWidget)
        self.addBtn.setGeometry(QtCore.QRect(40, 130, 91, 21))
        self.addBtn.setObjectName("addBtn")
        self.updateBtn = QtWidgets.QPushButton(self.baramWidget)
        self.updateBtn.setGeometry(QtCore.QRect(440, 40, 71, 24))
        self.updateBtn.setObjectName("updateBtn")
        self.platformType = QtWidgets.QComboBox(self.baramWidget)
        self.platformType.setGeometry(QtCore.QRect(40, 100, 91, 22))
        self.platformType.setObjectName("platformType")
        self.platformType.addItem("")
        self.platformType.addItem("")
        self.platformType.addItem("")
        self.platformType.addItem("")
        self.idListView = QtWidgets.QListView(self.baramWidget)
        self.idListView.setGeometry(QtCore.QRect(150, 10, 281, 211))
        self.idListView.setObjectName("idListView")
        self.idLabel = QtWidgets.QLabel(self.baramWidget)
        self.idLabel.setGeometry(QtCore.QRect(10, 10, 21, 16))
        self.idLabel.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.idLabel.setObjectName("idLabel")
        self.pwLabel = QtWidgets.QLabel(self.baramWidget)
        self.pwLabel.setGeometry(QtCore.QRect(10, 40, 21, 16))
        self.pwLabel.setAlignment(QtCore.Qt.Alignment.AlignCenter)
        self.pwLabel.setObjectName("pwLabel")
        self.loginBtn = QtWidgets.QPushButton(self.baramWidget)
        self.loginBtn.setGeometry(QtCore.QRect(440, 70, 71, 24))
        self.loginBtn.setObjectName("loginBtn")
        self.executeBtn = QtWidgets.QPushButton(self.baramWidget)
        self.executeBtn.setGeometry(QtCore.QRect(440, 160, 71, 24))
        self.executeBtn.setObjectName("executeBtn")
        self.allLoginBtn = QtWidgets.QPushButton(self.baramWidget)
        self.allLoginBtn.setGeometry(QtCore.QRect(440, 100, 71, 24))
        self.allLoginBtn.setObjectName("allLoginBtn")
        self.jobType = QtWidgets.QComboBox(self.baramWidget)
        self.jobType.setGeometry(QtCore.QRect(40, 70, 91, 22))
        self.jobType.setObjectName("jobType")
        self.jobType.addItem("")
        self.jobType.addItem("")
        self.jobType.addItem("")
        self.jobType.addItem("")
        self.jobType.addItem("")
        self.jobType.addItem("")
        self.jobType.addItem("")
        self.idText = QtWidgets.QLineEdit(self.baramWidget)
        self.idText.setGeometry(QtCore.QRect(40, 10, 91, 22))
        self.idText.setObjectName("idText")
        self.pwText = QtWidgets.QLineEdit(self.baramWidget)
        self.pwText.setGeometry(QtCore.QRect(40, 40, 91, 22))
        self.pwText.setObjectName("pwText")
        self.loadBtn = QtWidgets.QPushButton(self.baramWidget)
        self.loadBtn.setGeometry(QtCore.QRect(40, 160, 91, 24))
        self.loadBtn.setObjectName("loadBtn")
        baramWindow.setCentralWidget(self.baramWidget)
        self.menubar = QtWidgets.QMenuBar(baramWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 532, 22))
        self.menubar.setObjectName("menubar")
        baramWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(baramWindow)
        self.statusbar.setObjectName("statusbar")
        baramWindow.setStatusBar(self.statusbar)

        self.retranslateUi(baramWindow)
        QtCore.QMetaObject.connectSlotsByName(baramWindow)

    def retranslateUi(self, baramWindow):
        _translate = QtCore.QCoreApplication.translate
        baramWindow.setWindowTitle(_translate("baramWindow", "Baram:Yeon"))
        self.allExecuteBtn.setText(_translate("baramWindow", "All Execute"))
        self.deleteBtn.setText(_translate("baramWindow", "Delete"))
        self.addBtn.setText(_translate("baramWindow", "Add"))
        self.updateBtn.setText(_translate("baramWindow", "Update"))
        self.platformType.setItemText(0, _translate("baramWindow", "Nexon"))
        self.platformType.setItemText(1, _translate("baramWindow", "Google"))
        self.platformType.setItemText(2, _translate("baramWindow", "Naver"))
        self.platformType.setItemText(3, _translate("baramWindow", "Facebook"))
        self.idLabel.setText(_translate("baramWindow", "ID"))
        self.pwLabel.setText(_translate("baramWindow", "PW"))
        self.loginBtn.setText(_translate("baramWindow", "Login"))
        self.executeBtn.setText(_translate("baramWindow", "Execute"))
        self.allLoginBtn.setText(_translate("baramWindow", "All Login"))
        self.jobType.setItemText(0, _translate("baramWindow", "??????"))
        self.jobType.setItemText(1, _translate("baramWindow", "??????"))
        self.jobType.setItemText(2, _translate("baramWindow", "?????????"))
        self.jobType.setItemText(3, _translate("baramWindow", "??????"))
        self.jobType.setItemText(4, _translate("baramWindow", "??????"))
        self.jobType.setItemText(5, _translate("baramWindow", "?????????"))
        self.jobType.setItemText(6, _translate("baramWindow", "??????"))
        self.loadBtn.setText(_translate("baramWindow", "Load"))
