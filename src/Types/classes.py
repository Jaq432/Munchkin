class Class:
    def __init__( # initialization
        self,
        className: str,
        classcost: int,
        classSpecialProperties: str,
        classDropChanceWeight: int,
    ):
        # Define all of the declared attributes of the monster
        self.itemName = str(itemName)
        self.itemType = str(itemType)
        self.itemAttack = int(itemAttack)
        self.itemCost = int(itemCost)
        self.itemSpecialProperties = str(itemSpecialProperties)
        self.itemDropChance = int(itemDropChance)

    # Getters
    def getName(self):
        return self.itemName

    def getAttack(self):
        return self.itemAttack

    def getCost(self):
        return self.itemCost

    def getSpecialProperties(self):
        return self.itemSpecialProperties

    def getType(self):
        return self.itemType
    
    def getDropChance(self):
        return self.itemDropChance

    # Setters
    def setName(self, data):
        self.itemName = data

    def setAttack(self, data):
        self.itemAttack = data

    def setCost(self, data):
        self.itemCost = data

    def setSpecialProperties(self, data):
        self.itemSpecialProperties = data

    def setType(self, data):
        self.itemType = data

    def setDropChance(self, data):
        self.itemDropChance = data
