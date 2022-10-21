#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 16:28:21 2021

@author: adam
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mesaPlot as mp
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm



####################
#### Question 1 ####
####################

def rad_line(rho,mu):
    return (1/3)*rho + np.log10(3.2e7) - (1/3)*np.log10(mu)
    
def ideal_gas_nr_dege_line(rho,mu,mu_e):
    return (2/3)*rho + np.log10(1.21e5) + np.log10(mu) -(5/3)*np.log10(mu_e)
    
def nr_er_dege_line(mu_e):
    return np.log10(9.7e5 * mu_e)

def ideal_gas_er_dege_line(rho,mu,mu_e):
    return (1/3)*rho + np.log10(1.5e7)+np.log10(mu)-(4/3)*np.log10(mu_e)

path = os.getcwd()
data=mp.MESA()
data.loadHistory(f=path+'/workplace/runs/LOGS_15M')  # insert the appropriate path
data_df_15M = pd.DataFrame(np.array([data.hist.center_h1, data.hist.center_he4 ,data.hist.log_Teff, data.hist.log_L,
                                     data.hist.log_cntr_Rho, data.hist.log_cntr_T, data.hist.center_mu,data.hist.log_Lnuc,
                                     data.hist.pp, data.hist.cno, data.hist.tri_alfa]).T,columns=['center_h1','center_he4',
                                     'log_Teff','log_L','log_cntr_Rho','log_cntr_T', 'center_mu','log_Lnuc', 'pp', 'cno','tri_alfa'])

rho_vals=np.logspace(-8,8,191)
rho_vals=np.log10(rho_vals)

mass_values = np.logspace(0,10,100)
mass_values = np.log10(mass_values)

fig, axs = plt.subplots(figsize=(10,8))
plt.plot(data_df_15M['log_cntr_Rho'],data_df_15M['log_cntr_T'],color = 'green', linewidth=3, linestyle="dashed") # star
plt.plot(data_df_15M[data_df_15M['center_h1']>1e-5]['log_cntr_Rho'],data_df_15M[data_df_15M['center_h1']>1e-5]['log_cntr_T'],color='blue', linewidth=3)
plt.plot(data_df_15M[data_df_15M['tri_alfa']>-1]['log_cntr_Rho'],data_df_15M[data_df_15M['tri_alfa']>-1]['log_cntr_T'],color='red',linewidth=3)


plt.plot(rho_vals, rad_line(rho_vals,1.5), linestyle='dashed',color='black')
plt.axvline(nr_er_dege_line(2), ymin=.0, ymax=0.9, linestyle = '--', color = 'black')
plt.plot(rho_vals[rho_vals<nr_er_dege_line(2)], ideal_gas_nr_dege_line(rho_vals[rho_vals<nr_er_dege_line(2)],1.5,2), linestyle='dashed',color='black')
plt.plot(rho_vals[rho_vals>nr_er_dege_line(2)],ideal_gas_er_dege_line(rho_vals[rho_vals>=nr_er_dege_line(2)],1.5,2),linestyle='dashed',color='black')
plt.xticks(fontsize=15) 
plt.yticks(fontsize=15)
plt.xlabel(r'$log \rho_{c} \; (\frac{g}{cm^3}$)', fontsize=16)
plt.ylabel(r'$log T_{c} \; (K)$', fontsize=16)
#plt.title('Central Temperature as a Function of central Density', fontsize=16) 

plt.fill_between(rho_vals,rad_line(rho_vals,1.5),rad_line(rho_vals,1.5).max(), color='lightblue')
plt.fill_between(rho_vals[rho_vals<nr_er_dege_line(2)],ideal_gas_nr_dege_line(rho_vals[rho_vals<nr_er_dege_line(2)],1.5,2), color='lightgrey')
plt.fill_between(rho_vals[rho_vals>nr_er_dege_line(2)],ideal_gas_er_dege_line(rho_vals[rho_vals>nr_er_dege_line(2)],1.5,2), color='grey', alpha=0.8)

plt.annotate('Radiation',xy=(155,400), xycoords='figure pixels', fontsize=14)
plt.annotate('Ideal Gas',xy=(170,250), xycoords='figure pixels', fontsize=14)
plt.annotate('Degenerate',xy=(490,250), xycoords='figure pixels', fontsize=14)
plt.annotate('NR',xy=(380,170), xycoords='figure pixels', fontsize=14)
plt.annotate('ER',xy=(565,170), xycoords='figure pixels', fontsize=14)
plt.xlim(-6,8)
plt.ylim(0.5,10)
plt.grid()





