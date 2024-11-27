# Assignment 2 : Polymorphism challange 
# vehicles.py

class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling 🚲")

# Example usage
if __name__ == "__main__":
    vehicles = [Car(), Plane(), Bicycle()]

    for vehicle in vehicles:
        vehicle.move()