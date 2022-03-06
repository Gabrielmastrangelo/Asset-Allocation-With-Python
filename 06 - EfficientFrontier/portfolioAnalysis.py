import pandas as pd
import numpy as np
import math

from scipy.stats import norm
def var_gaussian(r, level=5, modified=False):
    """
    Returns the Parametric Gauusian VaR of a Series or DataFrame
    If "modified" is True, then the modified VaR is returned,
    using the Cornish-Fisher modification
    """
    # compute the Z score assuming it was Gaussian
    z = norm.ppf(level/100)
    if modified:
        # modify the Z score based on observed skewness and kurtosis
        s = skewness(r)
        k = kurtosis(r)
        z = (z +
                (z**2 - 1)*s/6 +
                (z**3 -3*z)*(k-3)/24 -
                (2*z**3 - 5*z)*(s**2)/36
            )
    return -(r.mean() + z*r.std(ddof=0))

def annualize_rets(r, periods_per_year = 252):
    '''
    The function receives a time series returns and convert them into ln(1 + r),
    sum them, and then exponentiate back.
    '''
    compounded_growth = np.expm1(np.log1p(r).sum())
    n_periods = r.shape[0]
    return compounded_growth**(periods_per_year/n_periods)-1