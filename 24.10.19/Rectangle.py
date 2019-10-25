class Rectangle:
    def __init__(self, length = 0, width = 0):
        if(length < 0):
            length = 0
        if(width < 0):
            width = 0

        self.__length = int(length)
        self.__width = int(width)

    def area(self):
        self.area_int = self.__length * self.__width
        return (self.area_int)

    def perimeter(self):
        self.parimeter = 2*self.__length + 2*self.__width
        return (self.parimeter)

    def __str__(self):
        return "Length: {}, Width: {}".format(self.__length, self.__width)

    def __repr__(self):
        return "Rectangle({},{})".format(self.__length, self.__width)

    def __eq__(self, obj):
        return self.area_int == obj.area_int

#Main
obj1 = Rectangle(2,-3)
print(obj1.area()) == print('0')
print(obj1.perimeter()) == print('4')
print(obj1) == print('Length: 2, Width: 0')


assert obj1.area() == 0
assert obj1.perimeter() == 4
assert str(obj1) == 'Length: 2, Width: 0'