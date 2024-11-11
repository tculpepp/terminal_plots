import plotext as plt

pizzas = ["Sausage", "Pepperoni", "Mushrooms", "Cheese", "Chicken", "Beef"]
percentages = [14, 36, 11, 8, 7, 4]

plt.simple_bar(pizzas, percentages, width = 100, title = 'Most Favored Pizzas in the World')
plt.show()