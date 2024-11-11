import plotext as plt

l = 10 ** 4
y = plt.sin(periods = 2, length = l)

plt.plot(y)

plt.xscale("log")    # for logarithmic x scale
plt.yscale("linear") # for linear y scale
plt.grid(0, 1)       # to add vertical grid lines

plt.title("Logarithmic Plot")
plt.xlabel("logarithmic scale")
plt.ylabel("linear scale")

plt.show()