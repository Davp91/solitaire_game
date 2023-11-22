from random import *
import pickle


def start():
    global bunker

    print('**** Wish Solitaire     *****')
    print('-----------------------------')
    print('**** 1 - Nytt spill     *****')
    print('**** 2 - Last inn spill *****')
    print('**** 3 - Avslutt        *****')
    handling=int(input('Velg handling: '))

    if(handling==1):
        bunker = delUt(kortStokk)
        spill(bunker)
    elif(handling==2):
        load()
    elif(handling==3):
         print('Programmet er nå avsluttet: ')
    else:
        print('Beklager, feil handling, prøv igjen')
        start()




kortStokk = []

for i in range(7,15):
    kortStokk.append(f'\u2665 {i}')
    kortStokk.append(f'\u2663 {i}')
    kortStokk.append(f'\u2666 {i}')
    kortStokk.append(f'\u2660 {i}')

def spill(kort):
    bokstav = list('ABCDEFGH')
    while True:
        if seier(kort):
            print('Du vant spillet!')
            break
        elif tap(kort):
            print('Du har tapt spillet')
            break

        else:
            for i, bunker in enumerate(kort):
                if len(bunker) > 0:
                    print(f'{bokstav[i]}: {bunker[0]} {" "* (len(bunker[0])%2)}{"X "* len(bunker[1:])}')
                else:
                    print(f'{bokstav[i]}: ')

            print('\nSkriv save for og lagre spillet til en fil')
            print('Skriv tilbake for og komme tilbake til meny')
            bruker = input('Velg 2 like kort for og fjerne: ').upper()
            if bruker == 'SAVE': save(kort)
            elif bruker == 'TILBAKE': start()
            else:
                if len(bruker) == 2:
                    c1 = bruker[0]
                    c2 = bruker[1]
                    fjernPar(c1, c2)
                else: spill(kort)

def delUt(split):
    shuffle(split)
    split = [split[x:x + 4] for x in range(0, len(split), 4)]
    return split


def fjernPar(c1, c2):
    global bunker
    bokstav = list('ABCDEFGH')
    konvertering = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

    if c1 != c2 and c1 in bokstav and c2 in bokstav and bunker[konvertering[c1]][0][2:] == bunker[konvertering[c2]][0][2:]:
        bunker[konvertering[c1]].pop(0)
        bunker[konvertering[c2]].pop(0)
    else:
        print('Feilt input. Skriv f.eks AC.')

def tap(kort):
    sammebunke = []
    for i in kort:
        try:
            sammebunke.append(int(i[0][2:]))
        except:
            continue

    sammebunke_check = set(sammebunke)
    if len(sammebunke) == len(sammebunke_check):
        return True


def seier(kort):
    if sum([len(x) for x in kort]) == 0:
        return True


def save(kort):
    pickle.dump(kort, open('save.p', 'wb'))
    print('Spillet er lagret')


def load():
    global bunker
    try:
        bunker = pickle.load(open('save.p', 'rb'))
        spill(bunker)
    except FileNotFoundError:
        print('Ingen lagret spill funnet')





bunker = delUt(kortStokk)

start()
