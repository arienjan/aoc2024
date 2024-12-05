input = [list(l.strip()) for l in open('input.txt').readlines()]
input2 = [list(k) for k in zip(*input)]
input3 = []

ylen = len(input)
xlen = len(input[0])
    
for i in range(ylen - 3):
    for j in range(xlen - 3):
        input3.append([input[i][j], input[i+1][j+1], input[i+2][j+2], input[i+3][j+3]]);
        input3.append([input[i][xlen-1-j], input[i+1][xlen-1-j-1], input[i+2][xlen-1-j-2], input[i+3][xlen-1-j-3]]);
            
count = 0
for l in [''.join(l) for l in input + input2 + input3]:

    count += l.count("XMAS")
    count += l.count("SAMX")
    
print(count)

count = 0
for i in range(1, ylen-1):
    for j in range(1, xlen-1):
        val1 = ''.join([input[i-1][j-1],input[i][j],input[i+1][j+1]])
        val2 = ''.join([input[i-1][j+1],input[i][j],input[i+1][j-1]])
        
        if ((val1 == "MAS" or val1 == "SAM") and (val2 == "MAS" or val2== "SAM") ):
            count += 1
            
print(count)
        