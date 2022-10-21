#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 13:40:27 2021

@author: adam
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mesaPlot as mp
import os
import mesaPlot as mp

m=mp.MESA()
p=mp.plot()
m.data=mp.MESA()
m.loadHistory(f=path+'/workplace/runs/LOGS_5M_He') # insert the appropriate path
data_df = pd.DataFrame(m.hist.data)
p.plotKip3(m,show_mass_loc=True, mix_hattch=True)