class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.idxs = {}
        self.vals = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.idxs:
            return False
        self.idxs[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.idxs:
            return False
        self.idxs[self.vals[-1]] = self.idxs[val]
        self.vals[self.idxs[val]] = self.vals[-1]
        self.vals.pop()
        del self.idxs[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.vals)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
