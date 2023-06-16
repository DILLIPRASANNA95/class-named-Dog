class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print("Name: ", self.name)
        print("Age: ", self.age)

    def get_info(self):
        print("Coat Color: ", self.coat_color)

class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color, breed_type, energy_level):
        super().__init__(name, age, coat_color)
        self.breed_type = breed_type
        self.energy_level = energy_level

    def breed_info(self):
        print("Breed Type: ", self.breed_type)

    def energy(self):
        print("Energy Level: ", self.energy_level)

class Bulldog(Dog):
    def __init__(self, name, age, coat_color, muscle_mass, personality):
        super().__init__(name, age, coat_color)
        self.muscle_mass = muscle_mass
        self.personality = personality

    def muscle(self):
        print("Muscle Mass: ", self.muscle_mass)

    def character(self):
        print("Personality: ", self.personality)

dog1 = JackRussellTerrier("Max", 5, "White", "Terrier", "Energetic")
dog2 = Bulldog("Rocky", 7, "Brown", "Strong", "Friendly")

print("\nJackRussellTerrier:")
dog1.description()
dog1.get_info()
dog1.breed_info()
dog1.energy()

print("\nBulldog:")
dog2.description()
dog2.get_info()
dog2.muscle()
dog2.character()
