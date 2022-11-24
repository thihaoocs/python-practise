import coffeeshop

myCoffee = coffeeshop.Concrete_Coffee()
print('Ingredients:{0}; Cost:{1}; Tax:{2}'.format(myCoffee.get_ingredients(), myCoffee.get_cost(), myCoffee.get_tax()))

myCoffee = coffeeshop.Vanilla(myCoffee)
myCoffee = coffeeshop.Sugar(myCoffee)
print('Ingredients:{0}; Cost:{1}; Tax:{2}'.format(myCoffee.get_ingredients(), myCoffee.get_cost(), myCoffee.get_tax()))