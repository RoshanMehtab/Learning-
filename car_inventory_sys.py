class Car:
    def __init__(self, make, model, year, price):
        self.__make = make
        self.__model = model
        self.__year = int(year)
        self.__price = float(price)
        
    def display_info(self):
        return f"Make: {self.__make}, Model: {self.__model}, Year: {self.__year}, Price: ${self.__price:.2f}"
    
    def update_info(self, make_new=None, model_new=None, year_new=None, price_new=None):
        if make_new:
            self.__make = make_new
        if model_new:
            self.__model = model_new
        if year_new:
            self.__year = int(year_new)
        if price_new:
            self.__price = float(price_new)

class Inventory:
    def __init__(self):
        self.inventory = []
        
    def add_car(self, car):
        self.inventory.append(car)
    
    def remove_car(self, index):
        if 0 <= index < len(self.inventory):
            self.inventory.pop(index)
        else:
            print("Invalid index")
    
    def view_inventory(self):
        for i, car in enumerate(self.inventory):
            print(f"{i}. {car.display_info()}")

def main():
    inventory = Inventory()
    while True:
        print("\n1. Add a new car")
        print("2. Show inventory")
        print("3. Update info")
        print("4. Remove car")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            make = input("Enter make: ")
            model = input("Enter model: ")
            year = input("Enter year: ")
            price = input("Enter price: ")
            car = Car(make, model, year, price)
            inventory.add_car(car)
            
        elif choice == 2:
            inventory.view_inventory()
            
        elif choice == 3:
            index = int(input("Enter the index of the car to update: "))
            if 0 <= index < len(inventory.inventory):
                make_new = input("Enter new make (or leave empty): ")
                model_new = input("Enter new model (or leave empty): ")
                year_new = input("Enter new year (or leave empty): ")
                price_new = input("Enter new price (or leave empty): ")
                inventory.inventory[index].update_info(make_new, model_new, year_new, price_new)
            else:
                print("Invalid index")
            
        elif choice == 4:
            index = int(input("Enter the index of the car to remove: "))
            inventory.remove_car(index)
            
        elif choice == 5:
            break
        
        else:
            print("Invalid choice")
