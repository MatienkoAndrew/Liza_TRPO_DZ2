from PyQt5 import QtCore, QtGui, QtWidgets


class PlaylistForm(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(812, 632)
        Dialog.setStyleSheet("background-color: rgb(100, 10, 125);")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 80, 700, 700))
        self.frame.setStyleSheet("background-color: rgb(100, 251, 251);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.playlist_label = QtWidgets.QLabel(self.frame)
        self.playlist_label.setGeometry(QtCore.QRect(0, 250, 250, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.playlist_label.setFont(font)
        self.playlist_label.setStyleSheet("color: rgb(0, 0, 0);")
        self.playlist_label.setObjectName("pulse_process_label")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.playlist_label.setText(_translate("Dialog", "Пульс"))

