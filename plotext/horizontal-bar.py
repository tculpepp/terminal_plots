import plotext as plt

pizzas = ["Sausage", "Pepperoni", "Mushrooms", "Cheese", "Chicken", "Beef"]
percentages = [14, 36, 11, 8, 7, 4]

plt.bar(pizzas, percentages, orientation = "horizontal", width = 3 / 5) # or in short orientation = 'h'
plt.title("Most Favoured Pizzas in the World")
plt.show()