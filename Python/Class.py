class Student:
    def __init__(self,name, std, gpa, is_on_leave):
        self.name=name
        self.std=std
        self.gpa=gpa
        self.is_on_leave=is_on_leave


    def honor(self):
        if self.gpa >= 8:
            return True
        else:
            return False