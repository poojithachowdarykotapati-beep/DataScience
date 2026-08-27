import matplotlib.pyplot as plt
X=[5,9,2,4]
Y=[30,45,20,50]
plt.plot(X,Y)
plt.title("line plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.savefig("line_plot.png")
plt.show()