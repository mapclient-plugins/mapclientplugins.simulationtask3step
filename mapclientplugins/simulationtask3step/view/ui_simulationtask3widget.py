# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simulationtask3widget.ui'
#
# Created: Wed May 27 23:51:22 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_SimulationTask3Widget(object):
    def setupUi(self, SimulationTask3Widget):
        SimulationTask3Widget.setObjectName("SimulationTask3Widget")
        SimulationTask3Widget.resize(819, 567)
        self.horizontalLayout = QtGui.QHBoxLayout(SimulationTask3Widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dockWidget = QtGui.QDockWidget(SimulationTask3Widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget.sizePolicy().hasHeightForWidth())
        self.dockWidget.setSizePolicy(sizePolicy)
        self.dockWidget.setStyleSheet("QToolBox::tab {\n"
"         background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                     stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"         border-radius: 5px;\n"
"         color: black;\n"
"     }\n"
"\n"
"     QToolBox::tab:selected { /* italicize selected tabs */\n"
"         font: bold;\n"
"         color: black;\n"
"     }\n"
"QToolBox {\n"
"    padding : 0\n"
"}")
        self.dockWidget.setFloating(False)
        self.dockWidget.setFeatures(QtGui.QDockWidget.NoDockWidgetFeatures)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtGui.QWidget(self.dockWidgetContents)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtGui.QLabel(self.widget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.stepSizeEdit = QtGui.QLineEdit(self.widget_2)
        self.stepSizeEdit.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.stepSizeEdit.setObjectName("stepSizeEdit")
        self.horizontalLayout_5.addWidget(self.stepSizeEdit)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget = QtGui.QWidget(self.dockWidgetContents)
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.toleranceEdit = QtGui.QLineEdit(self.widget)
        self.toleranceEdit.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.toleranceEdit.setObjectName("toleranceEdit")
        self.horizontalLayout_2.addWidget(self.toleranceEdit)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.widget)
        self.simulateButton = QtGui.QPushButton(self.dockWidgetContents)
        self.simulateButton.setObjectName("simulateButton")
        self.verticalLayout.addWidget(self.simulateButton)
        self.clearButton = QtGui.QPushButton(self.dockWidgetContents)
        self.clearButton.setObjectName("clearButton")
        self.verticalLayout.addWidget(self.clearButton)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.doneButton = QtGui.QPushButton(self.dockWidgetContents)
        self.doneButton.setObjectName("doneButton")
        self.verticalLayout.addWidget(self.doneButton)
        self.dockWidget.setWidget(self.dockWidgetContents)
        self.horizontalLayout.addWidget(self.dockWidget)
        self.plotPane = QtGui.QWidget(SimulationTask3Widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotPane.sizePolicy().hasHeightForWidth())
        self.plotPane.setSizePolicy(sizePolicy)
        self.plotPane.setObjectName("plotPane")
        self.horizontalLayout.addWidget(self.plotPane)

        self.retranslateUi(SimulationTask3Widget)
        QtCore.QMetaObject.connectSlotsByName(SimulationTask3Widget)

    def retranslateUi(self, SimulationTask3Widget):
        SimulationTask3Widget.setWindowTitle(QtGui.QApplication.translate("SimulationTask3Widget", "Heart Transform", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget.setWindowTitle(QtGui.QApplication.translate("SimulationTask3Widget", "Simulation Task 3", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("SimulationTask3Widget", "h:", None, QtGui.QApplication.UnicodeUTF8))
        self.stepSizeEdit.setText(QtGui.QApplication.translate("SimulationTask3Widget", "0.0", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SimulationTask3Widget", "tolerance:", None, QtGui.QApplication.UnicodeUTF8))
        self.toleranceEdit.setText(QtGui.QApplication.translate("SimulationTask3Widget", "1.0e-7", None, QtGui.QApplication.UnicodeUTF8))
        self.simulateButton.setText(QtGui.QApplication.translate("SimulationTask3Widget", "Simulate", None, QtGui.QApplication.UnicodeUTF8))
        self.clearButton.setText(QtGui.QApplication.translate("SimulationTask3Widget", "Clear graph", None, QtGui.QApplication.UnicodeUTF8))
        self.doneButton.setText(QtGui.QApplication.translate("SimulationTask3Widget", "Done", None, QtGui.QApplication.UnicodeUTF8))

