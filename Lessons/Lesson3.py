# import requests

# def p24():
#   url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
#   r = requests.get(url)
#   data = r.json()

#   print(data)

#   l =[]
#   for i in data:
#     text = '{} {}/{}'.format(i['ccy'],i['buy'],i['sale'])
#     # print(text)
#     l.append(text)

# # print(l)
#   print()
#   s = "\n";
#   message = s.join(l)

#   return message
#   # print(message)

# msg = p24()
# print(msg)
# def is_alpha(msg):
#   for i in msg:
#     if i.isalpha():
#       # print('{} {}'.format(i,True))
#       return False
#   return True

# # -*- coding: utf-8 -*-
# import time
# import telepot
# from telepot.loop import MessageLoop
# import requests

# def handle(msg):
#     content_type, chat_type, chat_id = telepot.glance(msg)
#     print(content_type, chat_type, chat_id)
#     if '/p24' == msg['text']:
#       msg['text'] = p24()

#     if is_alpha(msg['text']):
#       msg['text'] = eval(msg['text'])

#     print(msg['text'])
#     bot.sendMessage(chat_id, msg['text'])

# TOKEN = '635583256:AAEmQXtTb7pI7q39Z6OXNXCfsymnNfNGWaA'

# bot = telepot.Bot(TOKEN)
# MessageLoop(bot, handle).run_as_thread()
# print('Listening ...')

# while 1:
#     time.sleep(10)

# #sudo pip install requests --upgrade
# #sudo pip install telepot --upgrade

# # d = {}
# # def dec(foo):
# #   def w(name):
# #     if name not in d:
# #       d[name] = foo(name)
# #     return d[name]
# #   return w

# # @dec
# # def foo(n):
# #   print(f'Run foo({n})')
# #   return n**100

# # print()

# # print(foo(2))
# # print(foo(2))
# # print(foo(3))
# # print(foo(2))
# # print(foo(2))
# # print(foo(3))
# # print(foo(2))
# # print(foo(2))
# # print(foo(3))
# # print(foo(2))
# # print(foo(2))
# # print(foo(3))

# # def foo(name):
# #   return f'Hi {name}!'

# # def dec(foo):
# #   def wrapper(*l, **d):
# #     return '<h1>'+foo(*l, **d)+"</h1>"
# #   return wrapper

# # foo = dec(foo)
# # # print(foo('Mike'.upper()))

# # # print(dec(foo)('Mike'.upper()))

# # print(foo('Mike'))

# # @dec
# # def foo(name):
# #   return f'Hi {name}!'
# # print(foo('Mike'))

# # def foo(n):
# #   def f():
# #     return '@'*n
# #   return f

# # f1 = foo(5)
# # print(foo(5))
# # print(f1())
# # print(foo(5)())

# # len = lambda obj: obj.__len__()
# # print(len('MIke1'))

# # foo = lambda n: len(n)
# # print(foo('Mike'))

# # foo = lambda f,n: f(n)
# # print(foo(len,'Alexxxxx'))

# # def len(obj):
# #   return obj.__len__()


# # def foo(name):
# #   return f'Hi {name}!'
# # f0 = lambda name: f'Hi {name}!'
# # print(f0('Mike'))


# # def foo(f, n):
# #   return f(n)
# # print(foo(len, d))


# # def pow(*l, **d):
# #   #print(l, d)
# #   return d['n']**d['m']

# # l = [2, 5]
# # d = {'n': 2, 'm': 5}

# # print(pow(100, 'H1', a=1, b=2, **d))
# # print(pow(**d))
# # def pow(n, m):
# #   return n**m

# # l = [2, 5]
# # d = {'n': 2, 'm': 5, (1,2):2}
# # d[0]=2
# # print(pow(n=2, m=5))

# # s='s'*1000
# # print(id(s))
# # s1='s'*1000
# # print(id(s1))

# # print(id(l))
# # print(l)
# # l.append(1)
# # print(id(l))
# # print(l)

# #  def foo(name):
# #   print('Hello!')
# #   # return '{}, {}'.format('Hi', name)
# #   return f'Hi {name}!'

# # print(foo('Mike'))

# # def pow(n,m):
# #   return n ** m
# # print(pow(3,2))

# # razpakovka
# # l = [2,5]
# # print(pow(*l))

# # zapakovka
# # def pow(*l):
# #   print(l)
# #   return l[0] ** l[1]

# # l = [2,5,5,6,7,7,8]
# # print(pow(*l))

# # def pow(n=2,m=3):
# #   return n ** m
# # print(pow(2))
# # print(pow(n=4,m=2))