# OeQ autogenerated correlation for 'Buildings with n flats in correlation to year of construction'

import math
import numpy as np
def get(xin,mode='distribution'):

    # OeQ autogenerated correlation for 'Buildings with housing with 1 flat'
    Const= 247055.261409
    a=     -513.819131456
    b=     0.400679806649
    c=     -0.000138848340627
    d=     1.80407208943e-08
    x=xin
    BLD_NOFLAT_1 = Const + a*x + b*x**2 + c*x**3 + d*x**4
    # OeQ autogenerated correlation for 'Buildings with housing with 2 flats'
    Const= -220246.523398
    a=     457.624556753
    b=     -0.356503709409
    c=     0.00012341286256
    d=     -1.60181667963e-08
    x=xin
    BLD_NOFLAT_2 = Const + a*x + b*x**2 + c*x**3 + d*x**4
    # OeQ autogenerated correlation for 'Buildings with housing with 3 up to 6 flats'
    Const= -31263.8398908
    a=     65.3377958886
    b=     -0.0512059030339
    c=     1.78358005629e-05
    d=     -2.32966026258e-09
    x=xin
    BLD_NOFLAT_3TO6 = Const + a*x + b*x**2 + c*x**3 + d*x**4
    # OeQ autogenerated correlation for 'Buildings with housing with 7 up to 12 flats'
    Const=  5622.5437551
    a=     -11.5972409384
    b=     0.00896544543769
    c=     -3.07872116351e-06
    d=     3.96245494764e-10
    x=xin
    BLD_NOFLAT_7TO12 = Const + a*x + b*x**2 + c*x**3 + d*x**4
    # OeQ autogenerated correlation for 'Buildings with housing with more than 13 flats'
    Const= -1166.44187501
    a=     2.45401975352
    b=     -0.00193563964345
    c=     6.7839866757e-07
    d=     -8.91393301815e-11
    x=xin
    BLD_NOFLAT_MTH13 = Const + a*x + b*x**2 + c*x**3 + d*x**4
 
    l_sum = BLD_NOFLAT_1 + BLD_NOFLAT_2 + BLD_NOFLAT_3TO6 + BLD_NOFLAT_7TO12 + BLD_NOFLAT_MTH13
    if mode is 'distribution':
        return {'BLD_NOFLAT_1' : BLD_NOFLAT_1/l_sum, 'BLD_NOFLAT_2' : BLD_NOFLAT_2/l_sum, 'BLD_NOFLAT_3TO6' : BLD_NOFLAT_3TO6/l_sum, 'BLD_NOFLAT_7TO12' : BLD_NOFLAT_7TO12/l_sum, 'BLD_NOFLAT_MTH13' : BLD_NOFLAT_MTH13/l_sum}

    return(BLD_NOFLAT_1/l_sum * 1 + BLD_NOFLAT_2/l_sum * 2 + BLD_NOFLAT_3TO6/l_sum * 4.5 + BLD_NOFLAT_7TO12/l_sum * 9.5 + BLD_NOFLAT_MTH13/l_sum * 20 )


