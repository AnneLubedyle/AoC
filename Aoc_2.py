
import pandas as pd

input = "input2.txt"

data = pd.read_table(input, header=None, sep=" ")
#data = pd.DataFrame({0:['A','B','C'], 1:['Y','X','Z']}) # Fake data pour tester
data['A'] = data[0].map({"A":1, "B":2, "C":3})
data['B'] = data[1].map({"X":1, "Y":2, "Z":3})

# data = pd.DataFrame({"A":[1,1,1,2,2,2,3,3,3], "B":[1,2,3,1,2,3,1,2,3]})  # Fake data pour tester

# Part 1
data['win'] = data.apply(lambda row: ((row.B-row.A+1)%3)*3, axis=1)
data['score'] = data.B + data.win
data.score.sum()

# Part 2
data['play'] = data.apply(lambda row: ((row.B+row.A)%3)+1, axis=1)
data['score2'] = (data.B-1)*3 + data.play
data.score2.sum()
