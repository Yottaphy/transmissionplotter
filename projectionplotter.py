import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

def avg(listin):
    tot = 0
    n   = 0
    for i in range(len(listin)):
        if listin[i] != 0:
            n   += 1
            tot += listin[i]
    return tot/n


def column(matrix, i):
    return [row[i] for row in matrix]

filein = np.loadtxt("Optimal/NewGeometry/widerange_notopt.txt" , dtype='i')

nrows = 21
ncols = 15

z = np.zeros((nrows,ncols))
srfq = []
brfq = list(filein[0])
brfq.pop(0)

for i in range(1,nrows+1):
    srfq.append(filein[i][0])
    for j in range(1,ncols+1):
        z[i-1][ncols-j] = filein[i][j]

colmax = []
rowmax = []
for i in range(0,max(nrows,ncols)):
    if i < ncols:
        colmax.append(max(column(z,i)))
    if i < nrows:
        rowmax.append(max(list(z[i])))
colmax = colmax[::-1]


colavg = []
for i in range(0,ncols):
    colavg.append(avg(column(z,i)))

plt.rcParams['font.size'] = 18

He = [77,90,85,90,91,96,95,94,91,88,92,91,90,87,92,88,86,87,85,70,0]
Vac = [0,0,0,25,67,51,27,65,64,71,33,80,86,28,10,2,11,0,0,0,0]
Ar = []

fig2, axproj = plt.subplots()
axproj.plot(srfq, He, color='red', label = "Helium")
axproj.plot(srfq, Vac, color='green', label = "Vacuum")
axproj.set_xlim(0,400)
axproj.set_ylim(0,100)
axproj.set_aspect(2.2)
axproj.tick_params(top=True, right=True,direction='in')
axproj.set_xlabel("Bend RFQ Voltage Amplitude [V]")
axproj.set_ylabel("Transmission [%]")
axproj.legend(fontsize='x-small', loc=8, frameon=True,fancybox=True,framealpha=1)
# axproj.set_title("Transmission at 30 V Straight RFQ Voltage")
plt.savefig("projection.pdf", bbox_inches = 'tight', pad_inches = 0.1, transparent=True)
plt.savefig("projection.png", bbox_inches = 'tight', pad_inches = 0.1)