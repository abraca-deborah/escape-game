class Player:

    def __init__(self, eyeColor, hairColor, hairLength):
        self.eyeColor = eyeColor
        self.hairColor = hairColor
        self.hairLength = hairLength
        self.inventory = ["satchel", "weird key", "letter", "hunting knife"]


    def setEyes(self, color):
        self.eyeColor = color

    def setHair(self, color):
        self.hairColor = color

    def setHairLength(self, length):
        self.hairLength = length


