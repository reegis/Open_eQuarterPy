# OeQ autogenerated correlation for 'Building Heating Type Distribution in Correlation to the population density'

import math
import numpy as np
from . import oeqCorrelation as oeq
def get(*xin):

    # OeQ autogenerated correlation for 'Buildings with housing heated by district heating systems'
    BLD_HEAT_DISTR= oeq.correlation(
    const= -0.0497312239063,
    a=     0.0751958286351,
    b=     -0.028394997478,
    c=     0.00423665454622,
    d=     -0.000197740004603,
    mode= "log")
    # OeQ autogenerated correlation for 'Buildings with housing heated by self-contained heating systems'
    BLD_HEAT_SCDWELL= oeq.correlation(
    const= -0.0645092636623,
    a=     0.0926296333828,
    b=     -0.0320120926992,
    c=     0.0044015816766,
    d=     -0.000189576081619,
    mode= "log")
    # OeQ autogenerated correlation for 'Buildings with housing heated by block-type combined heat and power plants'
    BLD_HEAT_BLOCKTYPE= oeq.correlation(
    const= -0.00464954316969,
    a=     0.0109703900193,
    b=     -0.00348569366698,
    c=     0.000400127580116,
    d=     -1.15620456969e-05,
    mode= "log")
    # OeQ autogenerated correlation for 'Buildings with housing heated by central heating systems'
    BLD_HEAT_CENTRAL= oeq.correlation(
    const= 1.39552942759,
    a=     -0.68286525874,
    b=     0.24404894017,
    c=     -0.0338635816392,
    d=     0.00159286982264,
    mode= "log")
    # OeQ autogenerated correlation for 'Buildings with housing heated by single room heating systems including stoves and night storage heaters'
    BLD_HEAT_SNGLROOM= oeq.correlation(
    const= 0.0827660836629,
    a=     0.0966309375396,
    b=     -0.0357244881851,
    c=     0.00432678548534,
    d=     -0.000180797989534,
    mode= "log")
    # OeQ autogenerated correlation for 'Buildings w/ housing without heating systems'
    BLD_HEAT_NONE= oeq.correlation(
    const= -0.0276354062692,
    a=     0.0426818409654,
    b=     -0.0141287580667,
    c=     0.0018078400496,
    d=     -8.11193054339e-05,
    mode= "log")

    return dict(BLD_HEAT_DISTR=BLD_HEAT_DISTR.lookup(*xin),
    BLD_HEAT_SCDWELL=BLD_HEAT_SCDWELL.lookup(*xin),
    BLD_HEAT_BLOCKTYPE=BLD_HEAT_BLOCKTYPE.lookup(*xin),
    BLD_HEAT_CENTRAL=BLD_HEAT_CENTRAL.lookup(*xin),
    BLD_HEAT_SNGLROOM=BLD_HEAT_SNGLROOM.lookup(*xin),
    BLD_HEAT_NONE=BLD_HEAT_NONE.lookup(*xin))

