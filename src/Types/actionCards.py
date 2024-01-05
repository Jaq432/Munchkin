class ActionCard:
    def __init__( # initialization
        self,
        actionCardName: str,
        actionCardCost: int,
        actionCardSpecialProperties: str,
        actionCardDropChance: int,
        actionCardMonsterAssist: bool,
    ):
        # Define all of the declared attributes of the monster
        self.actionCardName = str(actionCardName)
        self.actionCardCost = int(actionCardCost)
        self.actionCardSpecialProperties = str(actionCardSpecialProperties)
        self.actionCardDropChance = int(actionCardDropChance)
        self.actionCardMonsterAssist = bool(actionCardMonsterAssist)

    # Getters
    def getName(self):
        return self.actionCardName

    def getCost(self):
        return self.actionCardCost

    def getSpecialProperties(self):
        return self.actionCardSpecialProperties
    
    def getDropChance(self):
        return self.actionCardDropChance
    
    def getMonsterAssist(self):
        return self.actionCardMonsterAssist

    # Setters
    def setName(self, data):
        self.actionCardName = data

    def setCost(self, data):
        self.actionCardCost = data

    def setSpecialProperties(self, data):
        self.actionCardSpecialProperties = data

    def setDropChance(self, data):
        self.actionCardDropChance = data

    def setMonsterAssist(self, data):
        self.actionCardMonsterAssist = data