import pandas as pd

with open('input/input7.txt') as f:
    cmd = f.read()

cmd = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""


root = list()
cur=''
for line in cmd.split('$')[2:]:
    seq = line.strip().split('\n')
    if seq[0] == 'ls':
        for elt in seq[1:]:
            a, b = elt.split()
            newelt = {'id': '/'.join([cur,b])}
            if a=='dir':
                newelt.update({'type':'dir'})
            else:
                newelt.update({'type':'fic', 'taille':int(a)})
            root.append(newelt)
            continue
    if seq[0][:2]=='cd':
        dest = seq[0].split()[1]
        if dest == '..':
            cur = '/'.join(cur.split('/')[:-1])
        else:
            cur = '/'.join([cur,dest])

data = pd.DataFrame(root)
for dir in data.query('type=="dir"').id:
    data.loc[data.id==dir,'taille'] = \
        data.query('id.str.startswith(@dir) & type=="fic"', engine='python').taille.sum()

# part 1
data.query('type=="dir" and taille<=100000').taille.sum()

# part 2
totalspace = 70000000
needed = 30000000
current = data.query('type=="fic"').taille.sum()

cleanmin = (needed - totalspace + current)
data.query('type=="dir" and taille>=@cleanmin')

