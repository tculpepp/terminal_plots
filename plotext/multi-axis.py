import plotext as plt

y1 = plt.sin()
y2 = plt.sin(2, phase = -1)

plt.plot(y1, xside = "lower", yside = "left", label = "lower left")
plt.plot(y2, xside = "upper", yside = "right", label = "upper right")

plt.title("Multiple Axes Plot")
plt.show()