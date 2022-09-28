# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 21:08:24 2022

@author: Philipp
"""

import matplotlib.pyplot as plt
import scipy
import numpy as np

#measured
pressures = [734.2,748.7,804.82,842,986]
coins = [3443+3400+3352,3167+3238,2587,2329+2294,1562+1583+1550]
nr = [3,2,1,2,3]
meanCoin = [i / j for i, j in zip(coins, nr)]
err = [1/np.sqrt(i)*j for i, j in zip(coins, meanCoin)]
#particle data group approximation
press = [714.6,804.35,926.3,1034]
flux = [153.7,129.5,107.16,88.67]
flux = coins[2]/flux[1]*np.array(flux)

fig, ax = plt.subplots()
plot, caps, bars = ax.errorbar(pressures,meanCoin, yerr = err, label="Measurements", fmt='o', color='c')
def func(x,a,b):
    return a*np.exp(b*x)

#optimum: a=104967 b=-0.00502004 c=759.015
popt, pcov = scipy.optimize.curve_fit(func, pressures, meanCoin, p0=[38978.8631,-0.00334030964])
xAx = np.linspace(pressures[0], pressures[-1])
print(str(popt[0]) + "," + str(popt[1]))
ax.plot(xAx, func(xAx,popt[0],popt[1]), label="Measurement fit", color='c')
popt, pcov = scipy.optimize.curve_fit(func, press, flux, p0=[38978.8631,-0.00334030964])
xAx = np.linspace(press[0], press[-1])
ax.plot(xAx, func(xAx,popt[0],popt[1]), label="Adjusted data from particle data group", color='r')
print(str(popt[0]) + "," + str(popt[1]))
plt.title("Measured muons")
plt.xlabel("$Pressure (hPa)$")
plt.ylabel("$Coincidences (-)$")
plt.yscale('log')
plt.legend()
plt.grid()
plt.show()