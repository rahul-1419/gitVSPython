class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof!")

# Create object
my_dog = Dog("Buddy", "Golden Retriever")

# Call method
my_dog.bark()
