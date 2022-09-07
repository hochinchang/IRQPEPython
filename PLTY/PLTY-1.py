import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

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
    fig=plt.figure()
    ax=plt.axes()
    print(type(ax))
    ax.set_title("TY name: "+TYname)
    ax.set_xlim(-1,len(rmaxwind))
    ax.xaxis.set_major_locator(MultipleLocator(8))
    ax.set_ylim(0,165)
    ax.set_ylabel("10m Max Wind Speed(kt)")
    ax.plot(tydate[-1::-1],rmaxwind[-1::-1])
    fig.savefig("ty_intensity.png")
    
# Main program
if __name__=='__main__':
    rlon,rlat,rmaxwind,tydate = ReadLatLonIntensityTYfromRAMMB("ty_2022no011.txt")
    PLTYIntensity(rmaxwind,"HINNAMNOR")




