class Animal:
    numOfAnimals = 0

    def __init__(self, species="no species", name="no name", age=99, birth_season="a season", color="a color",
                weight="99 pounds", originating_zoo="from where?"):

    # def __init__(self, species, name, age, birth_season, color, weight, originating_zoo):

        self.species = species
        self.name = name
        self.age = age
        self.birth_season = birth_season
        self.color = color
        self.weight = weight
        self.originating_zoo = originating_zoo

        Animal.numOfAnimals += 1

    @classmethod
    def create_with_species_and_name_only(cls, species: object, name: object):
        return cls(species, name)