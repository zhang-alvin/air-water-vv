import os
from proteus.default_so import *
from proteus import Context


# Create context from main module
name_so = os.path.basename(__file__)
if '_so.py' in name_so[-6:]:
    name = name_so[:-6]
elif '_so.pyc' in name_so[-7:]:
    name = name_so[:-7]
else:
    raise NameError, 'Split operator module must end with "_so.py"'

try:
    case = __import__(name)
    Context.setFromModule(case)
    ct = Context.get()
except ImportError:
    raise ImportError, str(name) + '.py not found'

pnList = [("vof_p",               "vof_n"),#0
          ("ls_p",                "ls_n"),#1
          ("redist_p",            "redist_n"),#2
          ("ls_consrv_p",         "ls_consrv_n"),#3
          ("twp_navier_stokes_p", "twp_navier_stokes_n"),#4
          ("pressureincrement_p", "pressureincrement_n"),#5
          ("pressure_p", "pressure_n"),#6
          ("pressureInitial_p", "pressureInitial_n")]#7

modelSpinUpList = [ct.PINIT_model]

name = ct.name 

class Sequential_MinAdaptiveModelStepPS(Sequential_MinAdaptiveModelStep):
    def __init__(self,modelList,system=defaultSystem,stepExact=True):
        Sequential_MinAdaptiveModelStep.__init__(self,modelList,system,stepExact)
        self.modelList = modelList[:len(pnList)-1]

systemStepControllerType = Sequential_MinAdaptiveModelStepPS

needEBQ_GLOBAL = False
needEBQ = False

tnList = [0.0,ct.dt_init]+[i*ct.dt_fixed for i in range(1,ct.nDTout+1)] 


