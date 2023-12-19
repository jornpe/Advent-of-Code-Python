# https://www.geeksforgeeks.org/plot-multiple-lines-in-matplotlib/
import matplotlib.pyplot as plt

# create data 
x = [10, 20, 30, 40, 50]
y = [30, 30, 30, 30, 30]

# plot lines 
plt.plot(x, y, label="line 1")
plt.plot(y, x, label="line 2")
plt.legend()
plt.show()
