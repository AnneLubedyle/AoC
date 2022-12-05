import pandas as pd

data = pd.read_table(
    'input/input4.txt',
    sep=',|-',
    engine='python',
    names = ["min1", "max1" , "min2", "max2"])

# part 1
data['fullycontains'] = data.apply(lambda l: (l.min1>=l.min2 and l.max1<=l.max2) or (l.min2>=l.min1 and l.max2<=l.max1), axis=1)
print(data['fullycontains'].sum())

# part 2
data['overlaps'] = data.apply(lambda l: (l.max1>=l.min2 and l.max2>=l.min1), axis=1)
print(data['overlaps'].sum())


