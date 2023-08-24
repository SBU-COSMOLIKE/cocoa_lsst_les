import getdist.plots as gplot
from getdist import MCSamples
from getdist import loadMCSamples
import os
import matplotlib
import subprocess
import matplotlib.pyplot as plt
import numpy as np

# GENERAL PLOT OPTIONS
matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'
matplotlib.rcParams['mathtext.rm'] = 'Bitstream Vera Sans'
matplotlib.rcParams['mathtext.it'] = 'Bitstream Vera Sans:italic'
matplotlib.rcParams['mathtext.bf'] = 'Bitstream Vera Sans:bold'
matplotlib.rcParams['xtick.bottom'] = True
matplotlib.rcParams['xtick.top'] = False
matplotlib.rcParams['ytick.right'] = False
matplotlib.rcParams['axes.edgecolor'] = 'black'
matplotlib.rcParams['axes.linewidth'] = '1.0'
matplotlib.rcParams['axes.labelsize'] = 'medium'
matplotlib.rcParams['axes.grid'] = True
matplotlib.rcParams['grid.linewidth'] = '0.0'
matplotlib.rcParams['grid.alpha'] = '0.18'
matplotlib.rcParams['grid.color'] = 'lightgray'
matplotlib.rcParams['legend.labelspacing'] = 0.77
matplotlib.rcParams['savefig.bbox'] = 'tight'
matplotlib.rcParams['savefig.format'] = 'pdf'

parameter = [u'omegam',u'sigma8', u'As_1e9', u'ns', u'SS8', u'omegab', u'H0', u'LSST_A1_1', u'LSST_A1_2']
chaindir=os.getcwd()

analysissettings={'smooth_scale_1D':0.35,'smooth_scale_2D':0.35,'ignore_rows': u'0.5',
'range_confidence' : u'0.01'}

analysissettings2={'smooth_scale_1D':0.35,'smooth_scale_2D':0.35,'ignore_rows': u'0.0',
'range_confidence' : u'0.01'}

root_chains = (
  'EXAMPLE_MCMC16',
  'EXAMPLE_MCMC17',
  'EXAMPLE_MCMC18'
)


# --------------------------------------------------------------------------------
samples=loadMCSamples(chaindir + '/../chains/' + root_chains[0],settings=analysissettings)
p = samples.getParams()
samples.addDerived(p.omegam*p.H0/100.,name='gamma',label='{\\Omega_m h}')
samples.addDerived(p.s8omegamp5/0.5477225575,name='SS8',label='{S_8}')
samples.saveAsText(chaindir + '/.VM_P2_TMP1')
# --------------------------------------------------------------------------------
samples=loadMCSamples(chaindir + '/../chains/' + root_chains[1],settings=analysissettings)
p = samples.getParams()
samples.addDerived(p.omegam*p.H0/100.,name='gamma',label='{\\Omega_m h}')
samples.addDerived(p.s8omegamp5/0.5477225575,name='SS8',label='{S_8}')
samples.saveAsText(chaindir + '/.VM_P2_TMP2')
# --------------------------------------------------------------------------------
samples=loadMCSamples(chaindir + '/../chains/' + root_chains[2],settings=analysissettings2)
p = samples.getParams()
samples.addDerived(p.omegam*p.H0/100.,name='gamma',label='{\\Omega_m h}')
samples.addDerived(p.s8omegamp5/0.5477225575,name='SS8',label='{S_8}')
samples.saveAsText(chaindir + '/.VM_P2_TMP3')
# --------------------------------------------------------------------------------

#GET DIST PLOT SETUP
g=gplot.getSubplotPlotter(chain_dir=chaindir,analysis_settings=analysissettings2,width_inch=9.5)
g.settings.axis_tick_x_rotation=65
g.settings.lw_contour = 1.2
g.settings.legend_rect_border = False
g.settings.figure_legend_frame = False
g.settings.axes_fontsize = 13.0
g.settings.legend_fontsize = 13.5
g.settings.alpha_filled_add = 0.85
g.settings.lab_fontsize=15.5
g.legend_labels=False

param_3d = None
g.triangle_plot([chaindir + '/.VM_P2_TMP1', 
                 chaindir + '/.VM_P2_TMP2',
                 chaindir + '/.VM_P2_TMP3'],
parameter,
plot_3d_with_param=param_3d,line_args=[
{'lw': 1.2,'ls': 'solid', 'color':'lightcoral'},
{'lw': 1.2,'ls': '--', 'color':'black'},
{'lw': 1.6,'ls': '-.', 'color': 'maroon'},
{'lw': 1.6,'ls': 'solid', 'color': 'indigo'},
],
contour_colors=['lightcoral','black','maroon','indigo'],
contour_ls=['solid','--','-.'], 
contour_lws=[1.0,1.5,1.5,1.0],
filled=[True,False,False,True],
shaded=False,
legend_labels=[
'LSST-Y3 3x2pt LES M1 Scale Cuts',
'LSST-Y3 3x2pt LES M2 Scale Cuts',
'LSST-Y3 3x2pt LES M3 Scale Cuts',
],
legend_loc=(0.48, 0.80))

g.export()