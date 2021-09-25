class Derivative:
    def __init__(self, x0, h):
        self.x0 = x0
        self.h = h
        self.interval = self.interval()
    def func(self, x):
        return x**2 + x**3
    def interval(self):
        if self.h < 0:
            L = [self.x0 + self.h, self.x0]
        else:
            L = [self.x0, self.x0 + self.h]
        return L
    def function(self):
        a = self.interval[0]
        b = self.interval[1]
        df = self.func(b) - self.func(a)
        dx = b - a
        return df/dx
    def printDiff(self, other):
        print([self.function(), other.function()])
