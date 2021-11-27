from PyQt5 import QtCore, QtGui, QtWidgets
from src.DomainModel.Pulse import MainForm

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainForm = MainForm()
    mainForm.show()
    sys.exit(app.exec_())

# CREATE TABLE Pulse (
# pulse_id SERIAL PRIMARY KEY,
# entered_pulse INT,
# good_pulse INT
# );
