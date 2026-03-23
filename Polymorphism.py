#POLYMORPHISM :-
#operator overloading :-
a=2;b=4
print(a+b)
print(a.__add__(b))
print(a.__add__(6))
print(a.__sub__(1))
print(a.__mul__(5))
#print(a.__div__(2))
print(a.__pow__(2))
print(a.__le__(8))
print(a.__ge__(3))
a=[1,2,3,4,5,6,7];b=[6,7,8,9,10,11]
print(a.__add__(b))
print(a.__getitem__(3))
print(b.__getitem__(5))
a="code";b="gnan"
print(a.__add__(" "+b))
print("simha".__add__(" "+"course"))
print("simha".__add__(" "+"python").title())
