
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(347, 355)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gif1 = QtWidgets.QLabel(self.centralwidget)
        self.gif1.setGeometry(QtCore.QRect(-70, -70, 501, 391))
        self.gif1.setText("")
        self.gif1.setPixmap(QtGui.QPixmap("../imgs/jar-1-unscreen.gif"))
        self.gif1.setScaledContents(True)
        self.gif1.setObjectName("gif1")
        self.ground = QtWidgets.QLabel(self.centralwidget)
        self.ground.setGeometry(QtCore.QRect(80, 20, 201, 211))
        self.ground.setText("")
        self.ground.setPixmap(QtGui.QPixmap("../imgs/1-removebg-preview.png"))
        self.ground.setScaledContents(True)
        self.ground.setObjectName("ground")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(100, 50, 161, 151))
        self.start.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../imgs/play btn.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.start.setIcon(icon)
        self.start.setIconSize(QtCore.QSize(150, 150))
        self.start.setAutoDefault(False)
        self.start.setDefault(True)
        self.start.setFlat(True)
        self.start.setObjectName("start")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-110, 200, 561, 141))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("imgs/load.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 347, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
