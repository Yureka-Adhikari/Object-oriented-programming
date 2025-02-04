class Dog:
    animal="Dog"
    
    def __init__(self, name, age, species, exercise):
        self.name= name
        self.age= age
        self.species = species
        self.exercise = exercise
        
rocky = Dog("Rocky", 5, "German Shepard", "Regular exercise")
luna = Dog("Luna", 9, "Golden Retreiver", "Lots of exercise")
Oreo = Dog("Oreo", 8, "Pug", "Do not exercise much")
bambi = Dog("Bambi", 7, "American Eskimo", "Regular exercise")
husku = Dog("Husku", 6, "Husky", "Lots of exercise")

print(f"Rocky is a {rocky.animal} which is {rocky.species}")
print(f"Luna is a {luna.animal} which is {luna.species}")
print(f"Oreo is a {Oreo.animal} which is {Oreo.species}")
print(f"Bambi is a {bambi.animal} which is {bambi.species}")
print(f"Husku is a {husku.animal} which is {husku.species}")

print()

print(f"{rocky.name} is {rocky.age}")
print(f"{luna.name} is {luna.age}")
print(f"{Oreo.name} is {Oreo.age}")
print(f"{bambi.name} is {bambi.age}")
print(f"{husku.name} is {husku.age}")

print()

print(f"{rocky.name} needs {rocky.exercise} per day")
print(f"{luna.name} is {luna.exercise} per day")
print(f"{Oreo.name} is {Oreo.exercise} per day")
print(f"{bambi.name} is {bambi.exercise} per day")
print(f"{husku.name} is {husku.exercise} per day")
