import matplotlib as mpl
import matplotlib.pyplot as plt
#from mpl_toolkits.basemap import Basemap
import numpy as np
import h5py

from datetime import datetime
import datetime as dt
from datetime import date, timedelta as td
from datetime import date as ab
import time
from time import strftime, localtime
###I want to set a start date and an end date, so will update you on the date stuff
import glob 

import pandas as pd

#curDT = dt.datetime(2004,10,1,19,52)
#endDT = dt.datetime(2004,12,31,19,52)
curDT = date(2004,10,1)
endDT = date(2004,12,31)
### Data can be specified by date windows. In this we look at only 2004.
good = 0
bad = 0
i=1

while curDT < endDT:
    year = curDT.strftime("%Y")
    ### We will take advantage of glob.glob to find files with similar naming patterns
    ### HDF files have the file name and some form of date at the end
    file = glob.glob("OMI-Aura_L2G-OMCLDO2G_" + curDT.strftime("%Ym%m%d")+"*")
    #print("homes/metogra/jeun/OMI-Aura_L2-OMTO3_" + curDT.strftime("%Ym%m%d")+"*")
    
    try:
        f = h5py.File(file[0],mode='r')
        good += 1
        #at = f['HDFEOS/SWATHS/OMI Column Amount O3/Geolocation Fields/Latitude'][:,:]
        #on = f['HDFEOS/SWATHS/OMI Column Amount O3/Geolocation Fields/Longitude'][:,:]
        cfrac = f['HDFEOS/GRIDS/CloudFractionAndPressure/Data Fields/CloudFraction'][:,:]
        cfrac = np.ma.masked_where(cfrac == -1.2676506E30,cfrac)
        #print(cfrac)
        avg = np.average(cfrac)
        #This is to aggregate data into a singular mean.
        #print(curDT, avg)
        print(avg)
        #print(curDT)
        
        #plt.plot(curDT, avg)
        #plt.show()
        
    except:
        bad += 1
        ###pass
        #EndYear=curDT.strftime("%Y")
    curDT = curDT + td(days=1)
    i+=1


#The following is to read csv data after HDF data is extracted
def load_comma_data(infile,headers):
        import pandas as pd
        data_in = pd.read_csv(infile, skiprows=headers, delim_whitespace=False, header=None).values
        return data_in

#The following is to visually plot the data.
data_in = load_comma_data('2004CloudFracData.csv', 1)

date = data_in[:,0]
CloudFrac = data_in[:,1]

#nday = 75 #2012 is a leap year, hence containing 366 days
#datespace = dt.datetime(2004, 1, 1); #Need To Set datespace at the last date of the year
                                     #This is because we will substract down by this date
#date = [datespace - dt.timedelta(days=x) for x in range(0, nday)]

plt.plot(date, CloudFrac)
plt.show()
