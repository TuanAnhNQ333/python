while True:
    line = str(input())
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)