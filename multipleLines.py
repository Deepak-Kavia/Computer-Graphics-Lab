# importing package 
from matplotlib import pyplot as plt  

# create data 
x = [10,20] 
y = [30,30] 

x1 = [10,10]
y2 = [30,50]

x2 = [10,20]
y3 = [50,50]
# plot line 
plt.plot(x,y)
plt.plot(x1,y2)
plt.plot(x2,y3)
plt.show()
