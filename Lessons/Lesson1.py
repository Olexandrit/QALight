# 1Lesson
# from decimal import Decimal as D

# d = {'test':[44,77],1:1}
# print(d['test'][1]/7)

apple = {
    "code": 1,
    "content": {
        "text": "apple",
        "changedText": "apple",
        "tpl_name": "one_plus_word",
        "records": {
            "words_additions": [
                {
                    "name": "apple watch",
                    "href": "https://rozetka.com.ua/ua/search/?text=apple+watch"
                },
                {
                    "name": "apple iphone 7",
                    "href": "https://rozetka.com.ua/ua/search/?text=apple+iphone+7"
                },
                {
                    "name": "apple airpods",
                    "href": "https://rozetka.com.ua/ua/search/?text=apple+airpods"
                },
                {
                    "name": "apple iphone",
                    "href": "https://rozetka.com.ua/ua/search/?text=apple+iphone"
                },
                {
                    "name": "apple tv",
                    "href": "https://rozetka.com.ua/ua/search/?text=apple+tv"
                }
            ],
            "cats_searches": [
                {
                    "id": "80004",
                    "top_id": "80253",
                    "name": "в категорії <span class='bold'> Ноутбуки</span>",
                    "href": "https://rozetka.com.ua/ua/search/?text=apple&section_id=80004&redirected=1"
                },
                {
                    "id": "80027",
                    "top_id": "4627949",
                    "name": "в категорії <span class='bold'> Навушники</span>",
                    "href": "https://rozetka.com.ua/ua/search/?text=apple&section_id=80027&redirected=1"
                },
                {
                    "id": "651392",
                    "top_id": "4627949",
                    "name": "в категорії <span class='bold'> Смарт-годинники</span>",
                    "href": "https://rozetka.com.ua/ua/search/?text=apple&section_id=651392&redirected=1"
                }
            ]
        },
        "count": 8,
        "total_count": 0,
        "page": 0,
        "start": 0,
        "sections_menu": [

        ],
        "move_to_category": "Перейти в категорію",
        "price_with_promo": "Ціна з промокодом",
        "sudg_noth_to_find": "По вашому запиту нічого не знайдено. <nobr>Уточніть свій запит",
        "all_find_result": "Всі результати пошуку",
        "currency": "грн"
    }
}

l_apple = apple["content"]
# ["records"]["words_additions"]

# new_list = [i['name'] for i in l_apple]

# names_goods = ", ".join(new_list)
# print(apple["content"]["records"]["words_additions"][0]["name"])

# n = '+380501122333'
# print(len(n))
# if len(n) == 13:
#   print("ok")
# else:
#   print("error")

# n1 = n[:3]
# print(n1)

# if n1 == "+38":
#   n = n[3:]
#   if len(n) == 10:
#     print("ok")
#   else:
#     print("error")
#   print(n)
# else:
#   print("error")

# if n1 == "+":
#   n = n[1:]
#   if len(n) == 12:
#       n1 = n[:2]
#       print(n1)
#       if n1 == "38":
#         n = n[3:]
#         if len(n) == 10:
#           print("ok")
#         else:
#           print("error")
#         #print(n)
#       else:
#         print("error")
#       print("ok")
#   else:
#     print("error")
#   print(n)
# else:
#   print("error")

'''
print(4/2)
print(5//2)
print(5%2)
print(4**2)

print(D('6033.8')%D('5678'))
print("qwerty")
print("qwerty"[0])
print("qwerty"[2:4])

s= 'HELLO world!'
print(s[6:11])

l=[1,2,3,4,5]
print(l[2]*100)

d={'100':333,0:1,1:2}
print(len(l),len(d))
print(d['100'])
print(d[str(100)])

print(True, False)
print(bool(0))
print(bool(1222))
print()

a=4
if a >= 5:
  print('bool(a) == True')
else:
  print('bool(a) == False')
  if a==4:
    print('a=4')
'''