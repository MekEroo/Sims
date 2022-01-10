def Display_Menu():
    print("=================="
          "\n   TBTP IMS   \n"
          "==================")

    print("A - Add item\n"
          "T - Take out item\n"
          "R - Remove item\n"
          "L - List of items\n"
          "U - Update item\n"
          "S - Search item\n"
          "M - Menu\n"
          "X - Exit")

    choice = input('> ').lower()
    print()

    Selection(choice)


def Selection(choice):
    match(choice):
        case 'a':
            add()

        case 't':
            take_out()

        case 'r':
            remove()

        case 'l':
            list()

        case 'u':
            ""

        case 's':
            ""

        case 'm':
            Display_Menu()

        case 'x':
            exit()

        case _:
            Display_Menu()

def add():
    f = open('storage.txt', 'a')
    for _ in range(0, int(input("Enter number of items to add: "))):

        print()
        item_name = input("Item Name: ").lower()
        item_quantity = input("Item Quantity: ")

        f.write(item_name + '\n')
        f.write(item_quantity + '\n')

    f.close()
    print()
    Display_Menu()

def take_out(): 
    for _ in range(0, int(input("Enter number of items to take out: "))):

        try :
            f = open('storage.txt', 'r+')
            items = f.readlines()
            f.seek(0)
            take_out_item = input("Item to take out: ").lower()
            take_out_quantity = int(input("Quantity to take out: "))

            for i, item in enumerate(items) :

                if item.strip("\n") == take_out_item :
                    remaining = int(items[i + 1])

                    if remaining - take_out_quantity <= 0 :
                        items.pop(i + 1)

                    else :
                        value = remaining - take_out_quantity
                        f.write(items[i])
                        items.pop(i + 1)
                        f.write(str(value)+ "\n")

                elif item.strip("\n") != take_out_item :
                    f.write(item)

        except :
            print("Error, please follow the instructions carefully.")
                
        f.truncate()
        f.close()
        
    print()
    Display_Menu()

def remove():
    for _ in range(0, int(input("Enter number of items to remove: "))):

        try :
            f = open('storage.txt', 'r+')
            items = f.readlines()
            f.seek(0)
            remove_item = input("Item to remove: ").lower()

            for i, item in enumerate(items) :

                if item.strip("\n") == remove_item :
                    items.pop(i + 1)

                elif item.strip("\n") != remove_item :
                    f.write(item)

        except :
            print("Error, please follow the instructions carefully.")
                
        f.truncate()
        f.close()
        
    print()
    Display_Menu()

def list():
    f = open("storage.txt", 'r')
    for x in f.read():
        print(x, end='')

    f.close()
    print()
    Display_Menu()


Display_Menu()
