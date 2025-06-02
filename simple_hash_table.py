class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        """ A simple hash function convert string character 
            into unicode standard code points which use as index."""
        return sum(ord(char) for char in key) % self.size
    
    def insert(self, key, value):
        """ Insert the key value pair in the list. """
        index = self._hash(key)

        for i, (k, v) in enumerate(self.table[index]): # i = (key,value) pair position in list
            if k == key:
                self.table[index][i] = (key, value)
                return 
        self.table[index].append((key, value)) # index = list position

    def search(self, key):
        """ A method to search key, value pair."""
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None
    
    def delete(self, key):
        """ Delete the key-value pair. """
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
        return False
    
    def display(self):
        """ display the whole hash """
        for i, chain in enumerate(self.table):
            print(f"index.{i}: {chain}")

ht = HashTable(11)
ht.insert("Name","Naveen Soni")
ht.insert("Age", 19)
ht.insert("Dream", "Japan")
ht.insert("Habit", "Python coding")

print(ht.search("Name"))
print(ht.delete("Dream"))

print(ht.display())