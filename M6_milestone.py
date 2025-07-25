#changing step1 to a setter getter method
class ItemToPurchase:   
    def __init__(self, item_name='none', item_description = 'none', item_price=0, item_quantity=0): #added description
        self.item_name = item_name
        self.item_description = item_description
        self.item_price = item_price
        self.item_quantity = item_quantity

    @property
    def item_name(self):
        return self._item_name
    
    @property
    def item_description(self):
        return self._item_description
    
    @property
    def item_price(self):
        return self._item_price
    
    @property
    def item_quantity(self):
        return self._item_quantity
   
    @property
    def item_total(self):
        return self.item_price * self.item_quantity
    
    @item_name.setter
    def item_name(self, value: str):
        if not isinstance(value, str):
            raise ValueError("Item name must be a string")
        self._item_name = value 
    
    @item_description.setter
    def item_description(self, value: str):
        if not isinstance(value, str):
            raise ValueError("Description must be a string")
        self._item_description = value
    
    @item_price.setter
    def item_price(self, value: float):
        if not isinstance(value, (int, float)):
            raise ValueError("Item price must be a number")
        if value < 0:
            raise ValueError("Item price cannot be negative")
        self._item_price = value
    
    @item_quantity.setter
    def item_quantity(self, value: int):
        if not isinstance(value, int):
            raise ValueError("Item quantity must be an integer")
        if value < 0:
            raise ValueError("Item quantity cannot be negative")
        self._item_quantity = value
    
    @item_total.setter
    def item_total(self, value: float):
        raise AttributeError("item_total is a read-only property")  

    def print_item_cost(self):
        print(f'{self.item_name} on hand {self.item_quantity} @ ${self.item_price:.2f} = ${self.item_total:.2f}')

#Step2
#function to get the total value of the inventory
def get_total_value(inventory):
    return sum(item.item_total for item in inventory)
    
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
            description = input("Enter the item description: ")
            if not description:
                description = 'none'  # Default value if no description is provided
            break
        except ValueError:
            print("Invalid entry. Please enter a valid description.")  
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
    
        
    item = ItemToPurchase(name, description, price, quantity)
    inventory.append(item)

    print("\n Inventory Summary:")
    for item in inventory:
        item.print_item_cost()

    # Print total inventory value
    print("\nTotal inventory value: ${:.2f}".format(get_total_value(inventory)))


#Step4 
#star with creating the shoping cart
class ShoppingCart:
    def __init__(self, customer_name = 'none', current_date = "January 1, 2020"):  
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items =[]
#add item to the cart
    def add_item(self, item: ItemToPurchase):
        if not isinstance(item, ItemToPurchase):
            raise ValueError("Item must be an instance of ItemToPurchase")
        # Check if item already exists in the cart
        for existing_item in self.cart_items:
            if existing_item.item_name == item.item_name:
                existing_item.item_quantity += item.item_quantity
                return
        self.cart_items.append(item)
#item to remove from cart
    def remove_item(self, item_name: str):  
        found = any(item.item_name == item_name for item in self.cart_items)
        self.cart_items = [item for item in self.cart_items if item.item_name != item_name]
        if not found:
            print("Item not found in cart. Nothing removed")
#modify the cart
    def modify_item(self, updated_item: ItemToPurchase):
        for item in self.cart_items:
            if item.item_name == updated_item.item_name:
                if updated_item.item_description:
                    item.item_description = updated_item.item_description
                if updated_item.item_price is not None:
                    item.item_price = updated_item.item_price
                if updated_item.item_quantity is not None:
                    item.item_quantity = updated_item.item_quantity
                return
        print("Item not found in cart. Nothing modified.")
#get_num_items_in_cart
    def get_num_items_in_cart(self):
        total = 0
        for item in self.cart_items:
            total += item.item_quantity
        return total
#get_cost_of_cart()
    def get_cost_of_cart(self):
        total = 0
        for item in self.cart_items:
            total += (item.item_price * item.item_quantity)
        return total
#Part 6  print_total
    def print_total(self):
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
            return
        print(f"{self.customer_name}'s Shopping Cart - { self.current_date}")
        print(f"Number of Items : {self.get_num_items_in_cart()}")

        for item in self.cart_items:
            print(f"{item.item_name} {item.item_quantity} @ ${item.item_price} = ${item.item_price * item.item_quantity}")
        print(f"Total: ${self.get_cost_of_cart()}")
#part 6 print the description
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")

#part 5
#print the menu and logic to it 
    def print_menu(self):
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

                # Find the item in the cart
                for item in self.cart_items:
                    if item.item_name == name:
                        if description:
                            item.item_description = description
                        if price:
                            try:
                                item.item_price = float(price)
                            except ValueError:
                                print("Invalid price entered. No change made.")
                        if quantity:
                            try:
                                item.item_quantity = int(quantity)
                            except ValueError:
                                print("Invalid quantity entered. No change made.")
                        break
                else:
                    print("Item not found in cart. Nothing modified.")
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
    cart = ShoppingCart()
    cart.main()