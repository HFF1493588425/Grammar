while True:
    s = input('enter sth: ')
    if s == 'quit':
        break
    elif len(s) < 3:
        print('too small')
        continue
    else:
        print('length is sufficient length')
        break

print('done')
