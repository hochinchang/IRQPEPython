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
fig=plt.figure()
ax=plt.axes()
x=np.arange(12)
print(x,rr[:,0])
ax.plot(x,rr[:,0])
ax.plot(x,rr[:,2])
ax.plot(x,rr[:,4])
ax.plot(x,rr[:,5])
ax.plot(x,rr[:,6])
ax.plot(x,rr[:,7])
fig.show()