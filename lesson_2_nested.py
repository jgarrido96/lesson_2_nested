
# 1. Nested Decisions: The Adventure Game

# Task 1: Code Correction
'''
place = input("Choose a place! [forest/cave] ")

if place == "forest":
    action = input("What's the move?? [cross] river, or [climb] tree? ")
    if action == "climb":
        print("You found a bird's nest!")
    elif action == "cross":
        print("You found a boat!")

# Task 2: Setting the Scene

if place == "cave":
    cave_fun = input("You found a hidden chest!""\n""I bet there's better loot inside! [light] torch or [proceed] through the dark? ")
    if cave_fun == "light":
        print("Good thing I lit this torch, there's a bunch of spider-webs ahead!! [woof] ")
    elif cave_fun == "proceed":
        print("Oh no! You walk into spider-webs in the dark! [wack]")

# Task 3: Default Path

else:
    pass

    '''

print("\n \n")
# 2. Quick Decisions: The Event Planner

# Task 1: Code Correction

attendees = int(input("Enter number of attendees: "))
vegetarian_input = input("Would you like vegetarian options? [y/n] ")
print('\n')
if attendees > 100:
    venue = "Large Hall"
    equip = "Small PA needed"
    if attendees > 200:
        equip = "PA needed"
        if attendees > 300:
            equip = "PA and projector needed"
elif attendees < 100:
    venue = "Conference Room"
    equip = "No additional equipment required"
print(venue + ", " + equip)

if vegetarian_input == "y":
    print('We recommend "Veggie Delight Caterers" for a larger vegetarian selection.')
elif vegetarian_input == "n":
    print('We recommend "Gourmet Meals Caterers" for an affordable, diverse menu.')
else:
    print("That's not a valid input!")


#lesson_2_nested 
