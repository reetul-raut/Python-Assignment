class Vehicle:
    def move(self):
        print("Vehicle is moving")


class Car(Vehicle):
    def move(self):
        print("Driving on the road")


class Bicycle(Vehicle):
    def move(self):
        print("Pedaling on the road")


# Demonstrating polymorphism
def demonstrate_movement(vehicle):
    vehicle.move()


# Create objects
car = Car()
bicycle = Bicycle()

# Call move() on both objects
demonstrate_movement(car)
demonstrate_movement(bicycle)