import collections

with open('nama buah.txt', 'r') as f:
    NamaBuah = [line.lower().strip() for line in f]

CountNamaBuah = {i:NamaBuah.count(i) for i in NamaBuah}
SortedCountNamaBuah = {k: v for k, v in sorted(CountNamaBuah.items(), key=lambda item: item[1], reverse=True)}
# SortedCountNamaBuah = sorted(CountNamaBuah.items(), key=lambda kv: kv[1], reverse=True)
# SortedCountNamaBuah_dict = collections.OrderedDict(SortedCountNamaBuah)

for k, v in SortedCountNamaBuah.items():
    if v > 1:
        print(f'Buah {k} berjumlah {v}')

# print(SortedCountNamaBuah)
