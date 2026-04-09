class carrier():
    
    def __init__(self, carryType, carryCap):
        """
        A carrier for the storage system (horse, mule, starship etc.)
        self.type = type of the carrier
        self.capacity = amount of weight the carrier can carry
        """
        self.type = carryType
        self.capacity = carryCap

    def getType(self):
        """
        Returns type of the carrier
        """
        return self.type

    def getCapacity(self):
        """
        Returns the capacity of the carrier
        """
        return self.capacity