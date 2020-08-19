from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from pytube import YouTube
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import time
import os


class TheWindow(QMainWindow):
    def __init__(self):
        super(TheWindow, self).__init__()
        xpos = 75
        ypos = 750
        width = 600
        height = 220
        self.setGeometry(xpos, ypos, width, height)
        self.setWindowTitle("YouTube Downloader")
        self.initUI()

    def initUI(self):
        self.startButton = QtWidgets.QPushButton(self)
        self.startButton.setText("Start Download")
        self.startButton.clicked.connect(self.startdownload)

        self.exitButton = QtWidgets.QPushButton(self)
        self.exitButton.setText("Exit")
        self.exitButton.clicked.connect(self.exitbutton)
        self.exitButton.adjustSize()

        self.labelUrl = QtWidgets.QLabel(self)
        self.labelUrl.setText("YouTube URL      ")
        #ALIGN RIGHT/LEFT?

        self.loadDataButton = QtWidgets.QPushButton(self)
        self.loadDataButton.setText("Load Video Data")
        self.loadDataButton.clicked.connect(lambda:self.textchanged(self.urlBlock))

        self.urlBlock = QtWidgets.QLineEdit(self)

        self.videoCombo = QtWidgets.QComboBox(self)
        self.audioCombo = QtWidgets.QComboBox(self)

        self.videoCombo.addItem("Video Downloads")
        self.audioCombo.addItem("Audio Downloads")

        self.directoryLabel = QtWidgets.QLabel(self)
        self.directoryLabel.setText("Output Directory")

        self.browseButton = QtWidgets.QPushButton(self)
        self.browseButton.setText("Browse Folders  ")
        self.browseButton.clicked.connect(self.browsebutton)

        self.dirBlock = QtWidgets.QLineEdit(self)

        #self.urlBlock.textChanged.connect(lambda:self.textchanged(self.urlBlock))
        #self.startButton.clicked.connect(lambda:self.textchanged(self.urlBlock))
        self.initLayout()

    def initLayout(self):
        widget = QtWidgets.QWidget(self)
        self.setCentralWidget(widget)

        self.fbox = QtWidgets.QFormLayout()
        self.hboxLabelUrl = QtWidgets.QHBoxLayout()
        self.hboxLabelUrl.addWidget(self.labelUrl)
        self.hboxLabelUrl.addWidget(self.urlBlock)
        self.hboxLabelUrl.addWidget(self.loadDataButton)
        self.fbox.addRow(self.hboxLabelUrl)

        self.hboxDirectoryBrowse = QtWidgets.QHBoxLayout()
        self.hboxDirectoryBrowse.addWidget(self.directoryLabel)
        self.hboxDirectoryBrowse.addWidget(self.dirBlock)
        self.hboxDirectoryBrowse.addWidget(self.browseButton)
        self.fbox.addRow(self.hboxDirectoryBrowse)

        self.hboxComboBoxes = QtWidgets.QHBoxLayout()
        self.hboxComboBoxes.addWidget(self.videoCombo)
        self.hboxComboBoxes.addWidget(self.audioCombo)
        self.fbox.addRow(self.hboxComboBoxes)

        self.hboxStartExit = QtWidgets.QHBoxLayout()
        self.hboxStartExit.addWidget(self.startButton)
        self.hboxStartExit.addWidget(self.exitButton)
        self.fbox.addRow(self.hboxStartExit)

        widget.setLayout(self.fbox)

    def browsebutton(self):
        #os.system('explorer.exe "C:\users\%username%\Desktop"')
        dir_ = QtWidgets.QFileDialog.getExistingDirectory(self,
            'Select Download Folder:', '/Users/patrickmac', QtWidgets.QFileDialog.ShowDirsOnly)
        print(dir_)
        self.dirBlock.setText(dir_)


    def exitbutton(self):
        quit()

    def startdownload(self):
        print ("Starting Download: ")

    def videocombobox(self, yt):
        #index = self.videoCombo.findText("THIS IS A TEST")
        self.videoCombo.removeItem(0)

        if(yt.streams.filter(subtype='mp4')):
            self.videoCombo.addItem("MP4 - Highest Quality")
            self.videoCombo.addItem("MP4 - Lowest Quality")

        if(yt.streams.filter(subtype='webm')):
            self.videoCombo.addItem("WebM - Highest Quality")
            self.videoCombo.addItem("WebM - Lowest Quality")

        self.videoCombo.addItem("Download Audio Only")


    def audiocombobox(self, yt):
        self.audioCombo.removeItem(0)

        self.audioCombo.addItem("Download Video Only")

        if(yt.streams.filter(only_audio=True).filter(subtype='mp4')):
            self.audioCombo.addItem("MP4 - Best Audio Only")
            self.audioCombo.addItem("MP4 - Worst Audio Only")

        if(yt.streams.filter(only_audio=True).filter(subtype='webm')):
            self.audioCombo.addItem("WebM - Best Audio Only")
            self.audioCombo.addItem("WebM - Worst Audio Only")

    def textchanged(self, url):
        #self.exitButton.adjustSize()
        userUrl = url.text()
        print ("The URL Was: " + userUrl)
        #YouTube('https://www.youtube.com/watch?v=QDIxi99xbOg').streams.first().download()

        time.sleep(2)
        yt = YouTube(userUrl)
        #video = yt.streams.first()
        #video.download('/Users/patrickmac/Desktop/YouTubeVids')

        #print(yt.streams)

        title = yt.title
        views = yt.views
        author = yt.author
        thumbUrl= yt.thumbnail_url

        print("Title = " + f'{yt.title}')
        print("Title: " + title)
        print ("Views: " + str(views))
        print ("Author: " + author)
        print ("Thumbnail Url: " + thumbUrl)

        self.videocombobox(yt)
        self.audiocombobox(yt)


        #views = yt.views()
        #print ("The Title Was:" + views)
        #return yt

    def updateLabel(self):
        self.label.adjustSize()



def window():
    #pass command line arguments to app
    app = QApplication(sys.argv)
    window = TheWindow()


    window.show()
    sys.exit(app.exec_())

window()
