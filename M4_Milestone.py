#Build the ItemToPurchase class with the following specifications
class ItemToPurchase:
    def __init__(self, item_name = 'none', item_price = 0, item_quantity = 0):
        self.item_name
        self.item_price
        self.item_quantity
        self.item_total = (self.item_price * self.item_quantity)
#* create print_item_cost
# Example of print_item_cost() output: Bottled Water 10 @ $1 = $10
    def print_item_cost(self):
        #print(self.item_name, self.item_quantiy, @, self.item_price, =, self.item_total)
        print(self.item_name(), self.item_quantiy(), "@ $",self.item_price (), " = $", self.item_total())