is_running = True

class Car():
    def __init__(self, name, company,  color, year, on_sale):
        self.name = name
        self.company = company
        self.color = color
        self.year = year
        self.on_sale = on_sale
    def __str__(self):
        return f"Name: {self.name} Company: {self.company} Color available: {self.color} Year of release: {self.year} Is on sale?: {self.on_sale}\n"
    

car1 = Car(name="Honda Civic", company="Honda", color="Cosmic Blue Metallic", year=2024, on_sale=True)
car2 = Car(name="Ford Mustang", company="Ford", color="Race Red", year="2024", on_sale=True)
car3 = Car(name="Subaru Forester", company="Subaru", color="White Pearl", year="2024", on_sale=True)
car4 = Car(name="Tesla M3", company="Tesla", color="Midnight Silver", year="2024", on_sale=True)
car5 = Car(name="Toyota Tacoma", company="Toyota", color="Ice Cap", year="2024", on_sale=True)
cars = [car1, car2, car3, car4, car5]

cat_option = input("Would you like to see the catalogue?(Y/N:)").upper()
if cat_option == "Y":
    print("\nHere is a catalogue of cars: \n")
    for car in cars:
        print(car)
        
elif cat_option != "Y":
    print("Thank you")
    is_running =  False

total_price = 0
while is_running:

    option = input("Are you willing to purchase?(Y/N):").upper()
    if option == "Y":
        print("Select the car you would like to purchase: ")
        print("1.Honda Civic")
        print("2.Ford Mustang")
        print("3.Subaru Forester")
        print("4.Tesla M3")
        print("5.Toyota Tacoma")
    elif option != "Y":
        print("Thank You!")
        is_running = False
        break
    
    choice = input("Enter your choice of purchase(1-5):")
    
    if choice == "1":
        price = 5040
        print("Congrats you purchased a Honda civic")
    
    elif choice == "2":
        price = 5030
        print("Congrats you purchased a Ford Mustang")

    elif  choice == "3":
        price = 5030
        print("Congrats you purchased a Subaru Forester")

    elif choice == "4":
        price = 5050
        print("Congrats you purchased a Tesla M3")

    elif choice == "5":
        price = 5000
        print("Congrats you purchased a Toyota Tacoma")
    
    else:
        price = 0
        print("Thank you! Visit again")
        is_running = False

    total_price += price
print(f"Total price would be: ${total_price}")






