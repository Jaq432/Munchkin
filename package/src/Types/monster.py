class Monster:
    def __init__(
        self,
        monsterName: str,
        monsterType: str,
        monsterAttack: int,
        monsterDescription: str,
        monsterLevelsGain: int,
        monsterLootGain: int,
        monsterSpawnChance: int,
    ):
        # Define all of the declared attributes of the monster
        self.monsterName = str(monsterName)
        self.monsterType = str(monsterType)
        self.monsterAttack = int(monsterAttack)
        self.monsterDescription = str(monsterDescription)
        self.monsterLevelsGain = int(monsterLevelsGain)
        self.monsterLootGain = int(monsterLootGain)
        self.monsterSpawnChance = int(monsterSpawnChance)

    # Getters
    def getName(self):
        return self.monsterName

    def getType(self):
        return self.monsterType

    def getAttack(self):
        return self.monsterAttack

    def getDescription(self):
        return self.monsterSpecialProperties

    def getLevelsGain(self):
        return self.monsterLevelsGain

    def getLootGain(self):
        return self.monsterLootGain
    
    def getSpawnChance(self):
        return self.monsterSpawnChance

    # Setters
    def setName(self, data):
        self.monsterName = data

    def setType(self, data):
        self.monsterType = data

    def setAttack(self, data):
        self.monsterAttack = data

    def setDescription(self, data):
        self.monsterSpecialProperties = data

    def setLevelsGain(self, data):
        self.monsterLevelsGain = data

    def setLootGain(self, data):
        self.monsterLootGain = data

    def setSpawnChance(self, data):
        self.monsterSpawnChance = data