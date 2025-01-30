class Vehicle:
    def __init__(self,speed, mileage):
        self.max_speed = speed
        self.mileage = mileage
    
ferrari = Vehicle(260, 18)
lamborghini = Vehicle(285, 28)

print(f"Ferrari max speed: {ferrari.max_speed}")
print(f"Ferrari mileage: {ferrari.mileage}")

print()

print(f"Ferrari max speed: {lamborghini.max_speed}")
print(f"Ferrari mileage: {lamborghini.mileage}")

