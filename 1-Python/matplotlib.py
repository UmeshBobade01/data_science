import matplotlib.pyplot as plt
plt.plot([1,3,2,4])

plt.show()
#This is called line chart
#--------------------------------------------------------------
'''
Multiline plot
'''
import matplotlib.pyplot as plt
x = range(1,5)
plt.plot(x, [xi*1.5 for xi in x])

plt.plot(x,[xi*3.0 for xi in x])

plt.plot(x,[xi/3.0 for xi in x])

plt.show()

#################################################################
#How matplotlib automatically choose diff color
#for each line green for first line 
#blue for second line
#red for the third one(from top to bottom)
"""
Grid ,axes and labels

"""
#Adding grid
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1,5)
plt.plot(x,x*1.5, x,x*3.0, x,x/3.0)
plt.grid(True)
plt.show()
#--------------------------------------------------------------

#Adding axes
#Handling axes

import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1,5)
plt.plot(x,x*1.5, x,x*3.0, x,x/3.0)

plt.axis()   #Show the current axes limit values

plt.axis([0, 5, -1, 13])   #Set new axes limit
#[xmin,xmax,ymin,ymax]
plt.show()

#----------------------------------------------------------------

#adding labels
import matplotlib.pyplot as plt
plt.plot([1,2,3,4])

plt.xlabel('This is x axis')
plt.ylabel('This is y axis')
plt.show()

#-----------------------------------------------------------------
'''
Adding Title
'''
#Adding Titles
import matplotlib.pyplot as plt
plt.plot([1,2,3,4])

plt.title('Rad')    #Adding Title
plt.show()
#-----------------------------------------------------------------
'''
Adding legend
'''
#Adding legend
#
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1,5)
plt.plot(x,x*1.5, label='Normal')

plt.plot(x,x*3.0, label='Fast')

plt.plot(x,x/3.0, label='Slow')

plt.legend()
plt.show()
#------------------------------------------------------------------

'''
color abbrevation

color Name
b    blue
c    cyan
g    green
k    black
m    mangenata
r    red
w    white
y    yellow
'''

#control color
import matplotlib.pyplot as plt
import numpy as np
y = np.arange(1,3)
plt.plot(y,'y');
plt.plot(y+1,'m');
plt.plot(y+2,'c');
plt.show()

#----------------------------------------------------------------------
'''
Control line style
'''
import matplotlib.pyplot as plt
import numpy as np
y=np.arange(1,3)
plt.plot(y,'--',y+1,'-.',y+2,':');
plt.show()

#--------------------------------------------------------------------
'''
Style abbrevation style

- solid
-- dashed
-. dashed.dot
:  doted   
'''
#-------------------------------------------------------------------

'''
Markers
'''
import matplotlib.pyplot as plt
import numpy as np
y=np.arange(1,3,0.2)
plt.plot(y,'x', y+0.5,'o', y+1,'D', y+1.5,'^', y+2,'s')
plt.show()
#------------------------------------------------------------------

'''
IMP
Histogram chart
'''
import matplotlib.pyplot as plt
import numpy as np
y = np.random.randn(1000)
plt.hist(y);
plt.show()
#-------------------------------------------------------------------

'''
Bar graph
'''
import matplotlib.pyplot as plt
plt.bar([1,2,3],[3,2,5]);
plt.show()

#--------------------------------------------------------------------
'''
#scatter plot
'''
import matplotlib.pyplot as plt
import numpy as np
x=np.random.randn(1000)
y=np.random.randn(1000)
plt.scatter(x,y);
plt.show()

size=50*np.random.randn(1000)
colors=np.random.rand(1000)
plt.scatter(x,y,s=size,c=colors);
plt.show()

#----------------------------------------------------------------------
'''
Adding Text
'''
import numpy as np
import matplotlib.pyplot as plt
X=np.linspace(-4, 4, 1024)
Y=.25*(X+4.)*(X+1.)*(X-2.)
plt.text(-0.5,-0.25," Peacock")
plt.plot(X,Y,c="g")
plt.show()



