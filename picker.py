import random, sys, pickle
from os import path
from house_names import houses

house_name = sys.argv[2]

the_house_names = list(houses.keys())

if house_name not in the_house_names:
    print("Use one of House1, House2, or House3 only")
    quit()

exclusions_file = 'exclusions.dat'

def load_exclusions(house_name):
    if path.exists(exclusions_file):
        exclusions = pickle.load(open(exclusions_file, 'rb'))
        for person in exclusions:
            if person[0]== house_name:
                houses[house_name].remove(person[1])
    else:
        exclusions = []
    return exclusions

def write_exlusions(house, name):
    exclusions.append(tuple([house, name]))
    pickle.dump(exclusions, open(exclusions_file, 'wb'))
    return

exclusions = load_exclusions(house_name)

number_names = len(houses[house_name])
el = len(sys.argv)

if el == 3 and int(sys.argv[1]) <= number_names and int(sys.argv[1]) >= 1:

        count = int(sys.argv[1])

        for i in range(count):
            random.seed()
            choice = random.choice(houses[house_name])
            print(choice)
            houses[house_name].remove(choice)
            write_exlusions(house_name, choice)

else:
    print("You must enter a number between 1 and " + str(number_names))