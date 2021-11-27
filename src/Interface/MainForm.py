from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(812, 632)
        Dialog.setStyleSheet("background-color: rgb(100, 10, 125);")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(90, 80, 631, 461))
        self.frame.setStyleSheet("background-color: rgb(100, 251, 251);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pulse_entered_label = QtWidgets.QLabel(self.frame)
        self.pulse_entered_label.setGeometry(QtCore.QRect(0, 165, 250, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pulse_entered_label.setFont(font)
        self.pulse_entered_label.setStyleSheet("color: rgb(0, 0, 0);")
        self.pulse_entered_label.setObjectName("pulse_entered_label")

        self.pulseEnteredEdit = QtWidgets.QLineEdit(self.frame)
        self.pulseEnteredEdit.setGeometry(QtCore.QRect(260, 165, 250, 30))
        self.pulseEnteredEdit.setStyleSheet("color: rgb(0, 0, 0);")
        self.pulseEnteredEdit.setStyleSheet("background-color: rgb(10, 207, 255); color: rgb(0, 0, 0);")
        self.pulseEnteredEdit.setObjectName("pulseEnteredEdit")


        self.pulse_process_label = QtWidgets.QLabel(self.frame)
        self.pulse_process_label.setGeometry(QtCore.QRect(0, 250, 250, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pulse_process_label.setFont(font)
        self.pulse_process_label.setStyleSheet("color: rgb(0, 0, 0);")
        self.pulse_process_label.setObjectName("pulse_process_label")

        self.pulseProcessedEdit = QtWidgets.QLineEdit(self.frame)
        self.pulseProcessedEdit.setGeometry(QtCore.QRect(260, 250, 250, 30))
        self.pulseProcessedEdit.setStyleSheet("color: rgb(0, 0, 0);")
        self.pulseProcessedEdit.setStyleSheet("background-color: rgb(10, 207, 255); color: rgb(0, 0, 0);")
        self.pulseProcessedEdit.setObjectName("pulseProcessedEdit")

        self.generBtn = QtWidgets.QPushButton(self.frame)
        self.generBtn.setGeometry(QtCore.QRect(520, 250, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.generBtn.setFont(font)
        self.generBtn.setStyleSheet("background-color: rgb(20, 170, 250);")
        self.generBtn.setObjectName("gener")

        self.ok_button = QtWidgets.QPushButton(self.frame)
        self.ok_button.setGeometry(QtCore.QRect(350, 360, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ok_button.setFont(font)
        self.ok_button.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.ok_button.setObjectName("pushButton")
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pulse_entered_label.setText(_translate("Dialog", "Введите ваш нормальный пульс"))
        self.ok_button.setText(_translate("Dialog", "ОК"))
        self.pulse_process_label.setText(_translate("Dialog", "Ваш измеренный пульс"))
        self.generBtn.setText(_translate("Dialog", 'Random'))

