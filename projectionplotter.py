import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use("science")
import matplotlib.gridspec as gridspec


def avg(listin):
    tot = 0
    n = 0
    for i in range(len(listin)):
        if listin[i] != 0:
            n += 1
            tot += listin[i]
    return tot / n


def column(matrix, i):
    return [row[i] for row in matrix]


fileHe = np.loadtxt("Optimal/NewGeometry/widerange_notopt.txt", dtype="f")
fileVac = np.loadtxt("Optimal/NewGeometry/newgeo_vacuum1k.txt", dtype="f")
# fileAr = np.loadtxt("Optimal/NewGeometry/widerange_notopt.txt" , dtype='f')

nrows = 21
ncols = 15
col30 = 7

He = np.zeros((nrows, ncols))
Vac = np.zeros((nrows, ncols))
Ar = np.zeros((nrows, ncols))
brfq = []
srfq = list(fileHe[0])
srfq.pop(0)

for i in range(1, nrows + 1):
    brfq.append(fileHe[i][0])
    for j in range(1, ncols + 1):
        He[i - 1][ncols - j] = fileHe[i][j]
        Vac[i - 1][ncols - j] = fileVac[i][j]
        # Ar[i-1][ncols-j] = fileAr[i][j]

# Plot only column for which SRFQ=30 V
plotHe = []
plotVac = []
plotOther = []
# plotAr = []

for i in range(0, nrows):
    plotHe.append(He[i][col30 - 1])
    plotVac.append(Vac[i][col30 - 1])
    # plotOther.append(Vac[i][-1])
    # plotAr.append(Ar[i][col30-1])

print(plotVac)

plt.rcParams["font.size"] = 18

fig, axproj = plt.subplots()
axproj.plot(brfq, plotVac, color="Green", label="Vacuum")
axproj.plot(brfq, plotHe, color="Red", label="Helium")
# axproj.plot(brfq, plotOther, color='Orange', label = "Vacuum @ 70 V SRFQ")
# axproj.plot(brfq, plotAr, color='Blue', label = "Argon")
axproj.set_xlim(0, 410)
axproj.set_ylim(0, 100)
axproj.set_aspect(2.2)
axproj.tick_params(top=True, right=True, direction="in")
axproj.set_title("Straight RFQ Voltage Amplitude 30V")
axproj.set_xlabel("Bend RFQ Voltage Amplitude [V]")
axproj.set_ylabel("Transmission [%]")
fig.legend(fontsize="x-small", loc=1, frameon=True, fancybox=True, framealpha=1)
# axproj.set_title("Transmission at 30 V Straight RFQ Voltage")
plt.savefig(
    "projection_science.pdf", bbox_inches="tight", pad_inches=0.1, transparent=True
)
