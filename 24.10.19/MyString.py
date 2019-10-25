class MyString:
    def __init__(self, str1 = ''):
        self.str1 = str1

    def __str__(self):
        return None

    def __sub__(self, obj):
        return abs(len(self.str1) - len(obj.str1))

    def __gt__(self, obj):
        return len(self.str1) > len(obj.str1)

#Main
a = MyString("What Does Tesla's Automated Truck Mean for Truckers?")
b = MyString('Answer: Hard to say.')
print(a > b)
print(a - b)
