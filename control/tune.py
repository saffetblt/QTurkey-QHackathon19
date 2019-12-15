import numpy as np
import sys

def tune_twiddle(params, costfunction, dparams=None, eps=0.001):

    if dparams is None:
        dparams = dict((key, 1.) for (key, _) in params.items())

    errprev = sys.float_info.max
    err = sys.float_info.max / 2

    while (errprev - err) > eps:
        errprev = err

        for k in params.keys():
            params[k] += dparams[k]
            e = costfunction(params)

            if e < err:
                err = e
                dparams[k] *= 1.1
            else:
                params[k] -= 2 * dparams[k]
                e = costfunction(params)

                if e < err:
                    err = e
                    dparams[k] *= 1.1
                else:
                    params[k] += dparams[k]
                    dparams[k] *= 0.95
    
    return params