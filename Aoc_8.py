import numpy as np
import matplotlib.pyplot as plt

plt.ion()

with open('input/input8.txt') as f:
    input = f.read()

input = """30373
25512
65332
33549
35390"""

data = np.array([[c for c in line] for line in input.strip().split('\n')]).astype(int)

# part 1 
visible = np.zeros(data.shape)
visible[0,:] = 1
visible[-1,:] = 1
visible[:,0] = 1
visible[:,-1] = 1

for i in range(1,data.shape[0]-1):
    for j in range(1,data.shape[1]-1):
        maxi = min([
            max(data[i,:j]),
            max(data[i,j+1:]),
            max(data[:i,j]),
            max(data[i+1:,j])])
        visible[i,j] = data[i,j] > maxi
 
visible.sum()

# part 2

def howmany(seq, h):
    res = 0
    while True:
        if res>=len(seq):
            return res
        if seq[res]>=h:
            return res + 1
        res += 1

view = np.zeros(data.shape)

for i in range(1,data.shape[0]-1):
    for j in range(1,data.shape[1]-1):
        h = data[i,j]
        a = howmany(data[:i,j][::-1], h)
        b = howmany(data[i+1:,j], h)
        c = howmany(data[i,:j][::-1], h)
        d = howmany(data[i,j+1:], h)
        view[i,j] = a*b*c*d


