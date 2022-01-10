def Display_Menu():
    print("=================="
          "\n   TBTP IMS   \n"
          "==================")

    print("A - Add item\n"
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

def remove():
    ""

def list():
    f = open("storage.txt", 'r')
    for x in f.read():
        print(x, end='')

    f.close()
    print()
    Display_Menu()


Display_Menu()
