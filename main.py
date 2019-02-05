from PyQt5 import QtCore, QtGui, QtWidgets
from internal import Internal_Ui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(140, 30, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.email = QtWidgets.QLabel(Dialog)
        self.email.setGeometry(QtCore.QRect(150, 120, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.email.setFont(font)
        self.email.setObjectName("email")
        self.emailText = QtWidgets.QLineEdit(Dialog)
        self.emailText.setGeometry(QtCore.QRect(100, 150, 201, 20))
        self.emailText.setObjectName("emailText")
        self.submitButton = QtWidgets.QPushButton(Dialog)
        self.submitButton.setGeometry(QtCore.QRect(160, 190, 75, 23))
        self.submitButton.setObjectName("submitButton")
        self.submitButton.clicked.connect(self.emailtext)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Welcome"))
        self.email.setText(_translate("Dialog", "Enter Email :"))
        self.submitButton.setText(_translate("Dialog", "Submit"))

    def emailtext(self):
        self.welcomeWindow = QtWidgets.QDialog()
        self.ui = Internal_Ui(self.emailText.text().split('@')[0])
        self.ui.setupUi(self.welcomeWindow)
        self.welcomeWindow.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

