class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says Woof!")

# Create object
my_dog = Dog("Buddy")

# Call method
my_dog.bark()
