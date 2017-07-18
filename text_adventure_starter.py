def start():
    print("Wrirte a name for your character")
    name = input("name: ")
    print("Once upon a time " + name +" wife sends him to the supermarket after work. " + name + " was very tired and a lazy guy. Also, he's impatient, forgetful, selfish and careless. Eventually " + name + " agrees to go to the supermarket. Now that he's at the supermarket he has to choose whether he wants to pick up vegetables or fruits first")
start()

def ChooseProduce():
    choice = input("Choose produce item fruits or vegetables: ")
    if choice == "fruits":
        print("What fruit would you like?")
        fruit=input("fruit: ")
        print("Wife calls and asks what is he buying. She gets mad because it is taking him too long and tells him to buy chicken. On his way to the meat section he passes the dairy aisle and gets distracted by the sale on ice cream. He knows that his wife likes vanilla ice cream but it is not on sale. Currently the store has only vanilla and chocolate in stock unfortunately. Now he has to pick a flavor he wants.")

    else:
        print("What vegetable would you like?")
        vegetable=input("vegetable: ")
        print("Wife calls and asks what is he buying. She gets mad because it is taking him too long and tells him to buy chicken. On his way to the meat section he passes the dairy aisle and gets distracted by the sale on ice cream. He knows that his wife likes vanilla ice cream but it is not on sale. Currently the store has only vanilla and chocolate in stock unfortunately. Now he has to pick a flavor he wants.")
ChooseProduce()

def ice():
    flavor = input("What ice cream flavor would you like to buy?")
    if flavor == "vanilla":
        print("Great Choice!")

    elif flavor=="chocolate":
            print("Oops your wife is not a fan of that flavor")
ice()

def dd():
    print("After picking up the ice cream he remembers that his wife wanted him to buy chicken so he goes to the meat section. While he is walking to the meat section he passes a man handing out free chocolate donuts which happen to be his favorite. So he grabs a donut and happens to check the time. He realizes that he was supposed to be home hours ago and has two choices. Either he picks up the chicken and runs to the cash register or hetakes only the cart to the cash register without the chicken")
    print("Choose to only take the chicken or to take the cart without the chicken?")
    choice = input("Type if you want the cart or the chicken only?")
    if choice == "chicken":
        print("He came home to his wife and got yelled at and eventually got kicked out")
    elif choice=="cart":
        print("He came home to his wife and got yelled at and eventually got kicked out")

dd()
