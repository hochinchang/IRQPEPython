def ReadLatLonIntensityTYfromRAMMB(file):
    # open/read file content
    with open(file)as fr: 
         # Skip first line : lines[0:]
         lines=fr.readlines()[1:]
    # split out variables
    rlon=[]
    rlat=[]
    rmaxwind=[]
    tydate=[]
    for line in lines:  
        s = line.split('\t')
        rlat.append(float(s[1]))
        rlon.append(float(s[2]))
        rmaxwind.append(float(s[3]))
        tydate.append(s[0])
    return rlat,rlon,rmaxwind,tydate

def PLTYIntensity(rmaxwind,TYname):
    print(type(rmaxwind))
    for i in rmaxwind:
        print(i)
    lenx=len(rmaxwind)
    x= np.arange(lenx)
    fig=plt.figure()
    # print(x,rmaxwind[:])
    ax=plt.axes()
    ax.set_title("TY name: "+TYname)
    ax.set_xticks(x,tydate)
    ax.set_xlim(-1,lenx)
    ax.set_ylim(0,165)
    ax.set_ylabel("10m Max Wind Speed(kt)")
    ax.plot(x,rmaxwind)
    fig.savefig("ty_intensity.png")
    
# Main program
TYdata = ReadLatLonIntensityTYfromRAMMB("ty_2022no011.txt")
print(type(TYdata))
rlon,rlat,rmaxwind,tydate=TYdata

import matplotlib.pyplot as plt
import numpy as np
PLTYIntensity(rmaxwind,"HINNAMNOR")




