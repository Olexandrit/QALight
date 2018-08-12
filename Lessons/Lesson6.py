# patern
# 
# Fasad
class Cat:
    say = 'meow'

class Dog:
    say = 'gaw'

class Monter():
    def kill(self):
        del self.cat
        return 'Blood pf pf pf.'

class Chupakabra(Monter, Dog):
    def __init__(self, name=''):
        self.name = name
        self.cat = Cat()
    
    @property
    def say_like_cat(self):
        try:
            return self.cat.say
        except AttributeError:
            return 'R.I.P'
    
    def __repr__(self):
        return '<Chupakabra({})>'.format(self.name)

class Flock():
    def __init__(self, count=1):
        self.set_ch = []
        self.count = count

    def make(self):
        for i in range(self.count):
            self.set_ch.append(Chupakabra(name='Chu #{}'.format(i)))
    
    def kill_cat(self):
        for i in self.set_ch:
            if 'cat' in i.__dict__:
                return i.kill()
        return "Can't do it!"
    
class Store_Flock():
    def __init__(self, flock):
        self.set_ch = flock.set_ch
        self.count = len(flock.set_ch)
    
    def make(self):
        f = Flock()
        f.set_ch = self.set_ch
        f.count = self.count
        return f

# ch = Chupakabra()
# print(ch.say, ch.say_like_cat, ch.kill(), ch.say_like_cat)
f = Flock(count=5)
f.make()
f.set_ch[0].name = 'Strong'
print(f.set_ch)

sf = Store_Flock(f)
del f
#print(f.set_ch)
f = sf.make()
print(f.set_ch)
for i in range(8):
    print(f.kill_cat())

# Store
# class Cat:
#     say = 'meow'

# class Dog:
#     say = 'gaw'

# class Monter():
#     def kill(self):
#         del self.cat
#         return 'Blood pf pf pf.'

# class Chupakabra(Monter, Dog):
#     def __init__(self, name=''):
#         self.name = name
#         self.cat = Cat()
    
#     @property
#     def say_like_cat(self):
#         try:
#             return self.cat.say
#         except AttributeError:
#             return 'R.I.P'
    
#     def __repr__(self):
#         return '<Chupakabra({})>'.format(self.name)

# class Flock():
#     def __init__(self, count=1):
#         self.set_ch = []
#         self.count = count

#     def make(self):
#         for i in range(self.count):
#             self.set_ch.append(Chupakabra(name='Chu #{}'.format(i)))
    
# class Store_Flock():
#     def __init__(self, flock):
#         self.set_ch = flock.set_ch
#         self.count = len(flock.set_ch)
    
#     def make(self):
#         f = Flock()
#         f.set_ch = self.set_ch
#         f.count = self.count
#         return f

# # ch = Chupakabra()
# # print(ch.say, ch.say_like_cat, ch.kill(), ch.say_like_cat)
# f = Flock(count=5)
# f.make()
# f.set_ch[0].name = 'Strong'
# print(f.set_ch)

# sf = Store_Flock(f)
# del f
# #print(f.set_ch)
# f = sf.make()
# print(f.set_ch)
    
# sobiratel
# class Cat:
#     say = 'meow'

# class Dog:
#     say = 'gaw'

# class Monter():
#     def kill(self):
#         del self.cat
#         return 'Blood pf pf pf.'

# class Chupakabra(Monter, Dog):
#     def __init__(self, name=''):
#         self.name = name
#         self.cat = Cat()
    
#     @property
#     def say_like_cat(self):
#         try:
#             return self.cat.say
#         except AttributeError:
#             return 'R.I.P'
    
#     def __repr__(self):
#         return '<Chupakabra({})>'.format(self.name)

# class Flock():
#     def __init__(self, count=1):
#         self.set_ch = []
#         self.count = count

#     def make(self):
#         for i in range(self.count):
#             self.set_ch.append(Chupakabra(name='Chu #{}'.format(i)))

# f = Flock(count=5)
# f.make()
# print(f.set_ch)

# abstraktnaya fabrica
# class Cat:
#     say = 'meow'
    
# class Dog:
#     say = 'gaw'
    
# class Monster():
#     def kill(self):
#         del self.cat
#         return 'Blood pf pf pf.'
        
# class Chupakabra(Monster,Dog): 
#     def __init__(self):
#         self.cat = Cat()
    
#     @property
#     def say_like_cat(self):
#         try:
#             return self.cat.say
#         except AttributeError:
#             return 'R.I.P'
        
        
#     # @property    
#     # def name(self):
#     #     return self.little_coder.name
        
# ch = Chupakabra()
# print(ch.say, ch.say_like_cat, ch.kill(),ch.say_like_cat)

# fabrica
# class Cat:
#     say = 'meow'
    
# class Dog:
#     say = 'gaw'

# class Chupakabra(Dog): 
#     def __init__(self, cat):
#         self.cat = Cat()
    
#     @property
#     def say_like_cat(self):
#         return self.cat.say
        
#     # @property    
#     # def name(self):
#     #     return self.little_coder.name
        
# ch = Chupakabra()
# print(ch.say, ch.say_like_cat)


# class Cat:
#     say = 'meow'
    
# class Dog:
#     say = 'gaw'

# class Chupakabra(Dog): 
#     def __init__(self, cat):
#         self.cat = cat
    
#     @property
#     def say_like_cat(self):
#         return self.cat.say
        
#     # @property    
#     # def name(self):
#     #     return self.little_coder.name
        
# ch = Chupakabra(Cat())
# print(ch.say, ch.say_like_cat)
        
    


# class Human():
#     def __get_death_day(self):
#         return 'Booo!'
#     def secret(self):
#         return self._Child__secret
        
# class Child(Human): 
#     atr = 'Hello'
#     def __init__(self):
#         self.__secret = 'woooo!'

# little_boy = Child()

# print(little_boy.secret())
# print(little_boy._Human__get_death_day())

# for i in dir(Child):
#     print(type(getattr(Child, i)).__name__)
#     # print(i,": ",type(getattr(Child, i)))
#     # print(type(getattr(Child, i)))
#     if type(getattr(Child, i)).__name__ == 'instancemethod':
#         print(i)

# class Singleton:
#     _store = {}
    
#     def __init__(self):
#         self.__dict__ = Singleton._store

# s1 = Singleton()
# s1.a = 1

# s2 = Singleton()
# print(s2.a)

# s2.b = 2
# print(s1.b)