class MathDojo:

    def __init__(self):
        self._result = 0
    
    def add(self, primer, *resto):
        self._result += primer
        for num in resto:
            self._result += num
    
    def substract(self, primer, *resto):
        self._result -= primer
        for num in resto:
            self._result -= num
    
    def getVal(self):
        return self._result
    
