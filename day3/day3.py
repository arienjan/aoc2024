import re

input = open('testinput2.txt').readline()

answer = 0
for match in re.findall(r"(mul\(\d+,\d+\))", input) :
    numbers = re.search(r"(\d+,\d+)", match).group(0).split(',')
    answer += int(numbers[0])*int(numbers[1])

print(answer)

input = open('testinput2.txt').readline()
input = open('input.txt').readline()
answer = 0
do = True
for match in re.findall(r"(mul\(\d+,\d+\)|do\(\)|don\'t\(\))", input):
    
    if match == "don't()":
        do = False
        continue
    if match == "do()":
        do = True
        continue
    
    if (do):
        numbers = re.search(r"(\d+,\d+)", match).group(0).split(',')
        answer += int(numbers[0])*int(numbers[1])

print(answer)
