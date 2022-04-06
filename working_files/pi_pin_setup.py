"""Stores dictionary for pins used on pi. Functions: 1. can check the dictionary before we run code to 
avoid damage to the board with pins set up incorrectly. 2. turns the pins into outputs. 3. can change 
the number of microsteps motor takes by changing the mode pins 3. Checks for broken pins."""
import RPi.GPIO as GPIO


microstepping_dict = {"fullstep" : [0, 0, 0], "1/2": [1, 0, 0], "1/4": [0, 1, 0],
"1/8": [0, 0, 1], "1/16": [1, 1, 0], "1/32": [1, 1, 1] }  

pins_dict = {"modes 1": [10, 12, 14], "modes 2": [26, 19, 13], "dir 1": [18], "dir 2": [5], "step 1": [20], 
"step 2": [6]}


def pin_numbering_checker():
    """ Run this to ask user to confirm correct pin set up """
    print(pins_dict)
    print("Is this the right pin set up? Type 'yes' or 'no' (note, changes made through console last time will not be saved)")
    input1 = input()
    if input1 == "yes":
        print("Sounds good, continuing.")
        return
    else:
        while True:
            print("Which one do you want to edit?")
            choice_of_edit = input()
         
            if (choice_of_edit == "modes 1") or (choice_of_edit == "modes 2"):
                print("Which pins do you want to change? (0, 1, 2?)")
                choice_of_mode_pins1 = int(input())
                print("Choose the new pin for mode {} pin in {}".format(choice_of_mode_pins1, choice_of_edit))
                pins_dict[choice_of_edit][choice_of_mode_pins1] = int(input())

            else:
                print("Choose the new pin for {}".format(choice_of_edit))
                pins_dict[choice_of_edit] = int(input())
            
            print(pins_dict)
            print("Would you like to continue editing the dictionary? (y or n)") 
            continue_editing = input()
            if continue_editing == "n":
                break


def setup_pins(pins, output_or_input = "output"):
    """'pins' is a list of integer values relating to the pin number, choose pins as output or input,
     defaults to output set to low."""
    GPIO.setwarnings(False)                                                        
    GPIO.setmode(GPIO.BCM)
    for pin in pins:
        if output_or_input == "input":
            print("{} set to input.".format(pin))
            GPIO.setup(pin, GPIO.IN)
        else:
            print("{} set to output.".format(pin))
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)


def broken_pin_checker():
    # exits code if broken pins chosen.
    for i in pins_dict:
      for j in pins_dict[i]:
        if j in (27, 22, 11, 21):
            print("Broken pins chosen. Please choose other GPIO pins. Also, double check the numbering system being used (this code uses Broadcom)")
            exit()