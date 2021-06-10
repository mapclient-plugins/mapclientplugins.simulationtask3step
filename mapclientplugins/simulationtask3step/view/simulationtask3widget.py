'''
Created on May 26, 2015

@author: andre
'''
from PySide2 import QtCore, QtWidgets

import matplotlib
matplotlib.use('Qt4Agg')
matplotlib.rcParams['backend.qt4']='PySide'

from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)

from matplotlib.figure import Figure
from matplotlib.backend_bases import key_press_handler

from mapclientplugins.simulationtask3step.view.ui_simulationtask3widget import Ui_SimulationTask3Widget
from mapclientplugins.simulationtask3step.sedml.execute import ExecuteSedml

class SimulationTask3Widget(QtWidgets.QWidget):
    '''
    classdocs
    '''


    def __init__(self, parent=None):
        '''
        Constructor
        '''
        super(SimulationTask3Widget, self).__init__(parent)
        self._ui = Ui_SimulationTask3Widget()
        self._ui.setupUi(self)
        self.sedml = ExecuteSedml()
        # create the plot
        self.fig = Figure((5.0, 4.0), dpi=100)
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self._ui.plotPane)
        self.canvas.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.canvas.setFocus()
        self.mpl_toolbar = NavigationToolbar(self.canvas, self._ui.plotPane)
        self.canvas.mpl_connect('key_press_event', self.on_key_press)

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.canvas)  # the matplotlib canvas
        vbox.addWidget(self.mpl_toolbar)
        self._ui.plotPane.setLayout(vbox)
        #self.setCentralWidget(self.main_frame)

        self.createAxes()
        self._makeConnections()

    def createAxes(self):
        self.axes = self.fig.add_subplot(111)
        self.canvas.draw()
        
    def setSimulationRoot(self, location):
        self.sedml.setSimulationRoot(location)

    def _makeConnections(self):
        self._ui.doneButton.clicked.connect(self._doneButtonClicked)
        self._ui.simulateButton.clicked.connect(self._simulateButtonClicked)
        self._ui.clearButton.clicked.connect(self._clearButtonClicked)
        
    def on_key_press(self, event):
        # implement the default mpl key press events described at
        # http://matplotlib.org/users/navigation_toolbar.html#navigation-keyboard-shortcuts
        key_press_handler(event, self.canvas, self.mpl_toolbar)

    def _simulateButtonClicked(self):
        h = self._ui.stepSizeEdit.text()
        tol = self._ui.toleranceEdit.text()
        results = self.sedml.execute(h, tol)
        if results == None:
            return
        #print results	
        #print data
        #print data.shape
        #print data.dtype.names
        #print data['X']
        #self.axes.plot(data['X'], data['sinX'], label='sin(x)')
        title = "h=" + str(h) + "; tol=" + str(tol) + "; time=" + str(results['time'])
        self.axes.plot(results['data']['t'], results['data']['Vm'], label=title)
        self.axes.legend()
        self.canvas.draw()
    
    def _clearButtonClicked(self):
        self.fig.clear()
        self.createAxes()
                        
    def initialise(self):
        print("Initialise called?")
        
    def registerDoneExecution(self, callback):
        self._callback = callback
        
    def _doneButtonClicked(self):
        self._callback()
        

