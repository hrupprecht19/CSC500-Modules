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
        print('{} {} @ $ {} = $ {}'.format(
            self.item_name, 
            self.item_quantity, 
            self.item_price , 
            self.item_total
            ))
# get the input in the string, float, interger format        
name = input("Enter i")
price = float(input('Enter'))
quantity = int(input("enter"))

