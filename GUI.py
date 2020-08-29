from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from pytube import YouTube, Stream
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import time
import os
import urllib.request
from PIL import Image



class TheWindow(QMainWindow):
    def __init__(self):
        super(TheWindow, self).__init__()
        xpos = 75
        ypos = 750
        width = 700
        height = 230
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
        self.dirBlock.setText("/Users/patrickmac/Downloads")

        defaultImage = "/Users/patrickmac/Desktop/code/python/YouTubeDL/thumbnails/default.jpeg"
        self.thumbnail = QtGui.QPixmap(defaultImage)

        self.labelPix = QtWidgets.QLabel(self)
        self.labelPix.setPixmap(self.thumbnail)

        self.labelTitle = QtWidgets.QLabel(self)
        self.labelTitle.setFont( QFont('Arial', 16))
        self.labelTitle.setText("Place Holder Title")
        self.labelTitle.setAlignment(QtCore.Qt.AlignCenter)


        self.labelAuthorViews = QtWidgets.QLabel(self)
        self.labelAuthorViews.setFont( QFont('Arial', 14))
        self.labelAuthorViews.setText("Author of Video" + "  ‣  " + "000,000 views")
        self.labelAuthorViews.setAlignment(QtCore.Qt.AlignCenter)



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

        self.vboxPicTitleViews = QtWidgets.QVBoxLayout()
        self.vboxPicTitleViews.addWidget(self.labelPix)
        self.vboxPicTitleViews.addWidget(self.labelTitle)
        self.vboxPicTitleViews.addWidget(self.labelAuthorViews)
        self.hboxComboBoxes.addLayout(self.vboxPicTitleViews)

        self.vboxCB = QtWidgets.QVBoxLayout()
        self.vboxCB.addWidget(self.videoCombo)
        self.vboxCB.addWidget(self.audioCombo)
        self.vboxCB.addWidget(self.startButton)
        self.hboxComboBoxes.addLayout(self.vboxCB)

        self.fbox.addRow(self.hboxComboBoxes)

        self.hboxStartExit = QtWidgets.QHBoxLayout()
        #self.hboxStartExit.addWidget(self.startButton)
        self.hboxStartExit.addWidget(self.exitButton)
        self.fbox.addRow(self.hboxStartExit)

        widget.setLayout(self.fbox)

    def browsebutton(self):
        #os.system('explorer.exe "C:\users\%username%\Desktop"')
        dir_ = QtWidgets.QFileDialog.getExistingDirectory(self,
            'Select Download Folder:', '/Users/patrickmac', QtWidgets.QFileDialog.ShowDirsOnly)
        self.dirBlock.setText(dir_)


    def exitbutton(self):
        quit()

    def startdownload(self):
        print ("Starting Download: ")

        videoComboData = self.videoCombo.currentText()
        audioComboData = self.audioCombo.currentText()

        print("video combo data: " + videoComboData)
        print("audio combo data: " + audioComboData)


    def videocombobox(self, yt):
        self.videoCombo.clear()

        if(yt.streams.filter(subtype='mp4')):
            self.videoCombo.addItem("MP4 - Highest Quality")
            self.videoCombo.addItem("MP4 - Lowest Quality")

        if(yt.streams.filter(subtype='webm')):
            self.videoCombo.addItem("WebM - Highest Quality")
            self.videoCombo.addItem("WebM - Lowest Quality")

        self.videoCombo.addItem("Download Audio Only")


    def audiocombobox(self, yt):
        self.audioCombo.clear()

        self.audioCombo.addItem("Download Video Only")

        if(yt.streams.filter(only_audio=True).filter(subtype='mp4')):
            self.audioCombo.addItem("MP4 - Best Audio Only")
            self.audioCombo.addItem("MP4 - Worst Audio Only")

        if(yt.streams.filter(only_audio=True).filter(subtype='webm')):
            self.audioCombo.addItem("WebM - Best Audio Only")
            self.audioCombo.addItem("WebM - Worst Audio Only")

    def updateData(self, yt):
        urllib.request.urlretrieve(yt.thumbnail_url,
                    '/Users/patrickmac/Desktop/code/python/YouTubeDL/thumbnails/default.jpg')

        im = Image.open(r"/Users/patrickmac/Desktop/code/python/YouTubeDL/thumbnails/default.jpg")
        resizeXY = (300, 170)
        im = im.resize(resizeXY)
        im.save(r"/Users/patrickmac/Desktop/code/python/YouTubeDL/thumbnails/default.jpg")

        thumbPic = "/Users/patrickmac/Desktop/code/python/YouTubeDL/thumbnails/default.jpg"
        self.updatedThumb = QtGui.QPixmap(thumbPic)
        self.labelPix.setPixmap(self.updatedThumb)

        self.labelTitle.setWordWrap(True)
        self.labelTitle.setText(yt.title)
        viewsStr = '{:,}'.format(yt.views)
        self.labelAuthorViews.setText(yt.author + "  ‣  " + viewsStr + " views")

    def textchanged(self, url):
        userUrl = url.text()

        yt = YouTube(userUrl)
        stream = yt.streams.filter(progressive = True, file_extension = "mp4").first()
        #stream.download('/Users/patrickmac/Desktop/YouTubeVids')

        # title = yt.title
        # views = yt.views
        # author = yt.author
        # thumbUrl= yt.thumbnail_url
        #defaultTitle = stream.default_filename

        #
        #
        #print("Title: " + defaultTitle)
        # print ("Views: " + str(views))
        # print ("Author: " + author)
        # print ("Thumbnail Url: " + thumbUrl)

        self.videocombobox(yt)
        self.audiocombobox(yt)
        self.updateData(yt)

    def updateLabel(self):
        self.label.adjustSize()



def window():
    #pass command line arguments to app
    app = QApplication(sys.argv)
    window = TheWindow()


    window.show()
    sys.exit(app.exec_())

window()
