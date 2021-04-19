import random

corpus = input()
# corpus.txt
f = open(corpus, "r", encoding="utf-8")



list_view = []
for i in f:
    list_view.append(i.split(' '))

new_list = []
for i in list_view:
    for j in i:
        if '\n' in j:
            j = j.replace('\n', '')
        new_list.append(j)


trigrams = []
c = 2
while c < len(new_list) - 2:
    trigrams.append([new_list[c], new_list[c+1], new_list[c+2]])
    c += 2


bool_flag = 1
count = 1
for i in range(10):
    array = ['qwerty']

    while True:
        two = random.choice(trigrams)

        if two[0][0].upper() == two[0][0] and two[0].isalpha():
            print(*two, end=' ')
            break

    while True:
        three = random.choice(trigrams)

        flag = 0

        for i in three:
            if i in two:
                flag = 1

        if flag:
            continue

        if three[0][0].upper() == three[0][0] and three[0].isalpha():
            continue

        if '.' in three[-1] or '!' in three[-1] or '?' in three[-1] or '...' in three[-1]:
            continue
        if '.' in three[0] or '!' in three[0] or '?' in three[0] or '...' in three[0]:
            continue
        if '.' in three[1] or '!' in three[1] or '?' in three[1] or '...' in three[1]:
            continue

        print(*three, end=' ')
        break

    while True:
        one = random.choice(trigrams)

        flag = 0

        for i in one:
            if i in three:
                flag = 1

        if flag:
            continue

        if one[0][0].upper() == one[0][0] and one[0].isalpha():
            continue

        if '.' in one[-1] or '!' in one[-1] or '?' in one[-1] or '...' in one[-1]:
            print(*one, end=' ')
            break

    bool_flag = 1
    count = 1
    print()
