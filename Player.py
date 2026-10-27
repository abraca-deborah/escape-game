class Player:

    def __init__(self):
        self.eyeColor = ""
        self.hairColor = ""
        self.hairLength = ""
        self.inventory = ["satchel", "weird key", "letter", "hunting knife"]
        self.set = False


    def setEyes(self, color):
        self.eyeColor = color

    def setHair(self, color):
        self.hairColor = color

    def setHairLength(self, length):
        self.hairLength = length


