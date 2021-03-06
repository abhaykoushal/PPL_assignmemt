class Animals:
    def __init__(self, legs=4, eyes=2):
        self.legs = legs
        self.eyes = eyes

class wild_animals(Animals):
    def place(self):
        print("Live in Jungle.")

class domestic_animals(Animals):    
    def place(self):
        print("Present in our surroundings.")

class carnivores(wild_animals):
    def food(self):
        print("Meat")
                        
class herbivores(wild_animals):
    def food(self):
        print("Plant based")

#animal 1        
class lion(carnivores):
    def speak(self):
        print("Roar")
    def colour(self):
        print("Yellow")

#animal 2        
class tiger(carnivores):
    def speak(self):
        print("Roar")
    def colour(self):
        print("Orange")
        
#animal 3
class hyena(carnivores):
    def speak(self):
        print("scream")
    def colour(self):
        print("Grey")

#animal 4
class deer(herbivores):
    def speak(self):
        print("bell")
    def colour(self):
        print("Brown")

#animal 5
class elephant(herbivores):
    def speak(self):
        print("trumpet")
    def colour(self):
        print("Grey")

#animal 6
class zebra(herbivores):
    def speak(self):
        print("neigh")
    def colour(self):
        print("Black and white")

#animal 7
class dog(domestic_animals):
    def speak(self):
        print("bark")
    def colour(self):
        print("brown, black, white, golden, etc.")

#animal 8        
class cat(domestic_animals):
    def speak(self):
        print("meow")
    def colour(self):
        print("Grey, brown, black, white, etc.")

#animal 9
class cow(domestic_animals):
    def speak(self):
        print("moo")
    def colour(self):
        print("white, brown, black, etc.")

#animal 10
class rabbit(domestic_animals):
    def speak(self):
        print("squeak")
    def colour(self):
        print("white, brown, black, lilac, etc.")
        

a = Animals(4, 3)
pea = cat()
pea.speak()
pea.place()
pea.colour()

print(pea.eyes)
print(pea.legs)


