# Assignment 1: Design Your Own Class

# Parent class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.__storage = storage  # Encapsulated attribute

    def phone_info(self):
        return f"{self.brand} {self.model} with {self.__storage}GB storage"

    # Encapsulation: controlled access to storage
    def get_storage(self):
        return self.__storage

    def set_storage(self, storage):
        if storage > 0:
            self.__storage = storage
        else:
            print("Invalid storage size!")


# Child class inheriting from Smartphone
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, gpu):
        super().__init__(brand, model, storage)
        self.gpu = gpu

    # Polymorphism: overriding phone_info()
    def phone_info(self):
        return f"{self.brand} {self.model} (Gaming Edition 🎮) with GPU: {self.gpu}"


# Example usage
if __name__ == "__main__":
    phone1 = Smartphone("Apple", "iPhone 15", 256)
    phone2 = GamingPhone("Asus", "ROG Phone 8", 512, "Adreno 740")

    print(phone1.phone_info())
    print(phone2.phone_info())   # Polymorphism in action
    print("Storage before upgrade:", phone1.get_storage())
    phone1.set_storage(512)
    print("Storage after upgrade:", phone1.get_storage())

    # Activity 2: Polymorphism Challenge 🎭

    class Animal:
        def move(self):
            print("This animal moves in some way...")

    class Dog(Animal):
        def move(self):
            print("Running 🐕")

    class Bird(Animal):
        def move(self):
            print("Flying 🐦")

    class Fish(Animal):
        def move(self):
            print("Swimming 🐟")

    # Example usage
    animals = [Dog(), Bird(), Fish()]

    for a in animals:
        a.move()   # Each one behaves differently — Polymorphism
