class Player:
    def __init__(self, name):
        # Define all of the default attributes of the player
        self.personalName = name
        self.personalLevel = 1
        self.personalRace = []
        self.personalClass = []
        self.personalWeapon = []
        self.personalItems = []
        self.attack = 0
        self.cardsInHand = []

    # Getters
    def getName(self):
        return self.personalName

    def getLevel(self):
        return self.personalLevel

    def getRace(self):
        return self.personalRace

    def getClass(self):
        return self.personalClass

    def getWeapons(self):
        return self.personalWeapon

    def getWeaponCount(self):
        return len(self.getWeapons())

    def getAttack(self):
        attackSum = self.attack

        # We need to account for dual wielding
        for weapon in self.personalWeapon:
            print("a")
            attackSum += weapon.getAttack()

        for item in self.personalItems:
            print("b")
            attackSum += item.getAttack()

        return attackSum

    def getCardsInHand(self):
        return self.cardsInHand

    # Setters
    def setName(self, data):
        self.personalName = str(data)

    def setLevel(self, data):
        # This does relative level adjustments based on the characteristics of the monster
        self.personalLevel += data

    def setRace(self, data):
        # The game might be able to have dual-race
        self.personalRace = data

    def setClass(self, data):
        if self.personalClass is "barbarian" and (self.getWeaponCount < 2):
            print("Prompt to remove one of the weapons.")
        # The game might be able to have dual-class
        self.personalClass = data

    def setWeapon(self, data):
        # The game has regulations around weapon equipment
        if (self.personalClass is "barbarian") and (self.getWeaponCount < 2):
            self.personalWeapon = data
        elif self.getWeaponCount != 1:
            self.personalWeapon = data
        else:
            print("Prompt to remove the weapon.")

    def sets(self, data):
        self.personalItems.append(data)

    def setCardsInHand(self, data):
        self.cardsInHand.append(data)

    # Deleters
    def deleteItem(self, data):
        self.personalItems.remove(data)

    def deleteWeapon(self, data):
        self.personalWeapon.remove(data)
