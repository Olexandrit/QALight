# -*- coding: utf-8 -*-
# Flask
# SQLAlchemy
# Folder Lesson12
import Lesson12_1
import numpy as np


l =[
u"1. Британская полиция знает о местонахождении основателя WikiLeaks",
u"2. В суде США начинается процесс против россиянина, рассылавшего спам",
u"3. Церемонию вручения Нобелевской премии мира бойкотируют 19 стран",
u"4. В Великобритании арестован основатель сайта Wikileaks Джулиан Ассандж",
u"5. Украина игнорирует церемонию вручения Нобелевской премии",
u"6. Шведский суд отказался рассматривать апелляцию основателя Wikileaks",
u"7. НАТО и США разработали планы обороны стран Балтии против России",
u"8. Полиция Великобритании нашла основателя WikiLeaks, но, не арестовала",
u"9. В Стокгольме и Осло сегодня состоится вручение Нобелевских премий"]
l2 = []
for i in l:
    # print(i)
    l3 = []
    for s in i:
        
        if s.isalpha():
            l3.append(s)
        else:
            l3.append(" ")
    
    l2.append(("".join(l3)).lower())

l4=[]
for i in l2:
    l4.append(i.split())
    # print(i)
# print(l4)
l5 = []
for i in l4:
    # print(i[0])
    l4_1 = []
    for i1 in i:
        # print(i1)
        
        if len(i1) > 2:
            # print(i1)
            try:
                l4_1.append(Lesson12_1.Porter.stem(i1))
            except:
                # print(i1)
                l4_1.append(i1)
            
    l5.append(l4_1)
    
# print(l5)
l_word = []
for i in l5:
    # print(" ".join(i))
    
    for i1 in i:
        l_word.append(i1)

# print(l_word)
w_l_word = []
w_l_word = list(set(l_word))
w_l_word.sort()

# print(w_l_word)
# for i in w_l_word:
#     print(i)

matrix = []

for i in w_l_word:
    # print(i)
    m = []
    for i1 in l5:
        
        if i in i1:
            m.append(1)    
        else:
            m.append(0)

    matrix.append(m)

# print(matrix)

n_matrix = []
n_word = []


for i in range(len(matrix)):
    
    if sum(matrix[i]) > 1:
        n_matrix.append(matrix[i])
        n_word.append(w_l_word[i])

# for i in n_matrix:
#     print(i)

# for w in n_word:
#     print w,n_matrix[n_word.index(w)]

# print(n_word,n_matrix)
    # print(i)
    # print(" ".join(i))
    
LA = np.linalg
a = np.array(n_matrix)
U,s,Vh = LA.svd(a,full_matrices=False)

x = list(Vh[0])
articles = []
for c, i in enumerate(x):
    new = abs(x[0] - i)
    articles.append([new, c])
articles.sort()
sorted_articles = articles
print(sorted_articles[1:4])
x = lambda x: x[1]
print([x(i) for i in sorted_articles[1:4]])  # рекомендованные статьи для первого слова