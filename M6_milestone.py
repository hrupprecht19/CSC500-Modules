#changing step1 to a setter getter method
class ItemToPurchase:   
    def __init__(self, item_name='none', description = 'none', item_price=0, item_quantity=0): #added description
        self.item_name = item_name
        self.description = description
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_total = self.item_price * self.item_quantity

    @property
    def item_name(self):
        return self._item_name
    
    @property
    def description(self):
        return self._description
    
    @property
    def item_price(self):
        return self._item_price
    
    @property
    def item_quantity(self):
        return self._item_quantity
    
    @item_name.setter
    def item_name(self, value):
        if not isinstance(value, str):
            raise ValueError("Item name must be a string")
        self._item_name = value 
    
    @description.setter
    def description(self, value):
        if not isinstance(value, str):
            raise ValueError("Description must be a string")
        self._description = value
    
    
    

    @property

    def print_item_cost(self):
        print('{} on hand {} @ $ {:.2f} = $ {:.2f}'.format(
            self.item_name, 
            self.item_quantity, 
            self.item_price, 
            self.item_total
        ))

    @property
    def item_total(self):
        return self.item_price * self.item_quantity
    @item_total.setter
    def item_total(self, value):
        raise AttributeError("item_total is a read-only property")  
#Step2
#function to get the total value of the inventory
    def get_total_value(inventory):
        total = 0
        for item in inventory:
            total += item.item_total
        return total    
#Step3
#place to store the items added
inventory = []
# get the input in the string, float, integer format        
# loop for more than one item
while True:
    name = input("Enter the item name (or type 'done' to finish): ")
    if name.lower() == 'done':
        break
    #creating a nested loop to have valued inputs
    while True:
        try:
            price = float(input("Enter the price: "))
            break
        except ValueError:
            print("Invalid entry. Please enter a number for price.") 
    #creating another nested loop to have a valued input
    while True:
        try:
            quantity = int(input("Enter the quantity: "))
            break
        except ValueError:
            print("Invalid entry. Please enter a whole number for quantity.")
    
    item = ItemToPurchase(name, price, quantity)
    inventory.append(item)
#Step4 
#star with creating the shoping cart
class ShoppingCart:
    def __init__(self, customer_name = 'none', current_date = "January 1, 2020"):  
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items =[]
#add item to the cart
    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)
#item to remove from cart
    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.name == item_name:
                self.cart_items.remove(item)
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
        for item in self.cart_items:
            total += (item.price * item.quantity)
        return total
#do print_total
    def print_total(self):
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
            return
        print(f"{self.customer_name}'s Shopping Cart - { self.current_date}")
        print(f"Number of Items : {self.get_num_items_in_cart()}")

        for item in self.cart_items:
            print(f"{item.name} {item.quantity} @ ${item.price} = ${item.price * item.quantity}")
        print(f"Total: ${self.get_cost_of_cart()}")
#print the description
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.name}: {item.description}")

#part 5
#print the menu and logic to it 
    def print_menu(cart):
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        print("Choose an option:",end="")
 
    def main(self):
        while True:
            self.print_menu()
            choice = input().strip().lower()
            if choice == 'a':
                name = input("Enter the item name: ")
                description = input("Enter the item description: ")
                price = float(input("Enter the item price: "))
                quantity = int(input("Enter the item quantity: "))
                item = ItemToPurchase(name, description, price, quantity)
                self.add_item(item)
            elif choice == 'r':
                name = input("Enter the item name to remove: ")
                self.remove_item(name)
            elif choice == 'c':
                name = input("Enter the item name to modify: ")
                description = input("Enter new description (or leave blank): ")
                price = input("Enter new price (or leave blank): ")
                quantity = input("Enter new quantity (or leave blank): ")
                item = ItemToPurchase(name, description if description else None,
                                      float(price) if price else None,
                                      int(quantity) if quantity else None)
                self.modify_item(item)
            elif choice == 'i':
                self.print_descriptions()
            elif choice == 'o':
                self.print_total()
            elif choice == 'q':
                print("Thank you for using the shopping cart!")
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()