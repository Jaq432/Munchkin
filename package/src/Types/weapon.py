class Weapon:

    def __init__(
        self,
        weaponName,
        weaponType,
        weaponAttack,
        weaponCost,
        weaponSpecialProperties,
        weaponDropChance
    ):
        # Define all of the declared attributes of the monster
        self.weaponName = str(weaponName)
        self.weaponType = str(weaponType)
        self.weaponAttack = int(weaponAttack)
        self.weaponCost = int(weaponCost)
        self.weaponSpecialProperties = str(weaponSpecialProperties)
        self.weaponDropChance = int(weaponDropChance)

    # Getters
    def getName(self):
        return self.weaponName

    def getAttack(self):
        return self.weaponAttack

    def getCost(self):
        return self.weaponCost

    def getSpecialProperties(self):
        return self.weaponSpecialProperties

    def getType(self):
        return self.weaponType
    
    def getDropChance(self):
        return self.weaponDropChance

    # Setters
    def setName(self, data):
        self.weaponName = data

    def setAttack(self, data):
        self.weaponAttack = data

    def setCost(self, data):
        self.weaponCost = data

    def setSpecialProperties(self, data):
        self.weaponSpecialProperties = data

    def setType(self, data):
        self.weaponType = data

    def setDropChance(self, data):
        self.weaponDropChance = data