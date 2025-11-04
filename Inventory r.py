run = True
bag = []
print("välkommen till ditt inventory")

while run:
    print("visa, innehållet i inventory[V]")
    print("avsluta programmet [Q]")
    print("spara i inventory [S]")
    choice = input("välj:")
    if choice.lower() == "v":
        for thing in bag:
            print(thing)
    elif choice.lower() == "s":
        bag.append(input("skriv vad du vill spara"))
    elif choice.lower() == "q":
        run = False
    else:
        print("ogiltigt val, försök igen")
