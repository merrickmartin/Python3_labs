def main():
    name = input("what is your name: ")
    shopping = input("Add items to your shoping list seperated with a space 'Milk Eggs ect...': "). split(" ")
    grocercy_list(name,shopping)

def grocercy_list(name,*shopping):
    #print(name)
    #print(shopping)
    #print(type(shopping))
    print(f"This is {name} shopping list:")
    for items in shopping:
        for item in items:
            print(item)
    

main()