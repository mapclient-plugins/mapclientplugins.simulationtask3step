# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'simulationtask3widget.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDockWidget, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_SimulationTask3Widget(object):
    def setupUi(self, SimulationTask3Widget):
        if not SimulationTask3Widget.objectName():
            SimulationTask3Widget.setObjectName(u"SimulationTask3Widget")
        SimulationTask3Widget.resize(819, 567)
        self.horizontalLayout = QHBoxLayout(SimulationTask3Widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.dockWidget = QDockWidget(SimulationTask3Widget)
        self.dockWidget.setObjectName(u"dockWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget.sizePolicy().hasHeightForWidth())
        self.dockWidget.setSizePolicy(sizePolicy)
        self.dockWidget.setStyleSheet(u"QToolBox::tab {\n"
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
        self.dockWidget.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.dockWidgetContents)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.stepSizeEdit = QLineEdit(self.widget_2)
        self.stepSizeEdit.setObjectName(u"stepSizeEdit")
        self.stepSizeEdit.setInputMethodHints(Qt.ImhFormattedNumbersOnly)

        self.horizontalLayout_5.addWidget(self.stepSizeEdit)


        self.verticalLayout.addWidget(self.widget_2)

        self.widget = QWidget(self.dockWidgetContents)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label, 0, Qt.AlignLeft)

        self.toleranceEdit = QLineEdit(self.widget)
        self.toleranceEdit.setObjectName(u"toleranceEdit")
        self.toleranceEdit.setInputMethodHints(Qt.ImhFormattedNumbersOnly)

        self.horizontalLayout_2.addWidget(self.toleranceEdit)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.widget)

        self.simulateButton = QPushButton(self.dockWidgetContents)
        self.simulateButton.setObjectName(u"simulateButton")

        self.verticalLayout.addWidget(self.simulateButton)

        self.clearButton = QPushButton(self.dockWidgetContents)
        self.clearButton.setObjectName(u"clearButton")

        self.verticalLayout.addWidget(self.clearButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.doneButton = QPushButton(self.dockWidgetContents)
        self.doneButton.setObjectName(u"doneButton")

        self.verticalLayout.addWidget(self.doneButton)

        self.dockWidget.setWidget(self.dockWidgetContents)

        self.horizontalLayout.addWidget(self.dockWidget)

        self.plotPane = QWidget(SimulationTask3Widget)
        self.plotPane.setObjectName(u"plotPane")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(3)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.plotPane.sizePolicy().hasHeightForWidth())
        self.plotPane.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.plotPane)


        self.retranslateUi(SimulationTask3Widget)

        QMetaObject.connectSlotsByName(SimulationTask3Widget)
    # setupUi

    def retranslateUi(self, SimulationTask3Widget):
        SimulationTask3Widget.setWindowTitle(QCoreApplication.translate("SimulationTask3Widget", u"Heart Transform", None))
        self.dockWidget.setWindowTitle(QCoreApplication.translate("SimulationTask3Widget", u"Simulation Task 3", None))
        self.label_2.setText(QCoreApplication.translate("SimulationTask3Widget", u"h:", None))
        self.stepSizeEdit.setText(QCoreApplication.translate("SimulationTask3Widget", u"0.0", None))
        self.label.setText(QCoreApplication.translate("SimulationTask3Widget", u"tolerance:", None))
        self.toleranceEdit.setText(QCoreApplication.translate("SimulationTask3Widget", u"1.0e-7", None))
        self.simulateButton.setText(QCoreApplication.translate("SimulationTask3Widget", u"Simulate", None))
        self.clearButton.setText(QCoreApplication.translate("SimulationTask3Widget", u"Clear graph", None))
        self.doneButton.setText(QCoreApplication.translate("SimulationTask3Widget", u"Done", None))
    # retranslateUi

