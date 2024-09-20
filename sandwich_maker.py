import pyinputplus as pyip

prices = {
    "wheat": 1,
    "white": 2,
    "sourdough": 3,
    "chicken": 1,
    "turkey": 2,
    "ham": 3,
    "tofu": 4,
    "cheddar": 1,
    "Swiss": 2,
    "mozzarella": 3,
    "mayo": 1,
    "mustard": 2,
    "lettuce": 3,
    "tomato": 4,
}

bread = pyip.inputMenu(["wheat", "white", "sourdough"], numbered=True)
protein = pyip.inputMenu(["chicken", "turkey", "ham", "tofu"], numbered=True)
if pyip.inputYesNo("Do you want cheese? ") == "yes":
    cheese = pyip.inputMenu(["cheddar", "Swiss", "mozzarella"], numbered=True)
else:
    cheese = ""
if pyip.inputYesNo("Do you want condiments? ") == "yes":
    condiment = pyip.inputMenu(["mayo", "mustard", "lettuce", "tomato"], numbered=True)
else:
    condiment = ""
number_of_sandwiches = pyip.inputInt("How many sandwiches do you want? ")

print()
print(
    f"That will cost {number_of_sandwiches*(prices[bread]+prices[protein]+prices.get(cheese,0)+prices.get(condiment,0))}"
)
