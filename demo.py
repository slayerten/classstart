#! /usr/bin/python
# this is a demo for class

class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_demo(self):
        print '%s:%s:'%(self.name,self.score),self.print_aa()
        

    def print_aa(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 70:
            return 'B'
        else:
            return 'C'

Wolf = Student('Wolf Cui',99)
John = Student('John Lily',86)
Q = Student('Q Yang',55)
Wolf.print_demo()
John.print_demo()
Q.print_demo()
