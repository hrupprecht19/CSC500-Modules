#Build the ItemToPurchase class with the following specifications
class ItemToPurchase:
    def __init__(self, item_name = 'none', item_price = 0, item_quantity = 0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_total = (self.item_price * self.item_quantity)
# Example of print_item_cost() output: Bottled Water 10 @ $1 = $10
#https://www.geeksforgeeks.org/python/class-instance-attributes-python/
    def print_item_cost(self):
        print('{} on hand {} @ $ {:.2f} = $ {:.2f}'.format(
            self.item_name, 
            self.item_quantity, 
            self.item_price, 
            self.item_total
            ))
#a place to store the items added 
shopping_cart = [ ]
# get the input in the string, float, interger format        
# loop for more than one item
while True:
    name = input("Enter the item name (or type 'done' to finish)")
    if name == 'done':
        break
    price = float(input("Enter the price: "))
    quantity = int(input("Enter the quantity: "))
#FITIT added in a part for debuging the price and quantity
    item = ItemToPurchase(name, price, quantity)
    shopping_cart.append(item)

print("\n Shopping Cart Summary:")
for item in shopping_cart:
    item.print_item_cost()



