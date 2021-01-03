# Python version 3.9

def printer(list, level):  # Συναρτηση που εκτυπωνει τις λιστες σε m x n
    if level == 1:
        x = 4
        y = 4
        n = 24
    elif level == 2:
        x = 4
        y = 10
        n = 60
    else:
        x = 4
        y = 13
        n = 78
    print('\t', end='')
    for p in range(y):
        print(f'{p + 1}\t|'.expandtabs(5), end='')
    print()
    for i in range(x):
        print('\t', end='')
        for _ in range(n):
            print('-', end='')
        print()
        print(f'{i + 1}\t', end='')
        for z in range(y):
            print(f"{list[i][z][0]}{list[i][z][1]}\t|".expandtabs(5), end='')
        print()
    print('\t', end='')
    for _ in range(n):
        print('-', end='')
    print('\n')


def make(lst, lvl):  # Συναρτηση που φτιαχνει τις λιστες σε m x n
    lista = []
    if lvl == 1:
        x = 4
        y = 4
    elif lvl == 2:
        x = 4
        y = 10
    else:
        x = 4
        y = 13
    for i in range(x):
        l = []
        for z in range(y):
            l.append(lst.pop())
        lista.append(l)
    return lista


def point(x, i):  # Συναρτηση που υπολογιζει τους ποντους
    if x == 'A':
        points[i] += 1
    elif x == 'J':
        points[i] += 10
    elif x == 'Q':
        points[i] += 10
    elif x == 'K':
        points[i] += 10
    else:
        for y in range(2, 11):
            if x == y:
                points[i] += y


def pick(p, i):  # Συναρτηση που παιρνει ως εισοδο τις θεσεις που δινει ο χρηστης
    if p:
        print(f'{list_players[i]} παιζει!')
        for z in range(2):
            pos = int(input(f'Δωσε θεση{z + 1}: ')) - 1
            picks[z] = pos
        while (picks[0] < 0 or picks[0] > x) or (picks[1] < 0 or picks[1] > y) or (
                state[picks[0]][picks[1]] == 'open'):
            for z in range(2):
                pos = int(input(f'Δωσε θεση{z + 1}: ')) - 1
                picks[z] = pos
        state[picks[0]][picks[1]] = 'open'
        for z in range(2, 4):
            pos = int(input(f'Δωσε θεση{z + 1}: ')) - 1
            picks[z] = pos
        while (picks[2] < 0 or picks[2] > x) or (picks[3] < 0 or picks[3] > y) or (
                state[picks[2]][picks[3]] == 'open'):
            for z in range(2, 4):
                pos = int(input(f'Δωσε θεση{z + 1}: ')) - 1
                picks[z] = pos
        state[picks[2]][picks[3]] = 'open'
    else:
        for z in range(4, 6):
            pos = int(input(f'Δωσε θεση{z + 1}: ')) - 1
            picks[z] = pos
        while (picks[4] < 0 or picks[4] > x) or (picks[5] < 0 or picks[5] > y) or state[picks[4]][picks[5]] == 'open':
            for z in range(4, 6):
                pos = int(input(f'Δωσε θεση{z + 1}: ')) - 1
                picks[z] = pos


def match(i, sum, flag=0):  # Συναρτηση που ελεγχει αν οι καρτες ταιριαζουν μεταξυ τους
    hidden[picks[0]][picks[1]] = deck[picks[0]][picks[1]]
    hidden[picks[2]][picks[3]] = deck[picks[2]][picks[3]]
    printer(hidden, level)
    if deck[picks[0]][picks[1]][1] == deck[picks[2]][picks[3]][1]:  # Ελεγχει αν ταιριαζουν οι καρτες
        sum += 1
        point(deck[picks[0]][picks[1]][1], i)
        if sum == N:
            return flag, sum
        if deck[picks[0]][picks[1]][1] == 'J':  # Αν οι καρτες εχουν φιγουρα το J τοτε καλει την pick και την match
            pick(1, i)
            flag, sum = match(i, sum)
        elif deck[picks[0]][picks[1]][
            1] == 'K':  # Αν οι καρτες εχουν φιγουρα το K τοτε επιστεφει το flag=1 ωστε να χασει ο επομενος παιχτη τη σειτα του
            flag = 1
            return flag, sum
    elif (deck[picks[0]][picks[1]][1] == 'K' or deck[picks[2]][picks[3]][1] == 'K') and (
            deck[picks[0]][picks[1]][1] == 'Q' or deck[picks[2]][picks[3]][
        1] == 'Q'):  # Ελεχγει αν οι καρτες εχουν τις φιογυρες K και Q Τοτε καλει την pick για να ζητησει απο το χρηστη 3η καρτα
        pick(0, i)
        print()
        hidden[picks[4]][picks[5]] = deck[picks[4]][picks[5]]
        printer(hidden, level)
        if deck[picks[0]][picks[1]][1] == deck[picks[4]][picks[5]][1]:
            sum += 1
            state[picks[4]][picks[5]] = 'open'
            point(deck[picks[0]][picks[1]][1], i)
            hidden[picks[2]][picks[3]] = ('*', '')
            if sum == N:
                return flag, sum
        elif deck[picks[2]][picks[3]][1] == deck[picks[4]][picks[5]][1]:
            sum += 1
            state[picks[4]][picks[5]] = 'open'
            point(deck[picks[2]][picks[3]][1], i)
            hidden[picks[0]][picks[1]] = '*'
            if sum == N:
                return flag, sum
        else:
            hidden[picks[0]][picks[1]], hidden[picks[2]][picks[3]], hidden[picks[4]][picks[5]] = ('*', ''), ('*', ''), (
                '*', '')
    else:
        hidden[picks[0]][picks[1]], hidden[picks[2]][picks[3]] = ('*', ''), ('*', '')
        state[picks[0]][picks[1]], state[picks[2]][picks[3]] = 'closed', 'closed'
    return flag, sum


print('Καλωσήλθατε στο Matching Game!\n')

list_players = []
while True:
    pl = int(input('Δωσε αριθμο παιχτων: '))
    while pl < 2:
        pl = int(input('Δωσε αριθμο παιχτων: '))
    level = int(input('Δωσε επιπεδο: '))
    while level < 1 or level > 3:
        level = int(input('Δωσε επιπεδο: '))
    if level == 1:
        x = 3
        y = 3
        N = 8
    elif level == 2:
        x = 3
        y = 9
        N = 20
    else:
        x = 3
        y = 12
        N = 26
    for i in range(pl):
        player = input(f'Δωσε ονομα για τον παιχτη{(i + 1)}: ')
        list_players.append(player.capitalize())
    print()
    break
kind = {'♥', '♦', '♣', '♠'}
number = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
if level == 1:
    numbers = {number.pop() for i in range(4)}
    deck = {(k, n) for k in kind for n in numbers}
    hidden = [('*', '') for k in kind for n in numbers]
elif level == 2:
    numbers = {number.pop(i) for i in range(9, -1, -1)}
    deck = {(k, n) for k in kind for n in numbers}
    hidden = [('*', '') for k in kind for n in numbers]
else:
    deck = {(k, n) for k in kind for n in number}
    hidden = [('*', '') for k in kind for n in number]

list(deck)
state = ['closed' for k in range(len(deck))]
state = (make(state, level)).copy()
deck = (make(deck, level)).copy()
hidden = (make(hidden, level)).copy()
printer(hidden, level)
picks = [0, 0, 0, 0, 0, 0]
points = [0 for i in range(pl)]
list_players.sort()  # Τοποθετει τους παιχτες σε αλφαβητική σειρα
printer(deck, level)
active_game = True
sum = 0  # Το συνολο των ζευγαριων που εχουν βρεθει
flag = 0
while active_game:
    for i in range(pl):
        if flag:
            flag = 0
            continue
        else:
            pick(1, i)
            print()
            flag, sum = match(i, sum)
        if sum == N:
            active_game = False
            break
for i in range(pl):
    print(f'{list_players[i]}: {points[i]}')
max = points[0]
winner = list_players[0]
for i in range(1, pl):  # Ελεγχει ποιος ειναι ο νικητης
    if max < points[i]:
        max = points[i]
        winner = list_players[i]
print(f'Ο νικητης ειναι: {winner}')