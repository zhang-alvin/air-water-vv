from proteus.default_p import *
from proteus.ctransportCoefficients import smoothedHeaviside
from proteus.mprans import VOF
from proteus import Context

ct = Context.get()
domain = ct.domain
nd = domain.nd
genMesh = ct.genMesh
movingDomain = ct.movingDomain
T = ct.T

LevelModelType = VOF.LevelModel
if ct.useOnlyVF:
    RD_model = None
    LS_model = None
else:
    RD_model = 3
    LS_model = 2

coefficients = VOF.Coefficients(LS_model=int(ct.movingDomain)+LS_model,
                                V_model=int(ct.movingDomain)+0,
                                RD_model=int(ct.movingDomain)+RD_model,
                                ME_model=int(ct.movingDomain)+1,
                                checkMass=False,
                                useMetrics=ct.useMetrics,
                                epsFact=ct.epsFact_vof,
                                sc_uref=ct.vof_sc_uref,
                                sc_beta=ct.vof_sc_beta,
                                movingDomain=ct.movingDomain)


dirichletConditions = {0: lambda x, flag: domain.bc[flag].vof_dirichlet}

advectiveFluxBoundaryConditions = {0: lambda x, flag: domain.bc[flag].vof_advective}

diffusiveFluxBoundaryConditions = {0: {}}
                       

class VF_IC:
    def uOfXT(self,x,t):
        return smoothedHeaviside(ct.epsFact_consrv_heaviside*ct.he,ct.signedDistance(x))
	    
initialConditions  = {0: VF_IC()}
