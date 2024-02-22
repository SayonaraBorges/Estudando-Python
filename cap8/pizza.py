def make_pizza(*toppings):
    """Exibe a lista de ingredientes pedidos."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def maker_pizza(size, *toppingss):
    """Apresenta a pizza que estamos prestes a preparar."""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings: ")
    for topping in toppingss:
        print('- ' + topping)

maker_pizza(16, 'clabreza')
maker_pizza(12, 'cogumelos', 'azeitonas', 'molho pomodoro')
