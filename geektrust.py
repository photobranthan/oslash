from sys import argv

def main():
    # Sample code to read inputs from the file
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    lines = f.readlines()
    for line in lines:
    
    Tshirt=1000
jacket=2000
cap=500
notebook=200
pen=300
price=0.00
        print("Tshirt: Php 40.0")
print("jacket: Php 30.00")
print("cap: Php 100.00")
print("notebook: Php 45.00")
print("pen: Php 20.00")

while True:
    choice=input('\nChoose an item: Tshirt, jacket, cap, notebook, pen\n')
    if choice == 'Tshirt':
        choice=input('Would you like to pick another order? y/n\n')
        if choice == 'y':
            choice=input('\nChoose an item: Tshirt, jacket, cap, notebook, pen\n')
        else:
            for cost in price:
                sum += cost
                break
                print("Total cost: Php",sum)
                print(" ")
    elif choice == 'jacket':
        choice=input('Would you like to pick another order? y/n\n')
        if choice == 'y':
            choice=input('\nChoose an item: Tshirt, jacket, cap, notebook, pen\n')
        else:
            for cost in price:
                sum += cost
                break
                print("Total cost: Php",sum)
                print(" ")
    elif choice == 'cap':
        choice=input('Would you like to pick another order? y/n\n')
        if choice == 'y':
            choice=input('\nChoose an item: Tshirt, jacket, cap, notebook, pen\n')
        else:
            for cost in price:
                sum += cost
                break
                print("Total cost: Php",sum)
                print(" ")
    elif choice == 'notebook':
        choice=input('Would you like to pick another order? y/n\n')
        if choice == 'y':
            choice=input('\nChoose an item: Tshirt, jacket, cap, notebook, pen\n')
        else:
            for cost in price:
                sum += cost
                break
                print("Total cost: Php",sum)
                print(" ")
    elif choice == 'pen':
        choice=input('Would you like to pick another order? y/n\n')
        if choice == 'y':
            choice=input('\nChoose an item: Tshirt, jacket, cap, notebook, pen\n')
        else:
            for cost in price:
                sum += cost
                break
                print("Total cost: Php",sum)
                print(" ")
    else:
        print("Error!")
    break
        print(output)
    
if __name__ == "__main__":
    main()
