import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10, 15, 13, 18, 20]

plt.plot(x,y)
plt.show()


plt.plot(x,y,marker = '*', linestlye = '-', color = 'red', label = 'temperature')
plt.title("dDaily temperature trend")
plt.xlabel("Time (Hour)")
plt.ylabel("Temperature (c)")
plt.legend()
plt.grid(True)
plt.savefig("./li")