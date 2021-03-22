for i in range(1, 100):
    if i%3 == 0 and i%5 == 0:
        print('snip-snap, ', end=' ')
    elif i % 3 == 0:
            print('snip, ', end=' ')
    elif i % 5 == 0:
            print('snap, ', end=' ')
    else:
        print(f'{i}, ', end=' ')