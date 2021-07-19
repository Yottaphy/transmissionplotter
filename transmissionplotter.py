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

filename = 'Optimal/NewGeometry/newgeo_argon_opt'

filein = np.loadtxt(filename+".txt" , dtype='f')

thecolor = 'Blue'
nrows = 23
ncols = 23

z = np.zeros((nrows,ncols))
brfq = []
srfq = list(filein[0])
srfq.pop(0)

for i in range(1,nrows+1):
    brfq.append(filein[i][0])
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

# colavg = []
# for i in range(0,ncols):
#     colavg.append(avg(column(z,i)))

plt.rcParams['font.size'] = 18

fig = plt.figure(figsize=(20, 15))
gs = gridspec.GridSpec(10, 12)
ax0 = plt.subplot(gs[6:10, 5:9])
axx = plt.subplot(gs[5:6, 5:9])
axy = plt.subplot(gs[6:10, 9:10])
axtop = plt.subplot(gs[4:5, 5:10])
axtop.set_visible(False)

axy.plot(rowmax, brfq, color=thecolor)
axy.set_ylim(min(brfq),max(brfq))
axy.set_xlim(0,105)
axy.yaxis.set_ticklabels([])

axx.plot(srfq, colmax, color=thecolor)
axx.set_xlim(min(srfq),max(srfq))
axx.xaxis.set_ticklabels([])

az = ax0.imshow(z, extent=[min(srfq), max(srfq), min(brfq),max(brfq)], aspect='auto', cmap = thecolor+'s')
# az = ax0.contourf(z, extent=[min(brfq), max(brfq), max(srfq),  min(srfq)], cmap = 'Blues', origin = "lower")
# ax0.contour(z, extent=[min(brfq), max(brfq), max(srfq),  min(srfq)], colors = 'k', origin = "lower", linewidths=0.4)

ax0.set_xlabel("Straight RFQ Voltage Amplitude [V]")
ax0.set_ylabel("Bend RFQ Voltage Amplitude [V]")
clb = fig.colorbar(az, ax=axtop, orientation = 'horizontal', aspect = 50)
clb.set_label("Transmission [%]", loc = 'center')
clb.ax.xaxis.set_ticks_position('top')
clb.ax.xaxis.set_label_position('top')

plt.savefig(filename+".pdf", bbox_inches = 'tight', pad_inches = 0.1, transparent=True)
plt.savefig(filename+".png", bbox_inches = 'tight', pad_inches = 0.1)