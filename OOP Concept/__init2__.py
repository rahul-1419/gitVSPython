class dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

    def dog_details(self):
        print(f"Dog Name: {self.name}, Breed: {self.breed}")

my_dog = dog("Buddy", "Golden Retriever")

my_dog.dog_details()