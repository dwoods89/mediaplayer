from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtCore import QSize
import qdarkstyle
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('mainwindow.ui', self)

        self.tbtn_MaxMin = self.findChild(QtWidgets.QToolButton, 'tbtn_MaxMin')
        self.tbtn_MaxMin.setCheckable(True)
        self.tbtn_MaxMin.setIcon(QtGui.QIcon('resources/icons/minimize.png'))
        self.tbtn_MaxMin.setIconSize(self.tbtn_MaxMin.frameSize())
        self.tbtn_MaxMin.clicked.connect(self.minmax_clicked)

        self.tbtn_PlayPause = self.findChild(QtWidgets.QToolButton, 'tbtn_PlayPause')
        self.tbtn_PlayPause.setCheckable(True)
        self.tbtn_PlayPause.setIcon(QtGui.QIcon('resources/icons/play.png'))
        self.tbtn_PlayPause.setIconSize(self.tbtn_PlayPause.frameSize())
        self.tbtn_PlayPause.clicked.connect(self.playpause_clicked)
        self.showFullScreen()

        self.tbtn_rewind = self.findChild(QtWidgets.QToolButton, 'tbtn_rewind')
        self.tbtn_rewind.setIcon(QtGui.QIcon('resources/icons/rewind.png'))
        self.tbtn_rewind.setIconSize(self.tbtn_rewind.frameSize())
        self.tbtn_rewind.clicked.connect(self.rewind_clicked)

        self.tbtn_fast_forward = self.findChild(QtWidgets.QToolButton, 'tbtn_fast_forward')
        self.tbtn_fast_forward.setIcon(QtGui.QIcon('resources/icons/fast-forward.png'))
        self.tbtn_fast_forward.setIconSize(self.tbtn_rewind.frameSize())
        self.tbtn_fast_forward.clicked.connect(self.fast_forward_clicked)

        self.showFullScreen()

    def minmax_clicked(self):
        if self.tbtn_MaxMin.isChecked():
            self.showNormal()
            self.tbtn_MaxMin.setIcon(QtGui.QIcon('resources/icons/maximize.png'))
        elif not self.tbtn_MaxMin.isChecked():
            self.tbtn_MaxMin.setIcon(QtGui.QIcon('resources/icons/minimize.png'))
            self.showFullScreen()

    def playpause_clicked(self):
        if self.tbtn_PlayPause.isChecked():
            print("Play")
            self.tbtn_PlayPause.setIcon(QtGui.QIcon('resources/icons/pause.png'))
        elif not self.tbtn_PlayPause.isChecked():
            print("Pause")
            self.tbtn_PlayPause.setIcon(QtGui.QIcon('resources/icons/play.png'))

    def rewind_clicked(self):
        print("rewind")

    def fast_forward_clicked(self):
        print("fast forward")




app = QtWidgets.QApplication(sys.argv)
app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
window = Ui()
app.exec_()
