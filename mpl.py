import matplotlib.pyplot as plt

x = [range(17, 24)]
y = []

plt.plot(x,y)
plt.show()


plt.plot(x,y,marker = '*', linestyle = '-', color = 'red', label = 'temperature')
plt.title("Daily temperature trend")
plt.xlabel("Time (Hour)")
plt.ylabel("Temperature (c)")
plt.legend()
plt.grid(True)