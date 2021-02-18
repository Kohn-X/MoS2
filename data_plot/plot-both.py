import os.path
import numpy as np
from matplotlib import rc
from pylab import *
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm
from matplotlib.font_manager import FontProperties
from matplotlib.ticker import AutoMinorLocator, MultipleLocator
from scipy.interpolate import interp1d
from scipy.ndimage.interpolation import map_coordinates
import matplotlib.pyplot as plt

#define font as serif! this font is good.
rc('font',family='times new roman')
#rc('font',family='serif', serif='times new roman')
rcParams['mathtext.fontset'] = 'stix' #'custom'
#rc('font', serif='times new roman')
# adjust the distance between tick and ticklabels
# set before the figure is created
rcParams['xtick.major.pad'] = 10
rcParams['ytick.major.pad'] = 10

###===================================================================================
def plotboth(ax,path0,path1,low,high,xticknum,xtickname,yticknum,ytickname,ylabel,title):
	
	bands0 = np.load(path0).T      ### plot VASP band
	print("Plot band from EIGENVAL")

	nbnd0,nkpt0 = bands0.shape
	nbnd0 = nbnd0-1
	
	for i in range(nbnd0):
		if min(bands0[i+1])>high or max(bands0[i+1])<low:
			pass
		else:
			line0,=ax.plot(bands0[0],bands0[i+1],color='r',lw=1.5)

	bands = np.loadtxt(path1).T     ### plot Questaal band
	nbnd,nkpt = bands.shape
	nbnd = nbnd-1
	
	for i in range(nbnd):
		if min(bands[i+1])>high or max(bands[i+1])<low:
			pass
		else:
			line1,=ax.plot(bands[0],bands[i+1]*13.6,color='b',lw=1.5)

	leg = ax.legend((line0,line1),('PAW-VASP','LMTO-FP'),loc=10,ncol=2,prop={'size':16},\
	bbox_to_anchor=(0.50,0.55),columnspacing=0.8,handlelength=0.8,handletextpad=0.1,frameon=False)

	xticknum = bands[0,xticknum]
	ax.set_xticks(xticknum)
	ax.set_xticklabels(xtickname,fontsize='20')
	ax.set_yticks(yticknum)
	ax.set_yticklabels(ytickname,fontsize='20')
	
	ax.set_xlim(bands[0,0],bands[0,-1])
	ax.set_ylim(low,high)
	ax.set_ylabel(ylabel,fontsize='25')
	ax.yaxis.set_label_coords(-0.12,0.5)

	ax.set_title(title,y=1.02,fontsize='20')
	
	for i in xticknum[1:len(xticknum)-1]:
		ax.axvline(i,color='k',ls=':',lw=1)
	
	ax.axhline(0,color='k',ls=':',lw=1)

###===================================================================================
fig = plt.figure(figsize=(4,6))
ax = fig.add_axes([0.20,0.1,0.75,0.8])

path0='./VASP_EBAND.npy'
path1='./questaal_bands.txt'

low = -3                  # energy interval
high = 4

yticknum=[-3,-2,-1,0,1,2,3,4]
ytickname = map(str,yticknum)
ylabel = 'E$\minus$E$_\mathrm{F}$ (eV)'

xticknum = [0,40,80,119]
xtickname = ['M','K','$\Gamma$','M']

title='MoS$_2$'

plotboth(ax,path0,path1,low,high,xticknum,xtickname,yticknum,ytickname,ylabel,title)

plt.show()
