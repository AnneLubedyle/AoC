

with open('input/input9.txt') as src:
    input = src.read().strip()

depl = {
    'L': (-1, 0),
    'R': (1, 0),
    'U': (0, 1),
    'D': (0, -1)
}
def sign(x):
    if x==0: return 0
    return x/abs(x)


def process(input, n, debug=False, see = None, ngrid=(5,6)):
    position = [(0,0)] * n    
    all_positions = [position]    
    for command in input.split('\n'):
        direction, nb = command.split(' ')
        if debug or see : print("==  ",direction, nb, "  ==")
        for i in range(int(nb)):
            prev_pos = position
            position = [tuple(sum(coord) for coord in zip(position[0], depl[direction]))]
            for j in range(1,n):
                diff = [
                    position[j-1][0]-prev_pos[j][0],
                    position[j-1][1]-prev_pos[j][1]]
                if abs(diff[0])>1:
                    if debug : print('move {} x {}'.format(j, sign(diff[0])))
                    position.append(tuple([
                        prev_pos[j][0] + sign(diff[0]),
                        prev_pos[j][1] + sign(diff[1])]))
                        # position[j-1][1]]))
                    continue
                if abs(diff[1])>1:
                    if debug : print('move {} y {}'.format(j, sign(diff[1])))
                    position.append(tuple([
                        prev_pos[j][0] + sign(diff[0]),
                        # position[j-1][0],
                        prev_pos[j][1] + sign(diff[1])]))
                    continue
                position.append(prev_pos[j])         
            all_positions.append(position)
            if see:
                grid = [['.'] * ngrid[1] for a in range(ngrid[0])]
                for a,pos in reversed(list(enumerate(position))):
                    grid[int(pos[1])][int(pos[0])] = str(a)
                print('\n'.join([' '.join(l) for l in reversed(grid)]))
                print('\n\n')
            if debug : print(i, position)
        if debug : print("--------------------------------\n")
    all_tails = set(pos[-1] for pos in all_positions)
    return  len(all_tails)

# part 1
exampleinput1 = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""
process(exampleinput1, 2)
process(input, 2)

# part 2
exampleinput2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""

process(exampleinput1, 10, see=True)

process(exampleinput2, 10)
process(input, 10)