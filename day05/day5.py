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
for u in updates:
    correct = check_correct(u)[0]
    if correct:
        answer1 += int(u[int((len(u) - 1)/2)])
            
print(answer1)

answer2 = 0
for u in updates:
    # whatever
    correct = check_correct(u)[0]
    index = check_correct(u)[1]
    
    if correct:
        continue
    
    while (not correct):
        a = u[index]
        b = u[index+1]
        u[index] = b
        u[index+1] = a
        
        correct = check_correct(u)[0]
        index = check_correct(u)[1]
     
    answer2 += int(u[int((len(u) - 1)/2)])   
     
print(answer2)