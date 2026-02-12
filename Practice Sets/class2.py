class Dog:
    species = "Canis familiaris"

    def __init__(self ,name = None):
        self.name = name
        if name:
            self.name = "Guru Prashanth"
my_dog = Dog("Buddy")
print(my_dog.name)
print(my_dog.species)