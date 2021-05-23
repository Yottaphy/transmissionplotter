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

filein = np.loadtxt("nogaschamfer2.txt" , dtype='i')

z = np.zeros((20,20))
srfq = []
brfq = list(filein[0])
brfq.pop(0)

for i in range(1,21):
    srfq.append(filein[i][0])
    for j in range(1,21):
        z[i-1][20-j] = filein[i][j]

colmax = []
rowmax = []
for i in range(0,20):
    colmax.append(max(column(z,i)))
    rowmax.append(max(list(z[i])))
colmax = colmax[::-1]


colavg = []
for i in range(0,20):
    colavg.append(avg(column(z,i)))

plt.rcParams['font.size'] = 18

fig = plt.figure(figsize=(20, 15))
gs = gridspec.GridSpec(10, 12)
ax0 = plt.subplot(gs[6:10, 5:9])
axx = plt.subplot(gs[5:6, 5:9])
axy = plt.subplot(gs[6:10, 9:10])
axtop = plt.subplot(gs[4:5, 5:10])
axtop.set_visible(False)
axy.plot(rowmax, srfq)
axx.plot(brfq,colmax)
axy.set_ylim(0,250)
axy.yaxis.set_ticklabels([])
axx.set_xlim(0,70)
axx.xaxis.set_ticklabels([])
az = ax0.imshow(z, extent=[min(brfq), max(brfq), min(srfq),max(srfq)], aspect='auto', cmap = 'Blues')
# az = ax0.contourf(z, extent=[min(brfq), max(brfq), max(srfq),  min(srfq)], cmap = 'Blues', origin = "lower")
# ax0.contour(z, extent=[min(brfq), max(brfq), max(srfq),  min(srfq)], colors = 'k', origin = "lower", linewidths=0.4)
ax0.set_xlabel("Straight RFQ Voltage Amplitude [V]")
ax0.set_ylabel("Bend RFQ Voltage Amplitude [V]")
clb = fig.colorbar(az, ax=axtop, orientation = 'horizontal', aspect = 50)
clb.set_label("Transmission [%]", loc = 'center')
clb.ax.xaxis.set_ticks_position('top')
clb.ax.xaxis.set_label_position('top')

plt.savefig("nogas_2cham.pdf", bbox_inches = 'tight', pad_inches = 0.1, transparent=True)
plt.savefig("nogas_2cham.png", bbox_inches = 'tight', pad_inches = 0.1, transparent=True)