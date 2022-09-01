#!/usr/bin/env python
# coding: utf-8
'''

 PART I:讀CMTmon_M8xm.txt的資料
 資料內容共12列(row)代表12個月，8欄(Column)代表不同的降雨估計
 
'''
import numpy as np
rr=np.loadtxt('CMTmon_M8xm.txt',dtype=float)

'''
 PART II:畫折線圖，共畫六條線，分別是下面6欄
  corrXM(0,:)   = tofloat(str_get_field(aaa, 1, " "))
  corrXM(1,:)   = tofloat(str_get_field(aaa, 3, " "))
  corrXM(2,:)   = tofloat(str_get_field(aaa, 5, " "))
  corrXM(3,:)   = tofloat(str_get_field(aaa, 6, " "))
  corrXM(4,:)   = tofloat(str_get_field(aaa, 7, " "))
  corrXM(5,:)   = tofloat(str_get_field(aaa, 8, " "))
  
'''
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import seaborn as sns
sns.set()
mon=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
fig=plt.figure(figsize=(1200/150,1200/150),dpi=150)
ax=plt.axes()
x=np.arange(12)
ax.set_title('Taiwan Monthly Rainfall : Abservation and Estimate')
ax.set_xticks(x,mon)
ax.set_xlim(0,11)
ax.set_ylim(0,20)

ax.set_yticks(range(0,20,3))
ax.set_ylabel('mm/day')
ax.plot(x,rr[:,3],'-ok',label='Gauge Corect Radar QPE ')
#ax.plot(x,rr[:,1])
ax.plot(x,rr[:,1],'--ok',label='RadarQPE')
#ax.plot(x,rr[:,3])
#ax.plot(x,rr[:,1],color='lime',label='IRQPE_RR')
ax.plot(x,rr[:,5],'--',color='lime',label='IRQPE_MW')
ax.plot(x,rr[:,4],'-ob',fillstyle='none',label='CMORPH2_raw')
ax.plot(x,rr[:,7],'--*b',label='IMERGE_V6_Late')
ax.legend()

#fig.show()
fig.savefig('CMTmon_M8xm_v2-1.png')
