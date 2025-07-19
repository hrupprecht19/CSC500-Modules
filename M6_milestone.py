#Step4 
#star with creating the shoping cart class  
class ShoppingCart:
    def __init__(self, customer_name = 'none', current_date = "January 1, 2020"):  #cart_items = 0):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items =[]
#add item to the cart
    def add_item(self, ItemToPurchase) -> None:
        self.cart_items.append(ItemToPurchase)
#item to remove from cart
    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.name == item.name:
                self.cart_items.remove(item):
                return
        print( "Item not found in cart. Nothing removed")
#modify the cart
    def modify_item(self,ItemToPurchase):
        for item in self.cart_items:
            if item.name == ItemToPurchase.name:
                if ItemToPurchase.description:
                    item.description = ItemToPurchase.description
                if ItemToPurchase.price:
                    item.price = ItemToPurchase.price
                if ItemToPurchase.quantity:
                    item.quantity =ItemToPurchase.quantity
                return
        print("Item not found in cart. Nothing modified.")
#get_num_items_in_cart
    def get_num_items_in_cart(self):
        total = 0
        for item in self.cart_items:
            total += item.quantity
        return total
#get_cost_of_cart()
    def get_cost_of_cart(self):
        total = 0 
 