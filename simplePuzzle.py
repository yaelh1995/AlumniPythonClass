def born_again():
    print("would you rather be a boy or a girl")

    choice = input("> ")
    if choice == "boy":
        print("Okay, great! STAY AWAY FROM GIRLS THEY HAVE CUDDIES!")
        exit(0)
    elif choice == "girl":
        print("Okay, great! girl power!! Be careful, boys think girls have cuddies when you're a kid")
        exit(0)
    else:
        dead("Sorry, that is not an option.")

def black_hole():
    print("Suddenly a black hole comes out of nowhere! You are about to die, any last words?")

    choice = input("> ")
    if choice == "save me":
        print("you're saved. Told you magic is real!!")
        exit(0)
    else:
        born_again()


def im_flying():
    print("magic is real.")
    print("im order for you to fly you must say abracadabra then jump.")
    print("you can either: just jump or abracadabra and jump.")
    print("How will you fly?")

    choice = input("> ")
    if choice == "just jump":
        dead("you're an idiot. I told you what to do. Now you look like ketchup.")
    elif choice == "abracadabra and jump":
        black_hole()
    else:
        print("sigh, what??")
        im_flying()


def the_building():
    print("magic is real")
    print("im going to force you to fly even if you dont want to")
    print("would you like to die or fly?")

    choice = input("> ")

    if "fly" in choice:
        start()
    elif "die" in choice:
        dead("you better run!")
    else:
        the_building()


def dead(why):
    print(why, "lit! Hope you enjoyed.")
    exit(0)

def start():
    print("I believe I can fly")
    print("YOu should come with me")
    print("do you want to come with me? yes or no...?")

    choice = input("> ")

    if choice == "yes":
        im_flying()
    elif choice == "no":
        the_building()
    else:
        dead("what?")


start()
