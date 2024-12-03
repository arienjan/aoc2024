input = open('input.txt').readlines()

answer1 = 0
for s in input:
    numbers = [int(i) for i in s.split(' ')]
    
    
    if (numbers != sorted(numbers) and numbers != sorted(numbers, reverse=True)):
        continue
    
    counted = [abs(numbers[i] - numbers[i + 1]) > 3 or (numbers[i] - numbers[i+ 1]) == 0 for i in range(len(numbers) - 1)]

    if (counted.count(True) > 0):
        continue
        
    answer1 += 1
    
print(answer1)
        
answer2 = 0
for s in input:
    numbers = [int(i) for i in s.split(' ')]
    
    safe = False
    
    for n in range(len(numbers)):
        newNumbers = numbers[:n] + numbers[n+1 :]
        
        if (newNumbers != sorted(newNumbers) and newNumbers != sorted(newNumbers, reverse=True)):
            continue
        
        counted = [abs(newNumbers[i] - newNumbers[i + 1]) > 3 or (newNumbers[i] - newNumbers[i+ 1]) == 0 for i in range(len(newNumbers) - 1)]

        if (counted.count(True) > 0):
            continue
        
        answer2+=1
        break
        
    
print(answer2)
        
        
        