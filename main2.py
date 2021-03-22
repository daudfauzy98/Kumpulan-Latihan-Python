array = [102, 32, 99, 32, 45, 102, 45, 67, 67, 100, 100]

for i in array:
    if array.count(i) == 1:
        print(f'Bilangan yang tidak berpasangan {i} berada di posisi {array.index(i)+1}')