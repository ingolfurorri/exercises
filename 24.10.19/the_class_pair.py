class Pair:
    def __init__(self, v1 = 0, v2 = 0):
        self.v1 = int(v1)
        self.v2 = int(v2)

    def __str__(self):
        return "Value 1: {}, Value 2: {}".format(self.v1, self.v2)

    def __add__(self, b):
        c = Pair()
        c.v1 = self.v1 + b.v1
        c.v2 = self.v2 + b.v2

        return c

    
def main():
    a = Pair(20,30)
    print(a)
    b = Pair(40, 60)
    print(b)
    c = a + b
    print(c)

main()