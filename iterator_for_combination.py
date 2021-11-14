class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.chars = characters
        self.comboLen = combinationLength
        self.combo = []
        self.combos = []
        self.generate(0)
        self.i = 0
        
    def generate(self, i):
        if len(self.combo) == self.comboLen:
            self.combos.append("".join(self.combo[:]))
            return
        for j in range(i, len(self.chars)):
            self.combo.append(self.chars[j])
            self.generate(j+1)
            self.combo.pop()
        
    def next(self) -> str:
        nextCombo = self.combos[self.i]
        self.i += 1
        return nextCombo

    def hasNext(self) -> bool:
        return self.i<len(self.combos)


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()