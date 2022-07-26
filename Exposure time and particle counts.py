############################################################################
# for an experiment where measurements were taken to see if having smaller exposure times affected the amount of data collected
# one set of data was based off of real world time and the other was based off of the number of frames times by their exposure time (i.e. ignoring the dead time inbetween)
# this plots the data for both and compares them, the data values are writen in by hand
############################################################################

import matplotlib.pyplot as plt

# create arrays of data, each data point represents a distance i.e. the first data point corresponds to x=.05, the second point to x=.1 etc.
x =     [.05, .1, .2, .3]
tot_t = [196,250,282,277]
alp_t = [ 35, 40, 41, 37]
ele_t = [ 59, 92, 98,101]
muo_t = [ 11, 18, 18, 16]
dot_t = [ 91,100,125,123]

y_t = [tot_t, dot_t, ele_t, alp_t, muo_t]
lab = ["Total","Dot","Electron","Alpha","Muon"]
col = ["royalblue","orange","green","red","purple"]

# plot the data in subplot
plt.figure(figsize=(15,4))
plt.subplot(1,3,1)
for z in range(len(y_t)):
    plt.plot(x, y_t[z], label=lab[z], color=col[z])

plt.xlim(0.05,0.3)
plt.ylim(0,325)
plt.xlabel("Exposure Time (s)")
plt.ylabel("Number of Particles Detected")
plt.legend(loc="upper left")
plt.title("Based on Time")
plt.tight_layout()


# repeat for other data
tot_f = [285,311,286,291]
alp_f = [ 36, 44, 32, 37]
ele_f = [102,111,102,104]
muo_f = [ 26, 26, 16, 24]
dot_f = [121,130,136,126]

y_f = [tot_f, dot_f, ele_f, alp_f, muo_f]

plt.subplot(1,3,2)
for z in range(len(y_t)):
    plt.plot(x, y_f[z], label=lab[z], color=col[z])

plt.xlim(0.05,0.3)
plt.ylim(0,325)
plt.xlabel("Exposure Time (s)")
plt.ylabel("Number of Particles Detected")
plt.legend(loc="upper left")
plt.title("Based on Frames")
plt.tight_layout()


# plot both sets of data together for comparison
plt.subplot(1,3,3)

for z in range(len(y_t)):
    plt.plot(x, y_t[z], color=col[z],linestyle="-")
    plt.plot(x, y_f[z], color=col[z],linestyle="--")

xlab, ylab = -1, -1
plt.plot(xlab, ylab, label="Frame", color="k", linestyle="--")
plt.plot(xlab, ylab, label="Time", color="k", linestyle="-")

plt.xlim(0.05,0.3)
plt.ylim(0,325)
plt.xlabel("Exposure Time (s)")
plt.ylabel("Number of Particles Detected")
plt.legend(loc="upper left")
plt.title("Comparison")
plt.tight_layout()

plt.savefig("Graph", dpi=200)