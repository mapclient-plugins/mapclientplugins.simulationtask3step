from string import Template
from subprocess import call
import numpy as np
from timeit import timeit
import tempfile
import sys
import os
import pathlib


class ExecuteSedml():

    def __init__(self, parent=None):
        self._simulation_root = None

    def setSimulationRoot(self, location):
        self._simulation_root = location
        
    def execute(self, stepSize, tolerance):
        '''
        http://stackoverflow.com/questions/6385686/python-technique-or-simple-templating-system-for-plain-text-output
        '''

        # Create our SED-ML file from the template with the given step size
        # open the file
        template_file = os.path.join(self._simulation_root, 'sed-ml-templates', 'ICC-model-simulation-tolerances.xml')
        filein = open(template_file)
        # read it
        src = Template(filein.read())
        # document data
        source_model = os.path.join(self._simulation_root, 'pmr2', 'faville_pullan_sanders_koh_lloyd_smith_2009',
                                    'faville_model_2008.cellml')
        model_url = pathlib.Path(source_model).as_uri()
        d = {'MAX_STEP_SIZE': stepSize, 'TOLERANCE_VALUE': tolerance, 'SOURCE_MODEL': model_url}
        # do the substitution
        result = src.substitute(d)
        tmpFile = tempfile.NamedTemporaryFile(delete=False)
        tmpFile.write(result.encode())
        tmpFile.flush()

        # execute the simulation experiment
        resultsFile = tempfile.NamedTemporaryFile(delete=False)
        sedmlDocument = pathlib.Path(tmpFile.name).as_uri()

        tmpFile.close()
        resultsFile.close()
        exeFile = os.path.join(self._simulation_root, 'bin', 'get-sed-ml-client-' + sys.platform)
        call_args = "[r'%s',r'%s',r'%s']" % (exeFile, sedmlDocument, resultsFile.name)
        timeTaken = timeit(stmt="returnCode = subprocess.call(%s)" % call_args, setup="import subprocess", number=1)
        # FIXME: get return code back?
        # if returnCode != 0:
        #	return None
        data = np.genfromtxt(resultsFile.name, dtype=float, delimiter=',', names=True)
        r = {'time': timeTaken, 'data': data}

        os.remove(resultsFile.name)
        os.remove(tmpFile.name)

        return r
