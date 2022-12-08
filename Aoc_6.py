
content = "mjqjpqmgbljsphdztnvjfqwrcgsmlb" # 7
content = "bvwbjplbgvbhsrlpgdmjqwftvncz" # 5
content = "nppdvjthqldpwncqszvftbrmjlhg" # 6
content = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg" # 10
content = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw" # 11
with open('input/input6.txt') as src : content = src.read()

n = 14

for i in range(n,len(content)):
    if len(set(content[i-n:i])) == n:
        print(i)
        break
