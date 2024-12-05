def check_correct(update):
    correct = True
    index = 0
    for i in range(len(update) - 1):
        if f"{update[i]}|{update[i+1]}" not in rules:
            correct = False
            index = i
    return (correct, index)

myarray = open('input.txt').read().split("\n\n")

rules = myarray[0].split("\n")
updates = [l.split(',') for l  in myarray[1].split("\n")]

answer1 = 0
answer2 = 0

for u in updates:
    (correct, index) = check_correct(u)
    
    if correct:
        answer1 += int(u[int((len(u) - 1)/2)])
        continue
    
    while (not correct):
        a = u[index]
        b = u[index+1]
        u[index] = b
        u[index+1] = a

        (correct, index) = check_correct(u)
     
    answer2 += int(u[int((len(u) - 1)/2)])   
     
print(answer1)
print(answer2)