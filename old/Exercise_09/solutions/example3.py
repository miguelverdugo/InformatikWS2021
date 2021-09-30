


class Star:

    def __init__(self, mass, age, metallicity):

        self.mass = mass
        self.age = age
        self.mh = metallicity

    @property
    def temperature(self):
        return "temperature(%s, %s, %s)" % self.mass, self.age, self.metallicity

    @property
    def radius(self):
        return "radius(%s, %s, %s)" % self.mass, self.age, self.metallicity

    @property
    def luminosity(self):
        return "luminosity(%s, %s, %s)" % self.temperature, self.radius, self.metallicity

    @property
    def gravity(self):
        return  "gravity(%s, %s, %s)" % self.mass, self.radius

    @property
    def spectrum(self):
        return "spectrum(%s, %s, %s)" % self.temperature, self.metallicity, self.luminosity

    @property
    def stellar_type(self):
        """
        probably looking at at lookup table
        """
        return "stellar_type(%s)" % self.spectrum

        
