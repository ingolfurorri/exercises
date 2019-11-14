class WholeNumber:
    def __init__(self, num = 0):
        if(type(num) == int):
            self.__num = int(num)
        else:
            self.__num = None

    def __add__(self, obj):
        num3 = self.__num + obj.__num
        if(num3 > -1):
            return num3
        else:
            return None

    def __sub__(self, obj):
        num3 = self.__num - obj.__num
        if(num3 > -1):
            return num3
        else:
            return None

    def __mul__(self, obj):
        num3 = self.__num * obj.__num
        if(num3 > -1):
            return num3
        else:
            return None

    def __str__(self):
        return "{}".format(self.__num)

