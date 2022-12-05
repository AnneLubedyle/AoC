from itertools import zip_longest

with open("input/input5.txt") as src:
    content = src.read()

content = \
"""    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

init, moves = [elt.split('\n') for elt in content.split('\n\n')]

columns = init.pop().split()
init = [elt.replace('[',' ').replace(']',' ')[1:-1].split('   ') for elt in init]


# part 1
etat = [[elt.strip() for elt in l if elt.strip() !=''][::-1] for l in zip(*init)]
# print(etat)
while True:
    try:
        line = moves.pop(0)
        fields = line.split()

        # print(line)
    except IndexError:
        break
    nb = int(fields[1])
    fr = int(fields[3])
    to = int(fields[5])
    for i in range(nb):
        # print(i)
        # print(etat)
        # print('-->')
        etat[to-1].append(etat[fr-1].pop())
    #     print(etat)
    #     print('----')
    # print('--------------------------')

    
print(''.join([l[-1] for l in etat]))
# part 2

init, moves = [elt.split('\n') for elt in content.split('\n\n')]

columns = init.pop().split()
init = [elt.replace('[',' ').replace(']',' ')[1:-1].split('   ') for elt in init]

etat = [[elt.strip() for elt in l if elt.strip() !=''][::-1] for l in zip(*init)]

while True:
    try:
        line = moves.pop(0)
        fields = line.split()

        print(line)
    except IndexError:
        break
    nb = int(fields[1])
    fr = int(fields[3])
    to = int(fields[5])
    print(etat)
    etat[to-1] += etat[fr-1][-nb:]
    etat[fr-1] = etat[fr-1][:-nb]
    print("--->")
    print(etat)
    print('----')
    print('--------------------------')

    
print(''.join([l[-1] for l in etat]))
