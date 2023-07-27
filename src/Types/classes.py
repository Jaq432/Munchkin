class Class:
    def __init__( # initialization
        self,
        className: str,
        classCost: int,
        classSpecialProperties: str,
        classDropChanceWeight: int,
    ):
        # Define all of the declared attributes of the monster
        self.className = str(className)
        self.classCost = str(classCost)
        self.classSpecialProperties = int(classSpecialProperties)
        self.classDropChanceWeight = int(classDropChanceWeight)

    # Getters
    def getName(self):
        return self.className

    def getCost(self):
        return self.classCost

    def getSpecialProperties(self):
        return self.classSpecialProperties

    def getDropChance(self):
        return self.classDropChanceWeight
    

    # Setters
    def setName(self, data):
        self.className = data

    def setCost(self, data):
        self.classCost = data

    def setSpecialProperties(self, data):
        self.classSpecialProperties = data

    def setDropChance(self, data):
        self.classDropChanceWeight = data
