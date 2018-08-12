class Point():
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __add__(self,other):
        return Point(self.x + other.x,self.y+other.y)
        
    def __iter__(self):
        yield self.x 
        yield self.y
        
        
p1 = Point(1,2)
p2 = Point(3,4)

print(p1.__add__(p2))

# p3 = p1.__add__(p2)
# print(p3.x,p3.y)

p3 = p1+p2+p1
print(p3.x,p3.y)

for i in p3:
    print(i)



# class D():
#     d = 0
# class C(D):
#     d = 1
# class B(D): pass
# class A(B,C):
    
#     def __len__(self):
        
#         return 9
        
        

    
# a = A()
# print(a.d)

# print(len(a))





# class Human:
    
#     def __init__(self, name='', age=0):
#         self.name = name
#         self.age = age
    
#     # Output text priority 1
#     def __repr__(self):
#         return '__repr__:My name {}. Age {}'.format(self.name,self.age)  
    
#     # Output text priority 2    
#     def __str__(self):
#         return '__str__:My name1 {}. Age1 {}'.format(self.name,self.age) 
#         # return self.__repr__()
    
#     def func_def(self):
#         print('func_def')
        
#     @classmethod 
#     def class_method(cls,a):
#         cls.a = a
#         print('class_method',a)
        
#     @staticmethod 
#     def static_method(a,b):
#         print('static_method',a,b)
        
#     @property 
#     def propert_method(self):
#         # print('propert_method',a,b)
#         return self.__str__()
        
# h1 = Human('Mike1',21)
# h2 = Human('Nika1',22)

# Human().func_def()
# Human.func_def(Human()) # ???????

# Human.class_method('a')
# Human.static_method('a','b')

# print(h1.propert_method)

# h1.new('Mike1',21)
# h2.new('Nika1',22)

# print(h1.print_new())
# print(h2.print_new())

# Human.new(Human(),'Nika1',22)
# Human().new('Nika1',22)

# print(h1.__str__())
# print(h2.__str__())

# h1.__init__()
# h2.__init__()

# print([h1,h2])
# print(h1,h2)



# class Human: pass

# h1 = Human()
# h2 = Human()

# # h1.name = 'Mike'
# # h1.age = 20

# # h2.name = 'Nika'
# # h2.age = 22

# def new(human, name, age):
    
#     human.name = name
#     human.age = age
    
    
# new(h1,'Mike1',21)
# new(h2,'Nika1',22)

# def print_new(human):
#   return 'My name {}. Age {}'.format(human.name,human.age)  

# print(print_new(h1))
# print(print_new(h2))

# import this
# this.test = 'Hi'
# print(this.test)

# def make():
#     def foo(): pass
#     def f(n): return n**2
#     foo.test = 'Hi'
#     foo.f = f
#     return foo

# obj = make()
# print(obj.test, obj.f(11))
# print(foo.test)

# class A: 
#     'Doc string for Class A'
#     test2 = 20

# a = A()
# a2 = A()

# a.test = 10
# print(a.test)
# print(dir(a))
# print(a.__dict__)
# print(a.__doc__)
