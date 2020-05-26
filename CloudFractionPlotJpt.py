#Jaemin Eun
#AOSC 652 Project: Cloud Fraction Change in Amazon

#Data Analysis: From "CloudFractionScript.py" we obtain the data. I created an entirely new dataset to
#make this easier. "CloudFracDataWhole.csv"


import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from datetime import datetime
import datetime as dt
from datetime import date, timedelta as td
from datetime import date as ab
import time
from time import strftime, localtime

import MyFunctions as mf
import scipy.stats as sps

def load_comma_data(infile,headers):
        import pandas as pd
        data_in = pd.read_csv(infile, skiprows=headers, delim_whitespace=False, header=None).values
        return data_in

data_in = load_comma_data('CloudFracDataWhole.csv', 1)

date = data_in[:,0]

x = [dt.datetime.strptime(d,'%m/%d/%Y').date() for d in date]


CloudFrac = data_in[:,1]

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval = 365))
plt.plot(x,CloudFrac)
plt.gcf().autofmt_xdate()

#plt.show()
#plt.plot(date, CloudFrac)



plt.title('Cloud Fraction in the Amazon Basin (2004-2018)')
plt.xlabel('Year')
plt.ylabel('Cloud Fraction (Unitless)')
#plt.legend(loc=0)

#plt.show()


plt.show()
