#152
from collections import deque
from typing import Deque
def search_gosha(p):
    verified = []
    galka = False
    while p:
        person = p.popleft()
        for i in verified:
            if person == i:
                galka = True

                break



        if galka:
            print('повтор')
            galka = False
            continue

        verified.append(person)
        if person == 'gosha':
            print('gosha')
            return True
        else:
            p += frends[person]
    return False
def search_x(p):
    verified = []
    galka = False
    while p:
        person = p.popleft()
        for i in verified:
            if person == i:
                galka = True

                break



        if galka:
            print('повтор')
            galka = False
            continue

        verified.append(person)
        if person == 'c':
            print('c найден')
            return True
        else:
            p += dar[person]
    return False

frends = {}
frends["you"] = ['heri','hori', 'robot']
frends["heri"] = ['tor','albert']
frends["hori"] = ['dobi','elli']
frends["robot"] = ['jon','gosha']
frends["tor"] = []
frends["albert"] = []
frends["dobi"] = []
frends["elli"] = []
frends["jon"] = []
frends["gosha"] = []

people = Deque()
people += frends["you"]



#search_gosha(people)

dar = {}
dar['ya'] = ['m','b']
dar['m'] = ['c']
dar['b'] = ['m','p']
dar['p'] = ['c','d']
dar['d'] = ['c']
dar['c'] = []

t = deque()
t+=dar['ya']
search_x(t)
#, 'jon', 'gosha'