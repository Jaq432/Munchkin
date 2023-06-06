class Item:
    def __init__(self):
        # Define all of the default attributes of the item
        self.itemName = ""
        self.itemType = ""
        self.itemAttack = 0
        self.itemCost = 0
        self.itemSpecialProperties = ""

    def __init__(self, 
                 itemName, 
                 itemType, 
                 itemAttack, 
                 itemCost, 
                 itemSpecialProperties):
        # Define all of the declared attributes of the monster
        self.itemName = str(itemName)
        self.itemType = str(itemType)
        self.itemAttack = int(itemAttack)
        self.itemCost = int(itemCost)
        self.itemSpecialProperties = str(itemSpecialProperties)

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
