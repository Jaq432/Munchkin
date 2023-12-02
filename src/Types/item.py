class Item:
    def __init__( # initialization
        self,
        inputItemName: str,
        inputItemType: str,
        inputItemAttack: int,
        inputItemCost: int,
        inputItemSpecialProperties: str,
        inputItemDropChance: int,
    ):
        # Define all of the declared attributes of the monster
        self.itemName = str(inputItemName)
        self.itemType = str(inputItemType)
        self.itemAttack = int(inputItemAttack)
        self.itemCost = int(inputItemCost)
        self.itemSpecialProperties = str(inputItemSpecialProperties)
        self.itemDropChance = int(inputItemDropChance)

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
