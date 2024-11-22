class Tank:
    def __init__(self, country, model):
        self.country = country
        self.model = model
        self._speed = 0
        self._direction = 0
        self._location = {'X':0, 'y':0, 'z':0}