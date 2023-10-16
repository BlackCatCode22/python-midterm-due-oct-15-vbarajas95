from Animal import Animal

class Lions(Animal):
    # create a static class variable as a means to keep track of the number of lions created
    numOfLions = 0

    # Create lion sound
    lion_sound = "roar"

    # Initialize empty list to store lion names
    list_of_lion_names = []

    # Define file path
    file_path = r'/Users/Vanessa/myGitDir/python-midterm-due-oct-15-vbarajas95/animalNames.txt'
    # Open file and read content
    with open(file_path, 'r') as file:
        lines = file.readlines()

        # Iterate through lines in the file
        line_num = 1
        for line in lines:
            if line_num == 3:
                is_lion_section = True
                list_of_lion_names.extend(line.strip().split(", "))
                break
            else:
                line_num += 1

    def __init__(self, name="a_name", animal_id ="an_id", birth_date="2099-01-01", color="a_color", gender = "a_gender",
                 weight="a_weight", originating_zoo="a_zoo", date_arrival="2099-01-01"):
        # Increment static variable numOfLions when a new hyena object is created
        Lions.numOfLions += 1

        # Call constructor of the parent class (Animal) with 'Lion' as the species
        super().__init__("lion", name, animal_id, birth_date, color, gender, weight, originating_zoo, date_arrival)

    def make_sound(self):
        return self.lion_sound

    # the list_of_lion_names []
    def get_lion_name(self):
        return self.list_of_lion_names.pop(0)