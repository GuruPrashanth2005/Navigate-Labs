import math
class Shape:
    def rectangle(self,a=None,b=None,c=None):
        if c is not None:
            return math.pi*c**2
        else:
            return a*b
area = Shape()
print(area.rectangle(5,10))
print(area.rectangle(c = 7))
