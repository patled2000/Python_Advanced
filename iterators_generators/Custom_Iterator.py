class MyNumbers:
    def __init__(self,n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= self.n:
            val = self.current
            self.current += 1
            return val
        else:
            raise StopIteration
        
nums = MyNumbers(100)

for num in nums:
    print(num)