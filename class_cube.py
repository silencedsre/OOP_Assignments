"""

Create a class in python representing a cube, it should take the length of each side via a constructor.
The class should have two methods, one returns the volume and other the total surface area.

"""

class Cube:
    def __init__(self,length):
        self.l=length

    def volume(self):
        return (self.l)**3

    def tsa(self):
        return 6*(self.l)**2

cube_obj=Cube(4)
print("Volume is ",cube_obj.volume(), "\nTSA is ",cube_obj.tsa())