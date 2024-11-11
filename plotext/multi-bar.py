import plotext as plt

pizzas = ["Sausage", "Pepperoni", "Mushrooms", "Cheese", "Chicken", "Beef"]
male_percentages = [14, 36, 11, 8, 7, 4]
female_percentages = [12, 20, 35, 15, 2, 1]

plt.multiple_bar(pizzas, [male_percentages, female_percentages], labels = ["men", "women"])
plt.title("Most Favored Pizzas in the World by Gender")
plt.show()