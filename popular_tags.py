from collections import Counter
import pandas as pd
list = []
tags = open("full_tags.txt").read().split('\n')
for tag in tags:
    n=  tag.split('|')
    for element in n:
        list.append(element)
d = Counter(list)

df = pd.Series(d).to_frame('Frequency')
df_sorted = df.sort_values(by='Frequency', ascending=False)
print(df_sorted.head(10))
