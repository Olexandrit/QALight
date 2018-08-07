# -*- coding: utf-8 -*-
import time
import telepot
from telepot.loop import MessageLoop
import requests


# text = "GATGGAACTTGACTACGTAAATT"
# print(text)
# print(text.replace("T", "U"))

# text = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

# symbols = 'ACGT'

# print([text.count(s) for s in symbols])


# def gen():
#     for i in range(3):
#         yield i
#         # yield 2
#         # yield 3

# it = gen()
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# try:
#     print(it.__next__())
# except StopIteration:
#     print('StopIteration')
# except KeyError:
#     pass


# l = [1,2,3,1,3,4]
# # [1,3,1,3]
# r = []

# print(l)
# print("Version 1")
# for i in l:
#     if l.count(i) > 1:
#         r.append(i)
# print(r)

# print("Version 3")
# print([i for i in l if l.count(i) > 1])

# r = list(range(10))
# f = lambda x: x**2
# # 1
# print(1)
# l = []
# for i in r:
#     if i%2:
#         l.append(f(i))

# print(l)
# # 2
# print(2)
# print(filter(
# lambda x:x%2, r))
# print(list(map(f,filter(lambda x:x%2, r))))
# print(list(map(f,r)))

# # 3
# print(3)
# print([f(i) for i in r])
# print([f(i) for i in r if i%2])

def translate_yandex(msg):
    # text = 'Привет Hello world'
    text = msg

    en_dict = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ru_dict = 'АБВГДЕЁЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    en_count = 0
    ru_count = 0

    for w in text:
        nw = w.upper()

        if nw in en_dict: en_count += 1

        if nw in ru_dict:
            ru_count += 1

    print(en_count)
    print(ru_count)

    if en_count > ru_count:
        lang_trans = 'ru-en'
    else:
        lang_trans = 'en-ru'

    params = {'key': 'trnsl.1.1.20170306T191951Z.66a368c52394039f.dac56045246cb91aa8da797d95dcfff798ba92f5',
              'lang': 'ru-en', 'text': text}
    params['lang'] = lang_trans

    r = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate', params=params)
    data = r.json()
    # print("data")

    text_trans = data[u'text'][0]
    print(text_trans)
    return text_trans


def p24():
    url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
    r = requests.get(url)
    data = r.json()

    print(data)

    l = []
    for i in data:
        text = '{} {}/{}'.format(i['ccy'], i['buy'], i['sale'])
        # print(text)
        l.append(text)

    print()
    s = "\n";
    message = s.join(l)

    return message


def is_alpha(msg):
    for i in msg:
        if i.isalpha():
            # print('{} {}'.format(i,True))
            return False
    return True


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if '/p24' == msg['text']:
        msg['text'] = p24()
    elif is_alpha(msg['text']):
        msg['text'] = eval(msg['text'])
    else:
        msg['text'] = translate_yandex(msg['text']) + "/" + str(chat_id)

    print(msg['text'])
    bot.sendMessage(chat_id, msg['text'])


TOKEN = '635583256:AAEmQXtTb7pI7q39Z6OXNXCfsymnNfNGWaA'

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()

print('Listening ...')

while 1:
    time.sleep(10)