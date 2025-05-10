f = open('Artists.txt')
content = f.read()
f.close()
with open('ArtistNames.txt', 'x') as output_f:
    content = content.split('\n')
    for (i, line) in enumerate(content):
        if i == 0:
            continue # Skip the first line
        line = line.split(',')
        try:
            output_f.write(line[1] + '\n') # Write Name to file
        except IndexError:
            continue

