# Decorators 

# Static Methods 
# Methods that don't use the self parameter (work at class level).

# Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function,
# without permanently modifying it.



class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    @staticmethod
    def hello():
        print(f"Hello: ")

    def avg_marks(self):
        sum = 0
        for i in self.marks:
            sum += i
        avg = sum/len(self.marks)
        print(f"The avg marks of {self.name} is {avg}.")
        

s1 = student("Tony Stark", [87,99,98])
s1.avg_marks()
s1.hello()