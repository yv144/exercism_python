# Given an age in secods, calculate how old someone
# is in term of a given planet's solar years.

db = {
    'Mercury': 0.2408467,
    'Venus':	0.61519726,
    'Earth':	1.0,
    'Mars':	1.8808158,
    'Jupiter':	11.862615,
    'Saturn':	29.447498,
    'Uranus':	84.016846,
    'Neptune':	164.79132,
}
class SpaceAge:
    def __init__(self,seconds) -> None:
        self.seconds = seconds
    def on_earth(self) -> float: 
        return round(self.seconds/60/60/24/365.25,2)
    
    def on_earth_precise(self) -> float: 
        return self.seconds/60/60/24/365.25
    def on_mercury(self): return round(self.on_earth_precise()/db['Mercury'],2)
    def on_venus(self):   return round(self.on_earth_precise()/db['Venus'],2)
    def on_mars(self):    return round(self.on_earth_precise()/db['Mars'],2)
    def on_jupiter(self): return round(self.on_earth_precise()/db['Jupiter'],2)
    def on_saturn(self):  return round(self.on_earth_precise()/db['Saturn'],2)
    def on_uranus(self):  return round(self.on_earth_precise()/db['Uranus'],2)
    def on_neptune(self): return round(self.on_earth_precise()/db['Neptune'],2)

