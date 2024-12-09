def getdir(tuple):
    match tuple:
        case (1,0):
            return (0,1)
        case (0,1):
            return (-1,0)
        case (-1,0):
            return (0,-1)
        case (0,-1):
            return (1,0)

def getstartdir(char):
    match char:
        case '^':
            return (0,-1)
        case '>':
            return (1,0)
        case 'v':
            return (0,1)
        case '<':
            return (-1,0)

input = [list(l.strip()) for l in open('input.txt').readlines()]

xp = -1
yp = -1
startdiri = (0, 0)
for y in input:
    if (startdiri != (0,0)):
        break
    xp = -1
    yp += 1
    for x in y:
        xp += 1
        if (x == '^' or x == '>' or x == 'v' or x == '<'):
            startdiri = getstartdir(x)
            break

startpos=(xp,yp)
print(startpos, startdiri)

is_patrolling = True
startdir = startdiri
while(is_patrolling):
    input[startpos[1]][startpos[0]] = 'X'
    nextmove = (startpos[0] + startdir[0], startpos[1] + startdir[1])
    if (nextmove[1] < 0 or nextmove[1] == len(input) or nextmove[0] < 0 or nextmove[0] == len(input[0])):
        is_patrolling = False
        break

    if (input[nextmove[1]][nextmove[0]] == '#'):
        startdir = getdir(startdir)
        continue
    
    startpos = nextmove
    
x_count = 0
for y in input:
    for x in y:
        if (x == 'X'):
            x_count += 1

print(x_count)

    
##### part2
print('part 2')
loop_count = 0
for y in range(len(input)):
    for x in range(len(input[0])):
        visited_locations = []
        inputcopy = list(map(list, input))
        inputcopy[y][x] = '#'
        is_patrolling = True
        startpos=(xp,yp)
        startdir = startdiri
        while(is_patrolling):
            if ((startpos[0], startpos[1], startdir) in visited_locations):
                loop_count += 1
                break

            visited_locations.append((startpos[0], startpos[1], startdir))
            nextmove = (startpos[0] + startdir[0], startpos[1] + startdir[1])

            if (nextmove[1] < 0 or nextmove[1] == len(inputcopy) or nextmove[0] < 0 or nextmove[0] == len(inputcopy[0])):
                is_patrolling = False
                break
            
            if (inputcopy[nextmove[1]][nextmove[0]] == '#'):
                startdir = getdir(startdir)
                continue
            
            startpos = nextmove

print(loop_count)



