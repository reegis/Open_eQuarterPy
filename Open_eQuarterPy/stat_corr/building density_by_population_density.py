# OeQ autogenerated correlation for 'Building Density in Correlation to the Population Density'

import math
import numpy as np
def building_density_by_population_density(xin,mode='distribution'):

    # OeQ autogenerated correlation for 'Density of buildings'
    Const= 3.01748429717
    a=     0.28965188502
    b=     -6.37219457945e-05
    c=     6.06666442362e-09
    x=xin
    BLD_DENS = Const + a*x + b*x**2 + c*x**3
 
    l_sum = BLD_DENS
    if mode is 'distribution':
        return {'BLD_DENS' : BLD_DENS/l_sum}

    return(BLD_DENS/l_sum * 1850 )


