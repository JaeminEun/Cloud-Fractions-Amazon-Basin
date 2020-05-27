#Jaemin Eun
#AOSC 652 Project: Cloud Fraction Change in Amazon

#Data Analysis: From "CloudFractionScript.py" we obtain the data. I created an entirely new dataset to
#make this easier. "CloudFracDataWholeGregorian.csv"

#Running Mean: In this script we will plot Running Mean along with the data itself. 

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

from scipy import stats

def load_comma_data(infile,headers):
        import pandas as pd
        data_in = pd.read_csv(infile, skiprows=headers, delim_whitespace=False, header=None).values
        return data_in

data_in = load_comma_data('CloudFracDataWholeGregorian.csv', 1)

date = data_in[:,2]
CloudFrac = data_in[:,1]

#plt.show()

plt.plot(date, CloudFrac, label = 'CloudFraction')

plt.title('Cloud Fraction in the Amazon Basin (2004-2018)')
plt.xlabel('Days')
plt.ylabel('Cloud Fraction (Unitless)')

#We use a running mean window of 365 days (1 year)
#This breaks down seasonality and highlight's the longer term trends. 
RunningMean, window = mf.running_mean(CloudFrac, 365)
plt.plot(date,RunningMean,label="365 Day Running Mean")


plt.legend(loc=0)

plt.show()
