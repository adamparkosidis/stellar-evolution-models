#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 00:22:48 2021

@author: adam
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mesaPlot as mp
import os
import itertools
from scipy import constants
from labellines import labelLine, labelLines
from matplotlib.patches import Circle

####################
#### Functions #####
####################

def sigma_cgs(x):
    return (x*(2.6310*10**(-27)))/(1.437*10**(-9))**2 

def L_func(r,T,sigma):
    return (4*np.pi*sigma*(r**2)*(T**4))

def plot_end_MS(y,x,c):
    min_h = np.where(x['center_h1'] == x['center_h1'].min()) # ['center_he4'][-1] to until the end of the helium burning phase
    min_h = min_h[0][0]
    x=x[0:min_h]
    if y==2:
        ax.plot(x['log_Teff'], x['log_L'], label=dataframes_names[y],linestyle='--', color=c) 
    else:
        ax.plot(x['log_Teff'], x['log_L'], label=dataframes_names[y],linestyle='-', color=c)
    if y == 5:
        plt.plot(x['log_Teff'].iloc[0], x['log_L'].iloc[0], 'o', markersize=3, color='black', label="ZAMS")
    else:
        plt.plot(x['log_Teff'].iloc[0], x['log_L'].iloc[0], 'o', markersize=3, color='black')
    

    

###################
#### Question 2 ###
###################

sigma = constants.value(u'Stefan-Boltzmann constant') # in W/m^2/K^4
sigma=sigma_cgs(sigma)

path = os.getcwd()
data=mp.MESA()
directory = path+'/workplace/runs'    # insert the appropriate path
data_df = pd.DataFrame(data.hist.data)

radii = np.logspace(0,2,10)
T = np.logspace(3.7,4.5,10)

data.loadHistory(directory+'/LOGS_1M')
data_df_1M = pd.DataFrame(np.array([data.hist.center_h1, data.hist.center_he4 ,data.hist.log_Teff, data.hist.log_L, data.hist.log_Lnuc]).T, columns=['center_h1',
                           'center_he4','log_Teff','log_L','log_Lnuc'])
data_df_1M = data_df_1M[data_df_1M['log_Lnuc']>0.99*data_df_1M['log_L']]
data_df_1M.name = r'M=3 $M_{\odot}$'

data.loadHistory(directory+'/LOGS_3M')
data_df_3M = pd.DataFrame(np.array([data.hist.center_h1, data.hist.center_he4 ,data.hist.log_Teff, data.hist.log_L, data.hist.log_Lnuc]).T, columns=['center_h1',
                           'center_he4','log_Teff','log_L','log_Lnuc'])
data_df_3M = data_df_3M[data_df_3M['log_Lnuc']>0.99*data_df_3M['log_L']]
data_df_3M.name = r'M=3 $M_{\odot}$'

data.loadHistory(directory+'/LOGS_5M')
data_df_5M = pd.DataFrame(np.array([data.hist.center_h1, data.hist.center_he4, data.hist.log_Teff, data.hist.log_L, data.hist.log_Lnuc]).T, columns=['center_h1',
                           'center_he4','log_Teff','log_L','log_Lnuc'])
data_df_5M = data_df_5M[data_df_5M['log_Lnuc']>0.99*data_df_5M['log_L']]
data_df_5M.name = r'M=5 $M_{\odot}$'

data.loadHistory(directory+'/LOGS_7M')
data_df_7M = pd.DataFrame(np.array([data.hist.center_h1, data.hist.center_he4, data.hist.log_Teff, data.hist.log_L, data.hist.log_Lnuc]).T, columns=['center_h1',
                           'center_he4','log_Teff','log_L','log_Lnuc'])
data_df_7M = data_df_7M[data_df_7M['log_Lnuc']>0.99*data_df_7M['log_L']]
data_df_7M.name = r'M=7 $M_{\odot}$'


data.loadHistory(directory+'/LOGS_9M')
data_df_9M = pd.DataFrame(np.array([data.hist.center_h1, data.hist.center_he4, data.hist.log_Teff, data.hist.log_L]).T, columns=['center_h1',
                           'center_he4','log_Teff','log_L'])
data_df_9M.name = r'M=9 $M_{\odot}$'

data.loadHistory(directory+'/LOGS_12M')
data_df_12M = pd.DataFrame(np.array([data.hist.center_h1, data.hist.center_he4, data.hist.log_Teff, data.hist.log_L, data.hist.log_Lnuc]).T, columns=['center_h1',
                           'center_he4','log_Teff','log_L','log_Lnuc'])
data_df_12M = data_df_12M[data_df_12M['log_Lnuc']>0.99*data_df_12M['log_L']]
data_df_12M.name = r'M=12 $M_{\odot}$'

data.loadHistory(directory+'/LOGS_7M_lowZ')
data_df_7M_lowZ = pd.DataFrame(np.array([data.hist.center_h1, data.hist.center_he4, data.hist.log_Teff, data.hist.log_L, data.hist.log_Lnuc, data.hist.pp, data.hist.cno]).T, columns=['center_h1',
                           'center_he4','log_Teff','log_L','log_Lnuc', 'pp', 'cno'])
data_df_7M_lowZ.name = r'M=5 $M_{\odot}$-Z=2d-4 Z_{\odot}'

#data_df_7M_lowZ = data_df_7M_lowZ[data_df_7M_lowZ['center_h1']<round(data_df_7M_lowZ['center_h1'].max(),3)] #exclude the pre-main sequence
#data_df_7M_lowZ = data_df_7M_lowZ[data_df_7M_lowZ['pp']>0] #exclude the pre-main sequence
data_df_7M_lowZ = data_df_7M_lowZ[data_df_7M_lowZ['log_Lnuc']>0.99*data_df_7M_lowZ['log_L']] #exclude the pre-main sequence

dataframes = [data_df_12M, data_df_7M, data_df_7M_lowZ, data_df_5M, data_df_3M, data_df_1M] # for the low Z star Z=0.001*Z_{\odot}
dataframes_names = [r'M=12 $M_{\odot}$', r'M=7 $M_{\odot}$', r'M=7 $M_{\odot} \; & \; Z=10^{-2} Z_{\odot}$', r'M=5 $M_{\odot}$', r'M=3 $M_{\odot}$', r'M=1 $M_{\odot}$']
colors=['darkviolet','dodgerblue','dodgerblue','green','gold','tomato']
x_vals = np.linspace(4.2,4.5,10)
fig, ax = plt.subplots(figsize=(10,10))
for i in radii:
    ax.plot(np.log10(T), np.log10(L_func(i,T,sigma)), color='lightgrey', linewidth=1 , linestyle='--', label='{:.0f}'.format(i)+r'$R_{\odot}$')
labelLines(plt.gca().get_lines(), xvals=x_vals ,zorder=2.5)

for i,value in enumerate(dataframes):
    plot_end_MS(i,value,colors[i])
    

plt.xlabel(r'$Log T_{eff} \; (K)$', fontsize='16')
plt.ylabel(r'$Log L \; \frac{L}{L_{\odot}}$', fontsize='16')
#plt.title(' HR Diagram')  
plt.xticks(fontsize=15) 
plt.yticks(fontsize=15) 
plt.gca().invert_xaxis()
plt.tight_layout()
plt.grid()
plt.xlim(4.5,3.7)
plt.ylim(-0.5,5)
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[10:], labels[10:],loc='center left', bbox_to_anchor=(0.0005, 0.175), prop={'size':'17'})



############ 5M

radii = np.logspace(0,2,10)
T = np.logspace(3.6,4.3,10)

x_vals = np.linspace(4.0,4.1,10)
fig, ax = plt.subplots(figsize=(10,8))
for i in radii:
    ax.plot(np.log10(T), np.log10(L_func(i,T,sigma)), color='lightgrey', linewidth=1 , linestyle='--', label='{:.0f}'.format(i)+r'$R_{\odot}$')
labelLines(plt.gca().get_lines(), xvals=x_vals ,zorder=2.5)

data.loadHistory(directory+'/LOGS_5M_He')
data_df_5M_Asy = pd.DataFrame(np.array([data.hist.center_h1, data.hist.center_he4 ,data.hist.log_Teff, data.hist.log_L,
                                     data.hist.log_cntr_Rho, data.hist.log_cntr_T, data.hist.center_mu,data.hist.log_Lnuc,
                                     data.hist.pp, data.hist.cno, data.hist.tri_alfa]).T,columns=['center_h1','center_he4',
                                     'log_Teff','log_L','log_cntr_Rho','log_cntr_T', 'center_mu','log_Lnuc', 'pp', 'cno','tri_alfa'])
data_df_5M_Asy.name = r'M=5 $M_{\odot}$'

ax.plot(data_df_5M_Asy['log_Teff'], data_df_5M_Asy['log_L'], color='orange') #label=r'M=5 $M_{\odot}$', )




plt.annotate("A",xy=(data_df_5M_Asy['log_Teff'][0],data_df_5M_Asy['log_L'][0]), xycoords='data', horizontalalignment='right',fontsize=16)
ax.plot(data_df_5M_Asy[data_df_5M_Asy['center_h1']>1e-4]['log_Teff'].iloc[0:], data_df_5M_Asy[data_df_5M_Asy['center_h1']>1e-4]['log_L'].iloc[0:], color='forestgreen')
plt.annotate('B,C',xy=(data_df_5M_Asy[data_df_5M_Asy['center_h1']<1e-4]['log_Teff'].iloc[0],data_df_5M_Asy[data_df_5M_Asy['center_h1']<1e-4]['log_L'].iloc[0]), xycoords='data',verticalalignment='bottom', fontsize=16)
plt.annotate('D',xy=(data_df_5M_Asy['log_Teff'][data_df_5M_Asy[data_df_5M_Asy['log_L']==data_df_5M_Asy['log_L'].min()].index[0]], data_df_5M_Asy['log_L'].min()), xycoords='data', verticalalignment='top', fontsize=16)
ax.plot(data_df_5M_Asy['log_Teff'][data_df_5M_Asy[data_df_5M_Asy['log_L']==data_df_5M_Asy['log_L'].min()].index[0]:], data_df_5M_Asy['log_L'][data_df_5M_Asy[data_df_5M_Asy['log_L']==data_df_5M_Asy['log_L'].min()].index[0]:], color='red')
plt.annotate('E',xy=(data_df_5M_Asy[data_df_5M_Asy['tri_alfa']>0]['log_Teff'].iloc[0],data_df_5M_Asy[data_df_5M_Asy['tri_alfa']>0]['log_L'].iloc[0]), xycoords='data',horizontalalignment='right',fontsize=16)

#ax.plot(data_df_5M_Asy[data_df_5M_Asy['tri_alfa']>0]['log_Teff'], data_df_5M_Asy[data_df_5M_Asy['tri_alfa']>0]['log_L'],color='blue')
ax.plot(data_df_5M_Asy['log_Teff'][193:], data_df_5M_Asy['log_L'][193:],color='blue')

plt.annotate('F',xy=(data_df_5M_Asy['log_Teff'].iloc[215],data_df_5M_Asy['log_L'].iloc[215]), xycoords='data',horizontalalignment='right',fontsize=16)
plt.annotate('G,H',xy=(data_df_5M_Asy['log_Teff'].iloc[-1],data_df_5M_Asy['log_L'].iloc[-1]), xycoords='data', horizontalalignment='right', verticalalignment='bottom',fontsize=16)

plt.xlabel(r'$Log T_{eff} \; (K)$', fontsize=16)
plt.ylabel(r'$Log L \; \frac{L}{L_{\odot}}$', fontsize=16)
#plt.title(' HR Diagram')   
plt.xticks(fontsize=15) 
plt.yticks(fontsize=15)
plt.gca().invert_xaxis()
plt.tight_layout()
plt.grid()
plt.xlim(4.3,3.6)
plt.ylim(1.5,5)
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[10:],labels[10:], loc='center left', prop={'size':'17'})#, bbox_to_anchor=(0.8, 0.95))






'''

##################### 9M

radii = np.logspace(0,2.5,8)
T = np.logspace(3.5,4.5,8)

x_vals = np.linspace(4.0,4.15,10)
fig, ax = plt.subplots(figsize=(10,8))
for i in radii:
    ax.plot(np.log10(T), np.log10(L_func(i,T,sigma)), color='lightgrey', linewidth=1 , linestyle='--', label='{:.0f}'.format(i)+r'$R_{\odot}$')
labelLines(plt.gca().get_lines(), xvals=x_vals ,zorder=2.5)

data.loadHistory(directory+'/LOGS_9M_He')
data_df_9M_Asy = pd.DataFrame(np.array([data.hist.center_h1, data.hist.center_he4 ,data.hist.log_Teff, data.hist.log_L,
                                     data.hist.log_cntr_Rho, data.hist.log_cntr_T, data.hist.center_mu,data.hist.log_Lnuc,
                                     data.hist.pp, data.hist.cno, data.hist.tri_alfa]).T,columns=['center_h1','center_he4',
                                     'log_Teff','log_L','log_cntr_Rho','log_cntr_T', 'center_mu','log_Lnuc', 'pp', 'cno','tri_alfa'])
data_df_9M_Asy.name = r'M=5 $M_{\odot}$'

ax.plot(data_df_9M_Asy['log_Teff'], data_df_9M_Asy['log_L'], label=r'M=9 $M_{\odot}$')

plt.annotate("A",xy=(data_df_9M_Asy['log_Teff'][0],data_df_9M_Asy['log_L'][0]), xycoords='data', horizontalalignment='right',fontsize=16)
plt.annotate('B,C',xy=(data_df_9M_Asy[data_df_9M_Asy['center_h1']<1e-4]['log_Teff'].iloc[0],data_df_9M_Asy[data_df_9M_Asy['center_h1']<1e-4]['log_L'].iloc[0]), xycoords='data',verticalalignment='bottom', fontsize=16)
plt.annotate('D',xy=(data_df_9M_Asy['log_Teff'][data_df_9M_Asy[data_df_9M_Asy['log_L']==data_df_9M_Asy['log_L'].min()].index[0]], data_df_9M_Asy['log_L'].min()), xycoords='data', verticalalignment='top', fontsize=16)
plt.annotate('E',xy=(data_df_9M_Asy[data_df_9M_Asy['tri_alfa']>0.3]['log_Teff'].iloc[0],data_df_9M_Asy[data_df_9M_Asy['tri_alfa']>0.3]['log_L'].iloc[0]), xycoords='data',horizontalalignment='right', verticalalignment='top',fontsize=16)
#plt.annotate('F',xy=(490,250), xycoords='data', fontsize=14)
plt.annotate('G,H',xy=(data_df_9M_Asy['log_Teff'].iloc[-1],data_df_9M_Asy['log_L'].iloc[-1]), xycoords='data', horizontalalignment='right', verticalalignment='top',fontsize=14)

plt.xlabel(r'$Log T_{eff} \; (K)$')
plt.ylabel(r'$Log L \; \frac{L}{L_{\odot}}$')
plt.title(' HR Diagram')   
plt.gca().invert_xaxis()
plt.tight_layout()
plt.grid()
plt.xlim(4.5,3.5)
plt.ylim(1,6.5)
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[8:],labels[8:], loc='center left', bbox_to_anchor=(0.8, 0.95))
'''