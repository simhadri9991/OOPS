#OOPS SYNTAX :-

'''class classname():
    name="codegnan"
    year=2018
    place="vja"
    def fname(method):
        print(statement....)
a=classmate()
print(dir(a))
a.fname()'''

#class declaration

'''class details():
    name="simha"
    age=22
    place="vja"
    def display(self):
        print(self.name,self.age,self.place)
a=details()
print(dir(a))
a.display()'''


#object instantiation

'''class details():
    def data(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=details()
print(dir(a))
a.data("simha",22,"vja")
a.display()
b=details()
b.data("aditya",23,"vja")
b.display()'''

#Creating a constructor

'''class details():
    def __init__(self,name,age,place):
        self.names=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=details("simhadri",22,"vja")
a.display()
b=details("aditya",23,"vja")
b.display()'''

#runtime Method 1
'''
class details():
    def __init__(self):
        self.name=input("name:")
        self.age=int(input("age:"))
        self.place=input("place:")
    def display(self):
        print(self.name,self.age,self.place)
a=details()
a.display()
'''

#runtime Method 2
class details():
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=details(input("name:"),int(input("age:")),input("Place:"))
a.display()


































