from PyQt5 import QtCore, QtGui, QtWidgets
from src.Interface.PlaylistForm import PlaylistForm


##-- Главное окно
class Playlist__(QtWidgets.QDialog):
    def __init__(self, res, parent=None):
        super().__init__(parent)
        self.ui = PlaylistForm()
        self.ui.setupUi(self)
        self.res = res
        self.setWindowTitle("Playlist")
        self.initUI()

    def initUI(self):
        # QtCore.QMetaObject.connectSlotsByName(Dialog)
        _translate = QtCore.QCoreApplication.translate
        if self.res == 1:
            self.ui.playlist_label.setText(_translate("Dialog", "Быстрый плейлист"))
        else:
            self.ui.playlist_label.setText(_translate("Dialog", "Медленный плейлист"))

