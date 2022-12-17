git re
import pandas as pd

data = pd.read_table('input/input3.txt', names=["content"])

# part 1
data['common']= data.content.apply(
    lambda l:(set(l[:len(l)//2])&set(l[len(l)//2:])).pop())
data['score'] = data.common.apply(lambda l: ord(l)-96+58*l.isupper())
print(data.score.sum())

# part 2
data['group']=data.index//3
common = data.groupby('group').content.apply(
    lambda df: set.intersection(*[set(elt) for elt in df]).pop())
score = common.apply(lambda l: ord(l)-96+58*l.isupper())
print(score.sum())