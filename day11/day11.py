input = list(map(int, open('input.txt').readline().split()))

blinks = 75

newlist = input.copy()
newerlist = []
for i in range(blinks):
    print(i)
    newerlist = []
    for j in newlist:
        if j == 0:
            newerlist.append(1)
        elif (len(str(j)) % 2 == 0):
            newerlist.append(int(str(j)[:int(len(str(j))/2)]))
            newerlist.append(int(str(j)[int(len(str(j))/2):]))
        else:
            newerlist.append(j * 2024)
    newlist = newerlist
    #print(newerlist)
    
print(len(newerlist))

