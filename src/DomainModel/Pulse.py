from PyQt5 import QtCore, QtGui, QtWidgets
from src.Interface.MainForm import Ui_Dialog
from src.DomainModel.Playlist import Playlist__

from src.RowDataGateway.PulseGateway import PulseGateway
import random

class Pulse:
    def __init__(self, entered_pulse, processed_pulse):
        self.entered_pulse = entered_pulse
        self.processed_pulse = processed_pulse
        pass

    def get_playlists(self):
        pulseGateway = PulseGateway()
        pulseGateway.entered_pulse = self.entered_pulse
        pulseGateway.processed_pulse = self.processed_pulse
        pulseGateway.Insert()

        if self.processed_pulse > self.entered_pulse:
            return 1
        else:
            return 0


##-- Главное окно
class MainForm(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("Pulse")
        self.random_pulse = None
        self.Playlist = None

        self.ui.generBtn.clicked.connect(self.get_random_pulse)
        self.ui.ok_button.clicked.connect(self.get_playlists)

    def get_playlists(self):
        # введенный пульс
        entered_pulse = self.ui.pulseEnteredEdit.text()
        pulse = Pulse(entered_pulse, self.random_pulse)
        res = pulse.get_playlists()
        self.Playlist = Playlist__(res)
        self.Playlist.show()
        self.close()

    def get_random_pulse(self):
        random_int = random.randint(40, 180)
        self.random_pulse = str(random_int)
        self.ui.pulseProcessedEdit.setText(self.random_pulse)
        pass
