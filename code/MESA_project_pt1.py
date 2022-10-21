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
import os


####################
#### Question 1 ####
####################
path = os.getcwd()

data=mp.MESA()
data.loadHistory(f=path+'/workplace/runs/LOGS_15M')   # insert the appropriate path
data_df = pd.DataFrame(data.hist.data)
#data_header = data_df.head()

max_he4 = np.where(data.hist.data['center_he4'] == data.hist.data['center_he4'].max())

plt.figure()
plt.plot(data.hist.data['star_age'][:max_he4[0][0]]/1e6, data.hist.data['center_h1'][:max_he4[0][0]], label='Hydorgen', color='blue')
plt.plot(data.hist.data['star_age'][:max_he4[0][0]]/1e6, data.hist.data['center_he4'][:max_he4[0][0]], label='Helium', color='darkorange')
plt.axvline(data.hist.data['star_age'][max_he4[0][0]]/1e6, ymin=.0, ymax=1, linestyle = '--', color = 'black',
            label='X=0.01 at t= {:.2e} yr'.format(data.hist.data['star_age'][-1]))
plt.xlabel(r'Star Age (Myr)')
plt.ylabel('Core Mass Fraction')
#plt.title(' H and He Mass Fraction')
plt.legend()
plt.tight_layout()
plt.grid()


plt.figure()
plt.plot(data.hist.data['star_age'][:max_he4[0][0]]/1e6, data.hist.data['center_n14'][:max_he4[0][0]], label='Nitrogen-14', color='darkviolet')
plt.plot(data.hist.data['star_age'][:max_he4[0][0]]/1e6, data.hist.data['center_o16'][:max_he4[0][0]], label='Oxygen-16', color='red')
plt.plot(data.hist.data['star_age'][:max_he4[0][0]]/1e6, data.hist.data['center_c12'][:max_he4[0][0]], label='Carbon-12', color='limegreen')
plt.xlabel(r'Star Age (Myr)')
plt.ylabel('Core Mass Fraction')
#plt.title(' C,N and O Mass Fraction')
plt.legend()
plt.tight_layout()
plt.grid()


plt.figure()
plt.plot(data.hist.data['star_age'][max_he4[0][0]:]/1e6, data.hist.data['center_he4'][max_he4[0][0]:], label='Helium', color='darkorange')
plt.plot(data.hist.data['star_age'][max_he4[0][0]:]/1e6, data.hist.data['center_c12'][max_he4[0][0]:], label='Carbon-12', color='limegreen')
plt.plot(data.hist.data['star_age'][max_he4[0][0]:]/1e6, data.hist.data['center_o16'][max_he4[0][0]:], label='Oxygen-16', color='red')
plt.xlabel(r'Star Age (Myr)')
plt.ylabel('Core Mass Fraction')
#plt.title(' He,C and O Mass Fraction - Helium Burning Phase')
plt.legend()
plt.tight_layout()
plt.grid()




    
'''  
data.loadHistory(f='/home/adam/My_Environment/Projects/Structure_and_Evolution_of_Stars/workplace/LOGS')  # insert the appropriate path
data_df = pd.DataFrame(data.hist.data)
data_header = data_df.head()


plt.figure()
plt.plot(data.hist.data['log_Teff'], data.hist.data['log_L'], label=r'$M=7 M_{\odot}$')
plt.xlabel(r'$Log T_{eff} \; (K)$')
plt.ylabel(r'$Log L \; \frac{L}{L_{\odot}}$')
plt.title(' HR Diagram')
plt.axis([4.4,3.6,3.1,3.8])
plt.legend()
plt.tight_layout()
plt.grid()
#plt.invert_xaxis()
'''





'''
sns.set_theme()
ax = sns.lineplot(data=data_df, x='star_age', y='center_h1')
ax = sns.lineplot(data=data_df, x='star_age', y='center_he4')
ax.set(xlabel='Star Age (yr)', ylabel='Mass Fraction', label= 'auto')
#plt.ticklabel_format(style='sci', axis='x')

'''







