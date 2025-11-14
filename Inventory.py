run = True
bag = ["katt", "majs"]
print("Välkommen till påsen😎")


while run:
    print("Visa innehållet i påsen [V]🤪")
    print("Spara i påsen [S]🧐")
    print("Avsluta programmet [Q]🥲")
    print("ta bort saker från inventory[D]")
    print("Sök efter saker i påsen [F]")
    print("Rensa påsen [R]")
    print("visa antal saker i påsen [C]")
    choice = input("Välj: ")
    if choice.lower() == "v":
        if not bag:
            print("Påsen är tom")
        else:
            for thing in bag:
                print(thing)
    elif choice.lower() == "s":
        bag.append(input("Skriv vad du vill spara: "))
        
    elif choice.lower() == "q":
        run = False
    elif choice.lower() == "f":
        query = input("vad vill du söka efter?")
        if query.lower() in bag:
            print(f"hittade: {query} i påsen")
        else:
            print(f"du sökte efter {query}, men det finns inte i påsen")
    elif choice.lower() == "r":
        bag.clear()
        print("du tömde påsen")
    elif choice.lower() == "c":
        print("antal saker i påsen är:", len(bag))
    elif choice.lower() == "d":
        if not bag: 
            print("påsen är tom")
        else:
            item = input("vad vill du ta bort")
       
        if item in bag:
            bag.remove(item)
            print(f"du har tagit bort {item} från din lista")
       
    


    else:
        print("Felaktigt kommando, försök igen.")