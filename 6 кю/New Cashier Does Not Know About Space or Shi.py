'''
Some new cashiers started to work at your restaurant.

They are good at taking orders, but they don't know how to capitalize words, or use a space bar!

All the orders they create look something like this:

"milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"

The kitchen staff are threatening to quit, because of how difficult it is to read the orders.

Their preference is to get the orders as a nice clean string with spaces and capitals like so:

"Burger Fries Chicken Pizza Pizza Pizza Sandwich Milkshake Milkshake Coke"

The kitchen staff expect the items to be in the same order as they appear in the menu.

The menu items are fairly simple, there is no overlap in the names of the items:
'''
def get_order(order):
        order = order.lower().replace('burger','1').replace('fries','2').replace('chicken','3').replace('pizza','4').replace('sandwich','5').replace('onionrings','6').replace('milkshake','7').replace('coke','8')
        contener = {
            1 : 'Burger',
            2 : "Fries",
            3 : "Chicken",
            4 : "Pizza",
            5 : 'Sandwich',
            6 : 'Onionrings',
            7 : 'Milkshake',
            8 : 'Coke'
        }
        new_order = ''
        # print(sorted(order))
        for i in sorted(order):
            new_order += f'{contener[int(i)]} '
        return new_order.strip()
