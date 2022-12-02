input = "input1.txt"

# with open(input) as f:
#     content = f.read()
# qte = [sum([int(e) for e in l.split('\n')]) for l in content.rstrip().split('\n\n')]
# max(qte)
# qte.sort()
# sum(qte[-3:])

import pandas as pd
data = pd.read_table(input, names=['cal'], skip_blank_lines=False)
data['elf'] = data.isnull().cumsum()
qte_elf = data.groupby("elf").sum()
qte_elf.max()
qte_elf.cal.sort_values()[-3:].sum()
