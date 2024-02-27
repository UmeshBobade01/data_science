"""Matplotlib"""
############################################################################
"""For pandas series"""
import pandas as pd
import matplotlib.pyplot as mt
s = pd.Series([45,60,38,13],name='Songs',index=['Paul','John','George','Ringo'])
s1 = pd.Series([94,67,48,33],name='Songs', index=['ram','shyam','sam','radhe'])

#plot a graph
fig = mt.figure()
s1.plot()
s.plot(color='r')
mt.legend()

#plot a bar graph
fig = mt.figure()
s1.plot(kind='bar')
s.plot(kind='bar',color='r')
mt.legend()

#plot histogram
import numpy as np
data = pd.Series(np.random.randn(500),name='random')
fig = mt.figure()
ax = fig.add_subplot(111)
data.hist()
mt.legend()
############################################################################

#plot a line graph for single line
#plot(x.coordinate,y.cordinate)
mt.plot([1,2,3,4,5],[1,2,3,4,5])


#plot a line graph for two lines
x = range(1,5)
mt.plot(x,[xi*1.5 for xi in x])
mt.plot(x,[xi*3.0 for xi in x])
mt.plot(x,[xi/3.0 for xi in x])
"""or"""
mt.plot(x,x*1.5,x,x*3.0,x,x/3.0)

x = np.arange(1,5)
mt.plot(x,x*1.5,x,x*3.0,x,x/3.0)
mt.grid(True)
#to define axis
mt.axis()
#axis([x.start,x.end,y.start,y.end])
mt.axis([0,5,-1,13]) 
#add lables to axis
mt.xlabel("x axis")
mt.ylabel("y axis")
