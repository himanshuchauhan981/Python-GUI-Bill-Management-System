from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_InvoiceGenerated(object):
    def setupUi(self, InvoiceGenerated):
        InvoiceGenerated.setObjectName("InvoiceGenerated")
        InvoiceGenerated.resize(436, 216)
        self.centralwidget = QtWidgets.QWidget(InvoiceGenerated)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 50, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 110, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        InvoiceGenerated.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(InvoiceGenerated)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 436, 21))
        self.menubar.setObjectName("menubar")
        InvoiceGenerated.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(InvoiceGenerated)
        self.statusbar.setObjectName("statusbar")
        InvoiceGenerated.setStatusBar(self.statusbar)

        self.retranslateUi(InvoiceGenerated)
        self.pushButton.clicked.connect(InvoiceGenerated.close)
        QtCore.QMetaObject.connectSlotsByName(InvoiceGenerated)

    def retranslateUi(self, InvoiceGenerated):
        _translate = QtCore.QCoreApplication.translate
        InvoiceGenerated.setWindowTitle(_translate("InvoiceGenerated", "MainWindow"))
        self.label.setText(_translate("InvoiceGenerated", "Invoice is Generated Successfully"))
        self.pushButton.setText(_translate("InvoiceGenerated", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InvoiceGenerated = QtWidgets.QMainWindow()
    ui = Ui_InvoiceGenerated()
    ui.setupUi(InvoiceGenerated)
    InvoiceGenerated.show()
    sys.exit(app.exec_())

