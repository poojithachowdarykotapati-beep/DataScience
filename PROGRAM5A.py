import matplotlib.pyplot as plt
X=[1,2,3,4]
Y=[10,20,25,30]
plt.plot(X,Y)
plt.title("line plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.savefig("line_plot.png")
plt.show()