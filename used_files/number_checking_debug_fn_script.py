Pins_dict = {"modes 1": [10, 12, 14], "modes 2": [15, 16, 17], "dir 1": 18, "dir 2": 20, "step 1": 21, 
"step 2": 25}

def pin_numbering_checker():
    """ Run this to ask user to confirm correct pin set up """
    print(Pins_dict)
    print("Is this the right pin set up? Type 'yes' or 'no' (note, changes made through console last time will not be saved)")
    input1 = input()
    if input1 == "yes":
        print("Sounds good, continuing.")
        return
    else:
        while True:
            print("Which one do you want to edit?")
            choice_of_edit = input()
         
            if choice_of_edit == "modes 1" or "modes 2":
                print("Which pins do you want to change? (0, 1, 2?)")
                choice_of_mode_pins1 = int(input())
                print("Choose the new pin for mode {} pin in {}".format(choice_of_mode_pins1, choice_of_edit))
                Pins_dict[choice_of_edit][choice_of_mode_pins1] = input()

            else:
                print("Choose the new pin for {}".format(choice_of_mode_pins1))
                Pins_dict[choice_of_edit] = input()
            
            print(Pins_dict)
            print("Would you like to continue editing the dictionary? (y or n)") 
            continue_editing = input()
            if continue_editing == "n":
                break

pin_numbering_checker()