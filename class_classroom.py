"""
Create a class in representing a classroom.
It should have have the following attributes 'no_students' (private), 'teacher' (public) and 'class'(public).
Also define a method to print the private attribute. All the attributes should be set via the constructor.
"""

class Classroom:
    def __init__(self, no_of_students, teacher, class_):
        self.__private = no_of_students
        self.pulic_teacher=teacher
        self.pulic_class=class_

    def print_private(self):
        print("The number of students are: ", self.__private)


classroom_obj = Classroom(45, "Shreyansh", "Room no: 5")
classroom_obj.print_private()

