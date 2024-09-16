
import math

G = 6.673 * math.pow(10, -11) 
class Star:
    def __init__(self, **components):

        if "name" in components.keys(): self.name = components["name"] 
        else: self.name = "Star"
        if "mass" in components.keys(): self.mass = components["mass"] 
        else: self.mass = 0
        if "radius" in components.keys(): self.radius = components["radius"]
        else: self.radius = 0


    def __str__(self):
        return f"{self.name}: {self.mass} kg"
    
    def gravfield(self, body_mass, bodies_distance):
        f = (G * self.mass * body_mass) / ((bodies_distance * 1000) * (bodies_distance * 1000))
        return f

    def gravaccel(self):
        g = (G * self.mass) / ((self.radius * 1000) * (self.radius * 1000))
        return g


earth_mass = 5.972 * math.pow(10, 24)
sun_mass = 1.989  * math.pow(10, 30)
star1 = Star(name = "Earth", mass = earth_mass, radius = 6371)
print(star1.name)
print(star1.mass)
print(star1.gravfield(sun_mass, 1.496 * math.pow(10, 8)))
