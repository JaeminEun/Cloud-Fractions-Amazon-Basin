#Jaemin Eun
#AOSC 652 Project: Cloud Fraction Change in Amazon

#Data Analysis: From "CloudFractionScript.py" we obtain the data. I created an entirely new dataset to
#make this easier. "CloudFracDataWholeGregorian.csv"

#Regression: Pretty similar to the Running Mean plot, but creating a regression (I want to see what
#happens in the future).

import numpy as np
import matplotlib.pyplot as plt
import MyFunctions as mf
import scipy.stats as sps
import LHD

data_in = LHD.load_space_data('CloudFracDataWholeGregorian.txt', 1)

#date = data_in[:,2]
#CloudFrac = data_in[:,1]

#np.polyfit really wants np floats. 
#I was having major dificulty because I did not have them as np floats
date = np.float_(data_in[:,2])
CloudFrac = np.float_(data_in[:,1])

plt.plot(date, CloudFrac,'o',label='Scatter Plot')

plt.title('Cloud Fraction in the Amazon Basin (2004-2018)')
plt.xlabel('Days')
plt.ylabel('Cloud Fraction (Unitless)')


plt.legend(loc=0)

coef_lin = np.polyfit(date, CloudFrac,1)
print(coef_lin)
#This will give us the linear fit coefficient
lfit=np.poly1d(coef_lin)
xfit = np.linspace(date[0], date[-1])
yfit_1 = lfit(xfit)

xfit_p = np.linspace(date[0],date[-1]+4989,170) #4989 to signify double the time frame
yfit_1p = lfit(xfit_p)
plt.plot(xfit_p, yfit_1p, color='red', label='Linear Fit Projection: y={0:1.9f}x + {1:1.3f}'.format(coef_lin[0], coef_lin[1]))
plt.legend(loc=0)


plt.show()


