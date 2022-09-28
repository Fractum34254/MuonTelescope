# %%
import scipy.special as sp
import numpy as np
from scipy.integrate import  quad
import matplotlib.pyplot as plt
#plt.style.use("science")

g = 9.81  # m/s²
# pat = 98650; % N/m²
alph = 0.0002  # GeV/(kg/m²)
epsmu = 1
epsK = 850
gam = 1.7
rpi = 0.5731
LambdaPi = 148
LambdaN = 115
rK = 0.0458
LambdaK = 147
ZNpi = 0.08
ZNK = 0.012
ZNN = 0.2609
mmu = 0.1056583755  # GeV/c²
c = 299792458  # m/s


def p1(Emu, theta, pat):
    return epsmu/(Emu*np.cos(theta)+alph*(pat/g))


Apimu = ZNpi*(1-rpi**(gam+1))/(1-rpi)/(1+gam)
AKmu = ZNK*(1-rK**(gam+1))/(1-rK)/(1+gam)
Bpimu = (gam+2)/(gam+1)*(1-rpi**(gam+1))/(1-rpi**(gam+2)) * \
    (LambdaPi-LambdaN)/(LambdaPi*np.log(LambdaPi/LambdaN))
BKmu = (gam+2)/(gam+1)*(1-rK**(gam+1))/(1-rK**(gam+2)) * \
    (LambdaK-LambdaN)/(LambdaK*np.log(LambdaK/LambdaN))


def Smu(theta, Emu, pat): 
    return (LambdaN*np.cos(theta)/(pat/g))**p1(Emu, theta, pat)*(Emu /
                        (Emu+alph*(pat/g)/np.cos(theta)))**(p1(Emu, theta, pat)+gam+1)*sp.gamma(p1(Emu, theta, pat)+1)


def dNdE(Emu, theta, pat):
    N0 = 17000 * Emu ** (-2.7)
    return Smu(theta, Emu, pat)*N0/(1-ZNN)*(Apimu/(1+Bpimu*np.cos(theta)*Emu/epsmu) + 0.635*AKmu/(1+BKmu*np.cos(theta)*Emu/epsK))


pressure = np.linspace(1000, 103000, 100)
# pressure = np.array(98650)
EmuDist = 10 ** np.linspace(0, 4, 200)
# EmuDist = np.logspace(0, 4, base=10, num=100)


# %%
# fig, ax = plt.subplots(subplot_kw={"projection" : "3d"})
fig, ax = plt.subplots()

pressure_mesh, Emu_mesh = np.meshgrid(pressure, EmuDist)
Z = (dNdE(Emu_mesh, 0, pressure_mesh))# ).reshape(200, 10)
# Z = Z * EmuDist.reshape(200,1) ** 3


ax.plot(EmuDist, EmuDist**3 * dNdE(EmuDist, 0, 98650))
# ax.plot_surface( np.log(Emu_mesh), pressure_mesh, np.log(Z))
DN = [quad(lambda emu:dNdE(emu, 0, p), 1, 10**4)[0] for p in pressure]
#%%
#ax.plot(pressure, DN)


ax.set_xscale("log")
ax.set_yscale("log")
plt.title("Calculated muon flux")
plt.xlabel("$E_\mu (GeV)$")
plt.ylabel("$dN_\mu/dE_\mu (cm^{–2}sr^{–1}s^{–1}GeV^{-1})$")
plt.grid()
plt.show()


# %%
