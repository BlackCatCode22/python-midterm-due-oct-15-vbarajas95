from _datetime import date
from Lions import Lions
from Animal import Animal
from Hyena import Hyena
from Bear import Bear
from Tiger import Tiger
# Programmer name: Vanessa Barajas

# Program name: Python Midterm

# Date: 8-15-2023

# Course: CIT 95


# create list of the species
list_of_hyenas = []
list_of_lions = []
list_of_tigers = []
list_of_bears = []

# To calculate birthday
current_date = date.today()
current_year = current_date.year


def calc_birth_date(the_season, the_years):
    year_of_birthday = int(current_year) - int(the_years)

    the_birth_day = ""

    if "spring" in the_season:
        the_birth_day = str(year_of_birthday) + "-03-21"
    elif "summer" in the_season:
        the_birth_day = str(year_of_birthday) + "-06-21"
    elif "fall" in the_season:
        the_birth_day = str(year_of_birthday) + "-09-21"
    elif "winter" in the_season:
        the_birth_day = str(year_of_birthday) + "-12-21"

    return the_birth_day


def process_one_line(one_line):
    # Create variables to help parse arrivingAnimals.txt
    a_species = ""
    a_gender = ""
    age_in_years = ""
    season = ""
    color = ""
    weight = ""
    origin_01 = ""
    origin_02 = ""

    print(one_line)
    group_of_words = one_line.strip().split(",")
    print(group_of_words)
    single_words = group_of_words[0].strip().split(" ")
    age_in_years = single_words[0]
    a_gender = single_words[3]
    a_species = single_words[4]
    single_words = group_of_words[1].strip().split(" ")
    season = single_words[2]
    color = group_of_words[2].strip();
    weight = group_of_words[2].strip();
    origin_01 = group_of_words[4].strip();
    origin_02 = group_of_words[5].strip();

    from_zoo = origin_01 + ", " + origin_02

    birth_day = calc_birth_date(season, age_in_years)

    if "hyena" in a_species:
        # Create hyena object
        my_hyena = Hyena("aName", "anID", birth_day, color, a_gender, weight, from_zoo, current_date)
        # fill in name and ID
        my_hyena.name = Hyena.get_hyena_name(my_hyena)
        my_hyena.animal_id = "Hy" + str(Hyena.numOfHyenas)
        # add to hyena list
        list_of_hyenas.append(my_hyena)

    if "lion" in a_species:
        # Create lion object
        my_lion = Lions("aName", "anID", birth_day, color, a_gender, weight, from_zoo, current_date)
        # fill in name and ID
        my_lion.name = Lions.get_lion_name(my_lion)
        my_lion.animal_id = "Li" + str(Lions.numOfLions)
        # add to lions list
        list_of_lions.append(my_lion)

    if "tiger" in a_species:
        # Create tiger object
        my_tiger = Tiger("aName", "anID", birth_day, color, a_gender, weight, from_zoo, current_date)
        # fill in name and ID
        my_tiger.name = Tiger.get_tiger_name(my_tiger)
        my_tiger.animal_id = "Ti" + str(Tiger.numOfTigers)
        # add to tiger list
        list_of_tigers.append(my_tiger)

    if "bear" in a_species:
        # Create bear object
        my_bear = Bear("aName", "anID", birth_day, color, a_gender, weight, from_zoo, current_date)
        # fill in name and ID
        my_bear.name = Bear.get_bear_name(my_bear)
        my_bear.animal_id = "Be" + str(Bear.numOfBears)
        # add to bear list
        list_of_bears.append(my_bear)


# Open arrivingAnimals.txt and read one line at a time
# Open file in read mode
file_path = r'/Users/Vanessa/myGitDir/python-midterm-due-oct-15-vbarajas95/arrivingAnimals.txt'
with open(file_path, "r") as file:
    # Iterate through file line by line
    for line in file:
        process_one_line(line)

# Access the static variable numOfHyenas
print(f'Number of Hyenas Created:{Hyena.numOfHyenas}')

# Access the static variable numOfAnimals
print(f"\n\nNumber of Animals Created: {Animal.numOfAnimals}")

# Output the static variable numOfHyenas
print(f"\n\nNumber of Hyenas Created: {Hyena.numOfHyenas}")

# Access the static variable numOfLions
print(f'Number of Lions Created:{Lions.numOfLions}')

# Access the static variable numOfAnimals
print(f"\n\nNumber of Animals Created: {Animal.numOfAnimals}")

# Output the static variable numOfLions
print(f"\n\nNumber of Lions Created: {Lions.numOfLions}")

# Access the static variable numOfBears
print(f'Number of Bears Created:{Bear.numOfBears}')

# Access the static variable numOfAnimals
print(f"\n\nNumber of Animals Created: {Animal.numOfAnimals}")

# Output the static variable numOfBears
print(f"\n\nNumber of Bears Created: {Bear.numOfBears}")

# Access the static variable numOfTigers
print(f'Number of Tigers Created:{Tiger.numOfTigers}')

# Access the static variable numOfAnimals
print(f"\n\nNumber of Animals Created: {Animal.numOfAnimals}")

# Output the static variable numOfTigers
print(f"\n\nNumber of Tigers Created: {Tiger.numOfTigers}")

# Output the Animals

for hyena in list_of_hyenas:
    print(hyena.animal_id + ", " + hyena.name + "; birthdate:" + str(hyena.birth_date) + "; " + hyena.color +
          "; " + hyena.gender + "; " + hyena.weight + "; " + hyena.originating_zoo + "; arrived: " +
          str(hyena.date_arrival))

for lion in list_of_lions:
    print(lion.animal_id + ", " + lion.name + "; birthdate:" + str(lion.birth_date) + "; " + lion.color +
          "; " + lion.gender + "; " + lion.weight + "; " + lion.originating_zoo + "; arrived: " +
          str(lion.date_arrival))

for bear in list_of_bears:
    print(bear.animal_id + ", " + bear.name + "; birthdate:" + str(bear.birth_date) + "; " + bear.color +
          "; " + bear.gender + "; " + bear.weight + "; " + bear.originating_zoo + "; arrived: " +
          str(bear.date_arrival))

for tiger in list_of_tigers:
    print(tiger.animal_id + ", " + tiger.name + "; birthdate:" + str(tiger.birth_date) + "; " + tiger.color +
          "; " + tiger.gender + "; " + tiger.weight + "; " + tiger.originating_zoo + "; arrived: " +
          str(tiger.date_arrival))
