class Pizza:
    def __init__(self):
        
        self.base_price = 10.00
        self.topping_price = 1.50
        self.toppings = ["pepperoni", "mushroom", "extra cheese"]

    def calculate_total(self, topping_count):
        return self.base_price + (topping_count * self.topping_price)

    def order(self):
        topping_count = 0
        while True:
            choice = input("Enter a topping (or type 'done' to finish): ").strip().lower()
            if choice == "done":
                break
            elif choice in self.toppings:
                topping_count += 1
                print("Added!")
            else:
                print("Not in menu")

        total_bill = self.calculate_total(topping_count)

        print(f"Your final total is: {total_bill:.2f}, php")



if __name__ == "__main__":
    parlor = Pizza()
    parlor.order()