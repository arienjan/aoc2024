input = list(map(int, list(open('input.txt').read().strip())))

file_system = []
id = 0
type = 0
for f in input:
    for i in range(f):
        if (type % 2 == 0):
            file_system.append(id)
        else:
            file_system.append('.')
    
    if (type % 2 == 0):
        id += 1
    type += 1

length = len(file_system)
file_system2 = file_system.copy()

# Part 1
for i in range(length):
      
    if (i >= len(file_system)):
        break
    
    if (file_system[i] == '.'):
        b = '.'
        while(b == '.'):
            if (i >= len(file_system)):
                break
            b = file_system.pop()
          
        if (i >= len(file_system)):
            break
          
        file_system[i] = b
       
output = 0
for i in range(len(file_system)):
    output += i * file_system[i]

print(output)

# Part 2
file_system = [-1 if f == '.' else int(f) for f in file_system2]
max_id = max(file_system)
for i in range(max_id, -1, -1):
    if (i not in file_system):
        continue
    index = file_system.index(i)
    count = file_system.count(i)
    for j in range(0, length, 1):
        if (j > index or j+count > length):
            break
        block = file_system[j:j+count]
        if (len(set(block)) == 1 and block[0] == -1):
            for k in range(j, j+count, 1):
                file_system[k] = i
            for k in range(index, index+count, 1):
                file_system[k] = -1
            break

output=0
for i in range(len(file_system)):
    if file_system[i] == -1: continue
    output += i * file_system[i]
    
print(output)