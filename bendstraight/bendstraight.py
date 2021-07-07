import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

volts, fileVac = np.loadtxt("bs_Vac.txt" , dtype='f', unpack=True)
volts, fileHe = np.loadtxt("bs_He.txt" , dtype='f', unpack=True)
# volts, fileAr = np.loadtxt("bs_Ar.txt" , dtype='f', unpack=True)

plt.rcParams['font.size'] = 18

plt.plot(volts, fileVac, color='green', label= 'Vacuum')
plt.plot(volts, fileHe, color='red', label= 'Helium')
#plt.plot(volts, fileAr, color='blue', label= 'Argon')
plt.xlabel('Voltage Amplitude [V]')
plt.ylabel('Transmission Efficiency [%]')
plt.xlim(0,500)
plt.ylim(0,105)
plt.legend(fontsize='x-small', loc=4, frameon=True,fancybox=True,framealpha=1)
plt.text(330,95,'$V_{BRFQ}=V_{SRFQ}$')

plt.savefig("bendstraight.pdf", bbox_inches = 'tight', pad_inches = 0.1, transparent=True)
plt.savefig("bendstraight.png", bbox_inches = 'tight', pad_inches = 0.1)