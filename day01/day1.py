input = open('input.txt').readlines()

list1=[]
list2=[]

for s in input:
    ss = s.split('   ')
    list1.append(int(ss[0].strip()))
    list2.append(int(ss[1].strip()))

answer = sum([abs(e[0] - e[1]) for e in zip(sorted(list1), sorted(list2))])
answer2 = sum([e * list2.count(e) for e in list1])

print(answer)
print(answer2)