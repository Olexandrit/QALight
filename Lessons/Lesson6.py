# patern
# 

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
    
        

# ch = Chupakabra()
# print(ch.say, ch.say_like_cat, ch.kill(), ch.say_like_cat)
f = Flock(count=5)
f.make()
print(f.set_ch)

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