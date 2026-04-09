class item():

    def __init__(self, name, weight, amount):
        """
        An item in the storage system
        """
        self.name = name
        self.itemWeight = weight
        self.amount = amount

    def getName(self):
        """
        Returns name of the item
        """
        return self.name
    
    def getItemWeight(self):
        """
        Returns weight of a single item
        """
        return self.itemWeight

    def getTotWeight(self):
        """
        Returns total weight of all items
        (singWeight multiplied by amount)
        """
        return self.itemWeight*self.amount

    def getAmount(self):
        """
        Returns the amount of the item
        """
        return self.amount