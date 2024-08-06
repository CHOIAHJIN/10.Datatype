

import matplotlib.pyplot as plt

time = [17, 18, 19, 20, 21, 22, 23, 24]
humidity = [65,70,70,75,80,85,85,85]

plt.plot(x,y,marker = '*', linestlye = '-', color = 'red', label = 'temperature')
plt.title("Daily humidity")
plt.xlabel("time")
plt.ylabel("humidity")