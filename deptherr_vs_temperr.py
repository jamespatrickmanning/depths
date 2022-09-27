"""
Created on Fri Mar 21 11:50:39 2014

compares depth error with temperature error

@author: jmanning
"""
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# read files once stored in /net/data5/jmanning/modvsobs/

dft=pd.read_csv('totalcalculate_25Mar2014.csv',index_col=0)
dfd=pd.read_csv('compare_depths.out',index_col=0)
f=plt.figure()
ax1=f.add_subplot(211)
ax2=f.add_subplot(212)
for k in range(len(dft)):
   for j in range(len(dfd)):
       if dft.index[k]==dfd.index[j]:
           #plt.plot(dft['mean'][k],abs(dfd['perc_diff'][j]),'*')
           ax1.plot(dft['mean'][k],dfd['perc_diff'][j],'*')
           ax1.set_title('Absolute Error')
           #ax1.annotate(dft.index[k],(dft['mean'][k],dfd['perc_diff'][j]),fontsize=6)
           ax2.plot(dft['rms'][k],dfd['perc_diff'][j],'*')
           ax2.set_title('RMS Error')
           #ax2.annotate(dft.index[k],(dft['rms'][k],dfd['perc_diff'][j]),fontsize=6)
plt.xlabel('temperature diff (degC)')
plt.ylabel('% depth diff')
plt.show()
plt.savefig('deptherr_vs_temperr.png')
