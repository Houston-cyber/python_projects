known_users = ["Mano", "Grace", "Jack", "Latusha", "Emily"]

while True:
    print("Hi! My name is Travis")
    name = input("What is your name?: ").strip().capitalize()

    if name in known_users:
        print("Hello {}!".format(name))
        remove = input("Would you like to be removed from the list (y/n)?: ").strip().lower()
        
        if remove == "y":
            known_users.remove(name)
        elif remove == "n":
            print("No problem, good! I want you to stay anyway!")
            
    else:
        print("We haven't met.... {}".format(name))
        add_me = input("Would you like to be added to the list (y/n)?: ").strip().lower()
        if add_me == "y":
             known_users.append(name)
        elif add_me == "n":
            print("No worries, see you around!")

