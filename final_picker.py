import random, sys, pickle
from os import path
from house_names import houses

# Start Debug
house_name = "Holger"
# End Debug

# Start Define variables
exclusions_file = 'exclusions.dat'
# End Define variables

# Start Define Functions
def load_exclusions(house_name):
    # Test if exclusion file exists
    if path.exists(exclusions_file):
        # Read in the saved exclusions
        exclusions = pickle.load(open(exclusions_file, 'rb'))
        # Remove saved exclusions from the main house list
        for person in exclusions:
            if(person[0] == house_name):
                houses[house_name].remove(person[1])
    else:
        exclusions = []

    return exclusions

def write_exlusions(name, house):
    # Exclusions should be a list of tuples
    exclusions.append(tuple([house, name]))
    # write exlusions to the exclusions file
    pickle.dump(exclusions, open(exclusions_file, 'wb'))
# End Define Functions

exclusions = load_exclusions(house_name)

number_names = len(houses[house_name])
el = len(sys.argv)

if el == 2 and int(sys.argv[1]) <= number_names and int(sys.argv[1]) >= 1:
        count = int(sys.argv[1])

        for i in range(count):
            random.seed()
            choice = random.choice(houses[house_name])
            print(choice)
            houses[house_name].remove(choice)
            write_exlusions(choice, house_name)
else:
    print("You must enter a number between 1 and " + str(number_names))