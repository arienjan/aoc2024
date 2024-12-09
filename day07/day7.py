def calc(i, j, part2):
    yield i + j
    yield i * j
    if part2:
        yield int(str(i) + str(j))

def testvalues(input, testvalue, part2):
    if (len(input) <= 1):
        return (input[0] == testvalue, input[0])
    for x in calc(input[0], input[1], part2):
        if x > testvalue:
            continue
        inputNew = input.copy()
        inputNew.pop(0)
        inputNew[0] = x
        retVal = testvalues(inputNew, testvalue, part2)
        if retVal[0]:
            return retVal
        else:
            continue
    return (False, -1)

input = [[int(m[0]), list(map(int, m[1].strip().split(' ')))] for m in [l.strip().split(':') for l in open('input.txt').readlines()]]
count1 = 0
count2 = 0
for l in input:
    val = testvalues(l[1], l[0], False)
    if val[0]:
        count1 += val[1]
        continue
    val2 = testvalues(l[1], l[0], True)
    if val2[0]:
        count2 += val2[1]

print(count1)
print(count1 + count2)