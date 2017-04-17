class Celcius:

    def __init__(self, temperature = 0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32

    def get_temperature(self):
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("That temperature is not possible lol")
        self._temperature = value



man = Celcius(-270)
print man.to_fahrenheit()

# Doing it a different way, with @property


class Celsius(object):

    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    def get_temperature(self):
        print "Getting value"
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("That temperature is not possible lol")
        print "Setting value"
        self._temperature = value

    # Makes a propert object temperature. It attaches some code get_temperature and
    # set_temperature to the member attribute accesses.
    temperature = property(get_temperature, set_temperature)

c = Celsius(20)
c.temperature = 900
print c.temperature

# Basically what happens is that is you set the class attribute temperature = some number,
# THen instead of just setting it equal, the second function in property() will be called with
# that number as an argument. If you try to get the temperature, the first funciton in property
# will be called (which returns the number) instead of just returning the number on its own.
# The actual property function: property(fget=None, fset=None, fdel=None, doc=None) fdel will delete something
