input = list(map(int, open('input.txt').readline().split()))

blinks = 75

#newlist = input.copy()
#newerlist = []
#for i in range(blinks):
#    print(i)
#    newerlist = []
#    for j in newlist:
#        if j == 0:
#            newerlist.append(1)
#        elif (len(str(j)) % 2 == 0):
#            newerlist.append(int(str(j)[:int(len(str(j))/2)]))
#            newerlist.append(int(str(j)[int(len(str(j))/2):]))
#        else:
#            newerlist.append(j * 2024)
#    newlist = newerlist
#    #print(newerlist)
#    
#print(len(newerlist))

values0 = dict()
for j in input:
    if (j in values0):
        values0[j] += 1
    else:
        values0[j] = 1
    
values = dict()
newerlist = []
for i in range(blinks):
    values = dict()
    print(i, len(values0.keys()), sum(values0.values()))
    for j in values0.keys():
        for k in range(values0[j]):
            #print(j, k)
            strval = str(j)
            strlen = len(strval)
            if j == 0:
                if (1 in values):
                    values[1] += 1
                else:
                    values[1] = 1
            elif (strlen % 2 == 0):
                val1 = int(strval[:int(strlen/2)])
                val2 = int(strval[int(strlen/2):])

                if (val1 in values):
                    values[val1] += 1
                else:
                    values[val1] = 1
                if (val2 in values):
                    values[val2] += 1
                else:
                    values[val2] = 1
            else:
                val3 = j * 2024
                if (val3 in values):
                    values[val3] += 1
                else:
                    values[val3] = 1
    values0 = values

cout = 0
for k in values.keys():
    cout += values[k]
print(cout)

