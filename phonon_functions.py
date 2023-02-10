import numpy as np
from scipy.special import erf, factorial as fac


def gauss(x, center, width, height):
    """Gaussian defined by peak height"""
    return height * np.exp(-1.0 * (x - center)**2 / (2 * width**2))


def one_phonon_at_energy(x, y, center, width):
    """Make a phonon at an specific energy center with a peak height that 
    matches the fit curve x, y"""
    height = np.interp(center, x, y)
    yout = gauss(x, center, width, height)
    return yout


def phononI_offset(x, g, I0, omega0, omegadet, gam, numphonons, res, wid, offset):
    """     # ['g', 'I0', 'omega0', 'omegadet', 'gam', 'numphonons', 'res', 'wid', 'offset']
    """
    import numpy
    
    def Bmn(m,n,g):
        prefac = (-1)**m * numpy.sqrt(numpy.exp(-g) * fac(m) * fac(n) ) 
        sumit = 0
        for l in range(n + 1):
            sumit = sumit + (-g)**l * numpy.sqrt(g)**(m-n) / (fac(n-l) * fac(l) * fac(m - n + l))
        return prefac * sumit
    
    def modeI(np, g, omega0, omegeadet, gam):
        Aq = 0
        for n in range(100):
            Aq = Aq + Bmn(max(np, n), min(np, n), g) * Bmn(n, 0, g) / (omegadet + 1j*gam + (g-n)*omega0 )
        return Aq

    y = 0.0*x
    totwid = numpy.sqrt(res**2 + wid**2)
    for np in range(1, int(numphonons)+1):
        I = modeI(np, g, omega0, omegadet, gam)
        y = y + gauss((x-offset), omega0*np, totwid, I)
    y=numpy.square(abs(y))

    return y/max(y)*I0

def errorfunc(x, lv, hv, jump, swid):
    """errorfunc - corresponding to the integral of a gaussain
        p = [lowval, highval, step_loc, sigma]
        sigma correspond to conv (step, exp(-x^2/(2sigma^2)) )
    """
    y = erf((x - jump )/ np.sqrt(2) / swid ) / 2 + 0.5
    
    out = y * (hv - lv) + lv

    return out